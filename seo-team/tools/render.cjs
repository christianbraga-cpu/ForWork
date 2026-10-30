#!/usr/bin/env node
// Render a page on mobile and desktop for the persona panel and technical QA.
//
// Usage: node seo-team/tools/render.cjs <page.html or URL> <out_dir>
//
// Writes mobile.png, desktop.png (full page), mobile-fold.png, desktop-fold.png
// (first screen) and render.json with LCP element,
// CLS, horizontal overflow and console errors. Uses the pre-installed Playwright.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const VIEWPORTS = {
  mobile: { width: 390, height: 844, deviceScaleFactor: 2, isMobile: true, hasTouch: true },
  desktop: { width: 1440, height: 900, deviceScaleFactor: 1 },
};

(async () => {
  const [target, outDir] = process.argv.slice(2);
  if (!target || !outDir) {
    console.error('Usage: node render.cjs <page.html|URL> <out_dir>');
    process.exit(2);
  }
  const url = /^https?:\/\//.test(target) ? target : 'file://' + path.resolve(target);
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const result = { url, viewports: {} };

  for (const [name, vp] of Object.entries(VIEWPORTS)) {
    const { width, height, ...opts } = vp;
    const ctx = await browser.newContext({ viewport: { width, height }, ...opts });
    const page = await ctx.newPage();
    const consoleErrors = [];
    page.on('console', (m) => { if (m.type() === 'error') consoleErrors.push(m.text()); });
    await page.addInitScript(() => {
      window.__lcp = null; window.__cls = 0;
      new PerformanceObserver((l) => {
        const e = l.getEntries().pop();
        if (e) window.__lcp = { time: e.startTime, tag: e.element ? e.element.tagName : null,
          id: e.element ? e.element.id : null, cls: e.element ? e.element.className : null, url: e.url || null };
      }).observe({ type: 'largest-contentful-paint', buffered: true });
      new PerformanceObserver((l) => {
        for (const e of l.getEntries()) if (!e.hadRecentInput) window.__cls += e.value;
      }).observe({ type: 'layout-shift', buffered: true });
    });
    try {
      await page.goto(url, { waitUntil: 'load', timeout: 45000 });
    } catch (e) {
      consoleErrors.push('navigation: ' + e.message);
    }
    await page.waitForTimeout(1500);
    const metrics = await page.evaluate(() => ({
      lcp: window.__lcp,
      cls: Math.round(window.__cls * 1000) / 1000,
      horizontalOverflow: document.documentElement.scrollWidth > window.innerWidth,
      scrollWidth: document.documentElement.scrollWidth,
      title: document.title,
    }));
    const shot = path.join(outDir, `${name}.png`);
    const fold = path.join(outDir, `${name}-fold.png`);
    await page.screenshot({ path: fold });
    await page.screenshot({ path: shot, fullPage: true });
    result.viewports[name] = { ...metrics, screenshot: shot, fold, consoleErrors };
    await ctx.close();
  }
  await browser.close();
  fs.writeFileSync(path.join(outDir, 'render.json'), JSON.stringify(result, null, 2));
  console.log(JSON.stringify(result, null, 2));
})();
