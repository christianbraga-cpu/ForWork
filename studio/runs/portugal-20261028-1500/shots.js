const { chromium } = require('playwright');
const path = require('path');
const run = '/home/user/ForWork/studio/runs/portugal-20261028-1500';
const url = 'file://' + run + '/preview.html';
(async () => {
  const browser = await chromium.launch();
  const out = [];
  for (const [name, w, h] of [['mobile', 390, 844], ['desktop', 1440, 900]]) {
    const ctx = await browser.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    const page = await ctx.newPage();
    await page.goto(url, { waitUntil: 'load' });
    const sw = await page.evaluate(() => document.documentElement.scrollWidth);
    const full = path.join(run, 'screens', `${name}-full.png`);
    await page.screenshot({ path: full, fullPage: true });
    out.push(full);
    const total = await page.evaluate(() => document.documentElement.scrollHeight);
    const n = Math.ceil(total / h);
    for (let i = 0; i < n; i++) {
      await page.evaluate(y => window.scrollTo(0, y), i * h);
      await page.waitForTimeout(250);
      const f = path.join(run, 'screens', `${name}-${String(i + 1).padStart(2, '0')}.png`);
      await page.screenshot({ path: f });
      out.push(f);
    }
    console.log(name, 'scrollWidth', sw, 'height', total, 'slices', n);
    await ctx.close();
  }
  await browser.close();
  console.log(out.join('\n'));
})();
