#!/usr/bin/env node
// Build the simple review document for a Page Studio run: the final page copy in
// order, as it should read on the page, plus a short "before you publish" list.
// Technical detail (fact ids, change reasons, QA, schema) stays in handoff_docx.js.
//
// Usage: node studio/tools/review_docx.js <run_dir> <out.docx> "<Page name>"

const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, AlignmentType, LevelFormat, PageBreak, Footer, PageNumber,
} = require('docx');

const [runDir, outPath, pageName = 'Page'] = process.argv.slice(2);
if (!runDir || !outPath) {
  console.error('usage: node studio/tools/review_docx.js <run_dir> <out.docx> "<Page name>"');
  process.exit(2);
}
const readJson = (f) => JSON.parse(fs.readFileSync(path.join(runDir, f), 'utf8'));
const env = readJson('30-page-copy.json');
const copy = env.payload;
const brief = readJson('20-content-brief.json').payload;

const FONT = 'Arial';
const GREY = '767676';
const AMBER = 'FFF2CC';
const PAGE_W = 11906;
const MARGIN = 1247; // 2.2 cm
const CONTENT_W = PAGE_W - 2 * MARGIN;

const links = new Map(); // anchor -> url, for the table at the end
const signoffs = []; // { owner, what }

const ownerName = (o) => (/project lead/i.test(o) ? 'You (Project Lead)' : o.trim());

// Remove build and CMS notes so only page text remains.
function clean(line) {
  return line
    .replace(/CMS note\b.*$/i, '')
    .replace(/\([^()]*(?:Dev|CMS|entry_point|Tab label|anchor:|prefills|sets |loaded on click|form posts)[^()]*\)/gi, '')
    .replace(/\(anchor:[^)]*\)/g, '')
    .replace(/\s{2,}/g, ' ')
    .trim();
}

function runs(text, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|\[Button[^\]]*\]\([^)]*\)|\[[^\]]+\]\([^)]+\))/g;
  let last = 0;
  let m;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    const tok = m[0];
    if (tok.startsWith('**')) out.push(new TextRun({ text: tok.slice(2, -2), bold: true, ...base }));
    else if (tok.startsWith('[Button')) {
      const label = tok.match(/\[Button[^:]*:\s*([^\]]+)\]/)[1];
      out.push(new TextRun({ text: `[ ${label} ]`, bold: true, color: '1F4E79', ...base }));
    } else {
      const [, anchor, url] = tok.match(/\[([^\]]+)\]\(([^)]+)\)/);
      if (!url.startsWith('#')) links.set(anchor, url);
      out.push(new TextRun({ text: anchor, underline: {}, color: '1F4E79', ...base }));
    }
    last = m.index + tok.length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), ...base }));
  return out;
}

const p = (text, base, opts = {}) => new Paragraph({ children: runs(text, base), spacing: { after: 120 }, ...opts });

function note(text) {
  return new Paragraph({
    shading: { type: ShadingType.CLEAR, fill: AMBER, color: 'auto' },
    spacing: { after: 120 },
    children: runs(text, { size: 18 }),
  });
}

// Render one block of copy markdown as page text.
function render(md) {
  const out = [];
  const lines = md.split('\n');
  for (let i = 0; i < lines.length; i++) {
    const raw = lines[i];
    const so = raw.match(/\[APPLY AFTER SIGN-OFF:?\s*([^\]]*)\]\s*(.*)$/);
    if (so) {
      // Collect the held block up to the fallback line.
      const held = [so[2]];
      let j = i + 1;
      while (j < lines.length && !/\[FALLBACK UNTIL THEN\]/.test(lines[j]) && !/\[APPLY AFTER SIGN-OFF/.test(lines[j])) held.push(lines[j++]);
      const owner = ownerName(so[1].split(',').slice(1).join(',') || 'sign-off');
      const fb = j < lines.length && /\[FALLBACK UNTIL THEN\]/.test(lines[j]) ? lines[j].replace(/.*\[FALLBACK UNTIL THEN\]\s*/, '') : '';
      if (fb) out.push(...render(fb));
      const heldText = held.map(clean).filter((l) => l && !/^\|[\s:|-]+\|$/.test(l)).map((l) => l.replace(/^#{1,6}\s+/, '')).join(' ');
      out.push(note(`Once ${owner} signs off, replace the line above with: ${heldText.slice(0, 600)}${heldText.length > 600 ? ' ...' : ''}`));
      signoffs.push({ owner, what: heldText.slice(0, 110) });
      i = j;
      continue;
    }
    const line = clean(raw.replace(/\[FALLBACK UNTIL THEN\]\s*/, ''));
    if (!line) continue;
    if (/entry_point|hidden field|Hidden fields|route_to|utm_|page_slug|Prefill rules|prefill/i.test(line)) continue;
    if (/^\|/.test(line)) continue; // tables only appear inside held cost blocks
    const h = line.match(/^(#{1,6})\s+(.*)$/);
    if (h) {
      const level = h[1].length <= 2 ? HeadingLevel.HEADING_2 : HeadingLevel.HEADING_3;
      out.push(new Paragraph({ heading: level, children: [new TextRun(h[2])] }));
      continue;
    }
    const b = line.match(/^(\s*)[-*]\s+(.*)$/);
    if (b) { out.push(new Paragraph({ numbering: { reference: 'b', level: 0 }, spacing: { after: 60 }, children: runs(b[2]) })); continue; }
    out.push(p(line));
  }
  return out;
}

const children = [];
children.push(new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun(`${pageName}: final copy for review`)] }));
children.push(p(`${brief.url}   |   Copy revision ${env.revision}   |   ${new Date().toISOString().slice(0, 10)}`, { color: GREY, size: 18 }));
children.push(p(fs.existsSync(path.join(runDir, 'fix-report.json')) ? 'Page 1 goes through each problem on the live page and what we changed. The full new copy follows for reference.' : 'This is the page exactly as it should read, top to bottom. Read it the way a couple would. Mark anything that sounds wrong, or anything you know is not true.'));
children.push(p('Amber boxes are lines waiting for someone to sign off. The page works without them; swap them in once approved.', { size: 18, color: GREY }));

// Fix report: what was broken on the live page and what we did, item by item.
const fixPath = path.join(runDir, 'fix-report.json');
const fix = fs.existsSync(fixPath) ? JSON.parse(fs.readFileSync(fixPath, 'utf8')) : null;
function bullets(items, base = {}) {
  return (items || []).map((t) => new Paragraph({ numbering: { reference: 'b', level: 0 }, spacing: { after: 50 }, children: runs(t, base) }));
}
function statusChip(status) {
  const ok = /^Fixed$|^Removed/.test(status);
  return new Paragraph({ spacing: { after: 80 }, children: [new TextRun({ text: ` ${status} `, bold: true, size: 18, shading: { type: ShadingType.CLEAR, fill: ok ? 'E2F0D9' : AMBER, color: 'auto' } })] });
}

// Body first so the sign-off list is complete when we build the summary.
const body = [];
body.push(new Paragraph({ children: [new PageBreak()] }));
body.push(new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun('Search result')] }));
body.push(p(`**Title:** ${copy.meta.title}`));
body.push(p(`**Description:** ${copy.meta.description}`));
body.push(new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun(fix ? 'The full new copy' : 'The page')] }));
for (const s of copy.sections) {
  if (/hidden at launch/i.test(s.heading) || /^Hidden at launch/i.test(s.body_md)) continue;
  if (s.id === 'sticky-bar') continue;
  if (s.id === 's11-faq') {
    body.push(...render(s.body_md.split('\n').filter((l) => /^#{1,2}\s/.test(l)).join('\n')));
    copy.faq.forEach((q, k) => {
      body.push(new Paragraph({ spacing: { before: 160, after: 60 }, children: [new TextRun({ text: `${k + 1}. ${q.q}`, bold: true })] }));
      body.push(...render(q.a));
    });
    continue;
  }
  if (!/^\s*#/.test(s.body_md) && !/^\(no heading\)/.test(s.heading)) body.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(s.heading)] }));
  const LABELS = { 'b9': 'Bar under the main heading (fills in the form)', 'b8': 'Proof line', 'beach': 'Line under the Algarve card', 'closing': 'Closing line after the questions' };
  if (/^\(no heading\)/.test(s.heading)) {
    const key = Object.keys(LABELS).find((k) => s.id.toLowerCase().includes(k));
    body.push(p(key ? LABELS[key] : s.heading.replace(/^\(no heading\)\s*/, ''), { color: GREY, size: 16, italics: true }));
  }
  body.push(...render(s.body_md));
}
const sticky = copy.sections.find((s) => s.id === 'sticky-bar');
if (sticky) { body.push(p('Mobile sticky bar', { color: GREY, size: 16, italics: true })); body.push(...render(sticky.body_md)); }

if (fix) {
  children.push(new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun('What was broken, and what we did')] }));
  children.push(p(fix.summary));
  fix.items.forEach((it, k) => {
    children.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(`${k + 1}. ${it.broken}`)] }));
    children.push(statusChip(it.status));
    if (it.before && it.before.length) { children.push(p('**Live page now**', { size: 18, color: GREY }, { spacing: { after: 40 } })); children.push(...bullets(it.before, { color: GREY, size: 19 })); }
    children.push(p('**New copy**', { size: 18 }, { spacing: { before: 80, after: 40 } }));
    children.push(...bullets(it.after));
    if (it.note) children.push(p(it.note, { size: 18, color: GREY, italics: true }));
  });
  children.push(new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun('What we need from you')] }));
  children.push(...bullets(fix.your_answers_needed));
  children.push(p('Everything else is ready. The full new copy follows, in page order, for reference.', { size: 18, color: GREY }));
}
if (!fix) {
// Before you publish
children.push(new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun('Before you publish')] }));
const byOwner = {};
for (const s of signoffs) (byOwner[s.owner] ||= new Set()).add(s.what.replace(/\s+\S*$/, '') + '...');
for (const [owner, items] of Object.entries(byOwner)) {
  children.push(p(`**${owner} to sign off** (${items.size}):`));
  for (const it of items) children.push(new Paragraph({ numbering: { reference: 'b', level: 0 }, spacing: { after: 40 }, children: runs(it, { size: 18 }) }));
}
children.push(p('**Dev:** confirm the enquiry form endpoint, the Privacy Policy and Wonderland Studio links, and that the CMS keeps the schema code (in the technical file).'));
children.push(p('**Hidden on purpose:** the real weddings section stays hidden until there are 3 Portugal weddings to show.', { size: 18 }));
}

children.push(...body);

// Chrome prompt and links
children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun('To apply it with Claude in Chrome')] }));
children.push(note('Open this page in the CMS editor. Paste: "Replace the page copy with the attached document, section by section. Copy the current text of each field to me first as a backup. Use the normal text, not the amber boxes. Change nothing else. Do not publish: stop when it is ready for my review." Then attach this document.'));
if (links.size) {
  children.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('Links on this page')] }));
  const border = { style: BorderStyle.SINGLE, size: 4, color: 'BFBFBF' };
  const borders = { top: border, bottom: border, left: border, right: border };
  const w = [Math.round(CONTENT_W * 0.45), CONTENT_W - Math.round(CONTENT_W * 0.45)];
  const cell = (t, i, head) => new TableCell({ borders, width: { size: w[i], type: WidthType.DXA }, margins: { top: 50, bottom: 50, left: 90, right: 90 },
    shading: head ? { type: ShadingType.CLEAR, fill: 'E7EEF7', color: 'auto' } : undefined,
    children: [new Paragraph({ children: [new TextRun({ text: t, size: 17, bold: head })] })] });
  children.push(new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: w, rows: [
    new TableRow({ tableHeader: true, children: [cell('Link text', 0, true), cell('Goes to', 1, true)] }),
    ...[...links].map(([a, u]) => new TableRow({ children: [cell(a, 0), cell(u, 1)] })),
  ] }));
}

const doc = new Document({
  creator: 'Page Studio',
  title: `${pageName}: final copy`,
  styles: {
    default: { document: { run: { font: FONT, size: 21 } } },
    paragraphStyles: [
      { id: 'Title', name: 'Title', basedOn: 'Normal', run: { size: 36, bold: true, font: FONT }, paragraph: { spacing: { after: 120 } } },
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 28, bold: true, font: FONT, color: '1F3864' }, paragraph: { spacing: { before: 280, after: 120 }, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 25, bold: true, font: FONT, color: '2E5496' }, paragraph: { spacing: { before: 260, after: 100 }, outlineLevel: 1 } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 22, bold: true, font: FONT }, paragraph: { spacing: { before: 160, after: 60 }, outlineLevel: 2 } },
    ],
  },
  numbering: { config: [{ reference: 'b', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 500, hanging: 260 } } } }] }] },
  sections: [{
    properties: { page: { size: { width: PAGE_W, height: 16838 }, margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [new TextRun({ text: `${pageName}  |  `, size: 16, color: GREY }), new TextRun({ children: [PageNumber.CURRENT], size: 16, color: GREY })] })] }) },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(outPath, buf);
  console.log(`wrote ${outPath}: ${signoffs.length} sign-off lines, ${links.size} links`);
});
