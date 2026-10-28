#!/usr/bin/env node
// Build the CMS handoff Word document for a Page Studio run.
//
// Usage: node studio/tools/handoff_docx.js <run_dir> <out.docx> [--draft "<status line>"]
//
// Reads 00-intake.md, facts.json, decisions.md, current.md, 20-content-brief.json,
// 30-page-copy.json (latest revision) and any review envelopes (3x-review-*.json),
// and lays out: how to review, decisions needed, sign-off items, the Chrome prompt
// (Part A), the change list (Part B), removals, code changes, outside scope, keep
// (Part C) and known issues from the reviews.

const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, AlignmentType, LevelFormat, PageBreak,
  Footer, PageNumber,
} = require('docx');

const [runDir, outPath, ...rest] = process.argv.slice(2);
if (!runDir || !outPath) {
  console.error('usage: node studio/tools/handoff_docx.js <run_dir> <out.docx> [--draft "<status>"]');
  process.exit(2);
}
const draftIdx = rest.indexOf('--draft');
const draftStatus = draftIdx >= 0 ? rest[draftIdx + 1] : null;

const read = (f) => fs.readFileSync(path.join(runDir, f), 'utf8');
const readJson = (f) => JSON.parse(read(f));
const exists = (f) => fs.existsSync(path.join(runDir, f));

const copyEnv = readJson('30-page-copy.json');
const copy = copyEnv.payload;
const brief = readJson('20-content-brief.json').payload;
const facts = readJson('facts.json').facts;
const currentMd = read('current.md');
const factById = Object.fromEntries(facts.map((f) => [f.id, f]));

// ---------- styling helpers ----------
const FONT = 'Arial';
const PAGE_W = 11906; // A4
const MARGIN = 1134; // 2 cm
const CONTENT_W = PAGE_W - 2 * MARGIN;
const GREY = '666666';
const SIGNOFF_FILL = 'FFF2CC'; // amber
const FALLBACK_FILL = 'E2F0D9'; // green
const NOTE_FILL = 'F2F2F2';

const border = { style: BorderStyle.SINGLE, size: 4, color: 'BFBFBF' };
const borders = { top: border, bottom: border, left: border, right: border };

function inlineRuns(text, base = {}) {
  // **bold**, [anchor](url), `code`
  const runs = [];
  const re = /(\*\*[^*]+\*\*|\[[^\]]+\]\([^)]+\)|`[^`]+`)/g;
  let last = 0;
  let m;
  while ((m = re.exec(text))) {
    if (m.index > last) runs.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    const tok = m[0];
    if (tok.startsWith('**')) runs.push(new TextRun({ text: tok.slice(2, -2), bold: true, ...base }));
    else if (tok.startsWith('`')) runs.push(new TextRun({ text: tok.slice(1, -1), font: 'Courier New', ...base }));
    else {
      const [, anchor, url] = tok.match(/\[([^\]]+)\]\(([^)]+)\)/);
      runs.push(new TextRun({ text: anchor, underline: {}, color: '1F4E79', ...base }));
      runs.push(new TextRun({ text: ` (${url})`, color: GREY, size: 18, ...base }));
    }
    last = m.index + tok.length;
  }
  if (last < text.length) runs.push(new TextRun({ text: text.slice(last), ...base }));
  return runs;
}

function para(text, opts = {}) {
  return new Paragraph({ children: inlineRuns(text, opts.run || {}), spacing: { after: 100 }, ...opts.p });
}

function heading(text, level) {
  return new Paragraph({ heading: level, children: [new TextRun(text)] });
}

function shadedPara(text, fill, label) {
  text = text.replace(/^#{1,6}\s+/, '');
  return new Paragraph({
    shading: { type: ShadingType.CLEAR, fill, color: 'auto' },
    spacing: { after: 60 },
    children: [new TextRun({ text: label, bold: true, size: 18 }), ...inlineRuns(text)],
  });
}

// Render body markdown into paragraphs. Sign-off pairs are highlighted.
function mdToParas(md) {
  const out = [];
  let held = null; // inside a sign-off block until the fallback line
  for (const raw of md.split('\n')) {
    const line = raw.trimEnd();
    if (!line.trim()) continue;
    if (held && !/\[FALLBACK UNTIL THEN\]|\[APPLY AFTER SIGN-OFF/.test(line)) {
      out.push(shadedPara(line.replace(/^\s*[-*]\s+/, '\u2022 '), SIGNOFF_FILL, ''));
      continue;
    }
    const signoff = line.match(/^\s*(?:[-*]\s+)?\[APPLY AFTER SIGN-OFF:?\s*([^\]]*)\]\s*(.*)$/);
    const fallback = line.match(/^\s*(?:[-*]\s+)?\[FALLBACK UNTIL THEN\]\s*(.*)$/);
    if (signoff) { held = signoff[1]; out.push(shadedPara(signoff[2], SIGNOFF_FILL, `APPLY AFTER SIGN-OFF (${signoff[1].trim()}): `)); continue; }
    if (fallback) { held = null; out.push(shadedPara(fallback[1], FALLBACK_FILL, 'USE UNTIL SIGNED OFF: ')); continue; }
    const h = line.match(/^(#{1,6})\s+(.*)$/);
    if (h) {
      out.push(new Paragraph({ spacing: { before: 120, after: 60 }, children: [new TextRun({ text: `${h[1]} `, color: GREY, size: 18 }), new TextRun({ text: h[2], bold: true })] }));
      continue;
    }
    const bullet = line.match(/^(\s*)[-*]\s+(.*)$/);
    if (bullet) {
      out.push(new Paragraph({ numbering: { reference: 'bullets', level: bullet[1].length >= 2 ? 1 : 0 }, spacing: { after: 40 }, children: inlineRuns(bullet[2]) }));
      continue;
    }
    if (/^\|/.test(line)) { // markdown table row: keep as monospace line
      if (/^\|[\s:-]+\|/.test(line.replace(/[^|:\- ]/g, ''))) continue;
      out.push(new Paragraph({ spacing: { after: 20 }, children: [new TextRun({ text: line, font: 'Courier New', size: 17 })] }));
      continue;
    }
    out.push(para(line));
  }
  return out;
}

function table(headers, rows, widths) {
  const total = widths.reduce((a, b) => a + b, 0);
  const cell = (text, isHead, w, fill) => new TableCell({
    borders, width: { size: w, type: WidthType.DXA },
    shading: isHead ? { type: ShadingType.CLEAR, fill: 'D9E2F3', color: 'auto' } : (fill ? { type: ShadingType.CLEAR, fill, color: 'auto' } : undefined),
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    children: String(text).split('\n').map((t) => new Paragraph({ children: inlineRuns(t, isHead ? { bold: true, size: 18 } : { size: 18 }) })),
  });
  return new Table({
    width: { size: total, type: WidthType.DXA },
    columnWidths: widths,
    rows: [
      new TableRow({ tableHeader: true, children: headers.map((h, i) => cell(h, true, widths[i])) }),
      ...rows.map((r) => new TableRow({ children: r.map((c, i) => cell(c, false, widths[i])) })),
    ],
  });
}

function fieldBlock(label, children) {
  return [new Paragraph({ spacing: { before: 80, after: 40 }, children: [new TextRun({ text: label, bold: true, color: '1F4E79' })] }), ...children];
}

function noteBox(lines) {
  return lines.map((l) => new Paragraph({ shading: { type: ShadingType.CLEAR, fill: NOTE_FILL, color: 'auto' }, spacing: { after: 40 }, children: inlineRuns(l, { size: 18 }) }));
}

// ---------- live page blocks by heading ----------
function liveBlocks(md) {
  const blocks = {};
  let cur = null;
  for (const line of md.split('\n')) {
    const h = line.match(/^#{1,3}\s+(.*)$/);
    if (h) { cur = h[1].trim(); blocks[cur] = []; continue; }
    if (cur && line.trim() && !line.startsWith('---')) blocks[cur].push(line.trim());
  }
  return blocks;
}
const live = liveBlocks(currentMd);
const liveFor = (names) => names.filter((n) => live[n]).map((n) => `[${n}]\n${live[n].join('\n')}`).join('\n\n');

const LIVE_MAP = {
  's1-hero': ['Portugal Wedding Venues', 'Portugal Wedding Venues: The Curated Luxury Guide for Your Destination Celebration'],
  's2-regions': ['The Algarve', 'Lisbon and Sintra', 'The Douro Valley', 'Comporta'],
  's3-reasons': ['Why Portugal'],
  'add-cost-bands': ['What a Portugal wedding costs'],
  's5-plan': ['Legal requirements and timing'],
  's10-advisor': ['Planning a wedding in Portugal?', 'Ready to plan your Portugal wedding?'],
  's10-form': ['Still have questions?'],
  's11-faq': ['Frequently Asked Questions'],
  's13-europe': ['Spain, the Iberia secondary'],
};

const TYPE = (id) => (id.startsWith('add-') || ['b9-qualifier', 'b8-proof-strip', 'b16-spotlight', 's4-settings', 's6-weekend', 's7-guests', 's9-celebrations', 's12-articles', 'closing-cta', 'sticky-bar', 's10-form', 's8-real-weddings'].includes(id) ? 'new block' : 'copy');

// ---------- assemble ----------
const children = [];
const title = `CMS handoff: ${brief.url}`;

children.push(new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun('CMS handoff')] }));
children.push(para(`**Page:** ${brief.url}  (https://weddedwonderland.com${brief.url})`));
children.push(para(`**Run:** ${copyEnv.run_id}    **Copy revision:** ${copyEnv.revision}    **Prepared:** ${new Date().toISOString().slice(0, 10)}`));
if (draftStatus) {
  children.push(new Paragraph({ shading: { type: ShadingType.CLEAR, fill: 'FCE4D6', color: 'auto' }, spacing: { before: 120, after: 120 }, children: [new TextRun({ text: 'REVIEW DRAFT. ', bold: true }), new TextRun(draftStatus)] }));
}

// 1. How to review
children.push(heading('1. How to review this document', HeadingLevel.HEADING_1));
children.push(para('Part B is the page in order, one numbered change per field or section. Each change shows where it goes in the CMS, the live text it replaces, the new text, and why it changed.'));
children.push(shadedPara('lines in this colour depend on a fact that still needs sign-off. Do not apply them yet.', SIGNOFF_FILL, 'Amber: '));
children.push(shadedPara('the line to use until that sign-off arrives.', FALLBACK_FILL, 'Green: '));
children.push(para('Grey text in brackets after a link is its URL. Lines starting with #### are card or tab titles inside a block.', { run: { color: GREY } }));
children.push(para('Section 10 lists issues the reviewers have already found, so you do not need to flag them again.'));

// 2. Decisions needed
children.push(heading('2. Decisions needed from you', HeadingLevel.HEADING_1));
const userQs = (copyEnv.open_questions || []).filter((q) => !/fact-checker|Please add PROPOSED|re-read pt\.usembassy|Word count is|entry_point=celebrations/i.test(q.question));
children.push(table(['#', 'Question', 'Blocking?'], userQs.map((q, i) => [String(i + 1), q.question, q.blocking ? 'Yes' : 'No, a fallback is in place']), [500, 7638, 1500]));

// 3. Sign-off items
children.push(heading('3. Facts waiting for sign-off', HeadingLevel.HEADING_1));
const pending = facts.filter((f) => f.needs_sign_off_by && f.status !== 'confirmed' || (f.needs_sign_off_by && !f.signed_off_by && /fee|price|cost|Blue Flag|B8|quote|byline/i.test(f.fact)));
children.push(table(['Fact', 'What it says', 'Status', 'Signs off'], pending.map((f) => [f.id, `${f.fact}: ${String(f.value).slice(0, 220)}`, f.status, f.needs_sign_off_by]), [800, 5838, 1300, 1700]));

// Part A
children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(heading('4. Part A: prompt for Claude in Chrome', HeadingLevel.HEADING_1));
children.push(para('Open the CMS editor for this page in Chrome, then paste this into the extension, followed by Part B (or attach this document).'));
const prompt = [
  'You are editing one page in our custom CMS, in the tab I have open. Apply the changes in the attached CMS handoff (Part B), exactly as written.',
  'Rules:',
  '1. Before changing anything, copy the current content of every field or section you will edit and show it to me, so I have a backup.',
  '2. Make the changes in the order listed. For each change, find the field or section from "Where", check that the "Current" text matches what is there now, then replace it with the "New" text. If the current text does not match, stop and tell me. Do not guess.',
  '3. Skip every line marked APPLY AFTER SIGN-OFF. Use the line marked USE UNTIL SIGNED OFF instead.',
  '4. Do not change anything that is not on the list.',
  '5. Keep the page as a draft or unpublished. Do NOT click publish, update live, or save to the live page. When all changes are in, stop and tell me they are ready for my review.',
  '6. If the editor removes or rewrites code (scripts, schema markup, form attributes, meta tags), stop and tell me which change it affected.',
  '7. When finished, list each change number with "done", "skipped" or "problem", and give a reason for anything not done.',
];
children.push(...noteBox(prompt));

// Part B
children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(heading('5. Part B: change list', HeadingLevel.HEADING_1));
children.push(para(`Order: head and meta first, then the page top to bottom. ${copy.sections.length + 4} changes. Word count of the new copy: about ${copy.word_count || 'n/a'}.`));

let n = 0;
const change = (name, type, where, current, newParas, why, signoff, check) => {
  n += 1;
  children.push(heading(`Change ${n}: ${name}`, HeadingLevel.HEADING_2));
  children.push(para(`**Type:** ${type}    **Where:** ${where}`));
  children.push(...fieldBlock('Current (live)', current ? current.split('\n').map((l) => para(l, { run: { color: GREY, size: 18 } })) : [para('None (new).', { run: { color: GREY } })]));
  children.push(...fieldBlock('New', newParas));
  if (why) children.push(...fieldBlock('Why', [para(why, { run: { size: 18 } })]));
  if (signoff) children.push(...fieldBlock('Depends on sign-off', [para(signoff, { run: { size: 18 } })]));
  if (check) children.push(...fieldBlock('Check after publishing', [para(check, { run: { size: 18 } })]));
};

change('Title tag', 'meta', 'SEO title field', 'Portugal Wedding Venues: Curated Luxury Guide | Wedded Wonderland (66 characters)', [para(`${copy.meta.title} (${copy.meta.title.length} characters)`)], 'Primary keyword "wedding in portugal" first; under 60 characters (D7).', null, 'View source: <title> shows the new text.');
change('Meta description', 'meta', 'Meta description field', 'Promises "real costs" (live, 15 Oct).', [para(`${copy.meta.description} (${copy.meta.description.length} characters)`)], 'Carries the primary keyword, regions, legal route by passport and the Wedded Advisor; drops the "real costs" promise (brief section 8).', null, 'View source: meta description shows the new text.');
change('Open Graph title and description', 'meta', 'Social sharing fields', 'Not captured.', [para(`og:title: ${copy.meta.og_title}`), para(`og:description: ${copy.meta.og_description}`)], 'Social preview matches the new page.', null, 'Paste the URL into a link preview tool.');
change('H1', 'copy', 'Page heading (H1)', 'Portugal Wedding Venues', [para(copy.h1)], 'Plan section 1 H1; "Portugal wedding venues" moves into the first sentence.', null, 'One H1 on the page.');

copy.sections.forEach((s, i) => {
  const prev = i === 0 ? 'the H1' : copy.sections[i - 1].heading.replace(/^\(no heading\)\s*/, '');
  const where = `${s.heading.replace(/^\(no heading\)\s*/, '')} (after ${prev})`;
  const signRefs = (s.fact_refs || []).filter((id) => factById[id] && factById[id].needs_sign_off_by && factById[id].status !== 'confirmed');
  const body = s.id === 's11-faq'
    ? copy.faq.flatMap((q, k) => [new Paragraph({ spacing: { before: 100, after: 40 }, children: [new TextRun({ text: `Q${k + 1}. ${q.q}`, bold: true })] }), ...mdToParas(q.a)])
    : mdToParas(s.body_md);
  if (s.captions && Object.keys(s.captions).length) {
    body.push(new Paragraph({ spacing: { before: 80 }, children: [new TextRun({ text: 'Captions', bold: true, size: 18 })] }));
    for (const [slot, cap] of Object.entries(s.captions)) body.push(...mdToParas(`- ${slot}: ${cap}`));
  }
  change(s.heading.replace(/^\(no heading\)\s*/, ''), TYPE(s.id), where, liveFor(LIVE_MAP[s.id] || []), body, s.change_reason,
    signRefs.length ? signRefs.map((id) => `${id} (${factById[id].needs_sign_off_by})`).join(', ') : null,
    s.id === 's11-faq' ? 'FAQ shows 10 questions; FAQ schema has the same 10 (code change C2).' : null);
});

// Removals
children.push(heading('6. Remove from the live page', HeadingLevel.HEADING_1));
const removals = brief.structure_changes.filter((c) => /removed/i.test(c.fate) && !c.target);
children.push(table(['Live item', 'Action', 'Note'], removals.map((c) => [c.live, c.fate, c.note || '']), [4000, 2400, 3238]));

// Code changes
children.push(heading('7. Code changes (the CMS may strip these)', HeadingLevel.HEADING_1));
children.push(...noteBox(['The final schema JSON-LD is produced at the build stage (after copy revision 2). This section lists what will change so dev can check the CMS supports it.']));
children.push(table(['#', 'Change', 'Detail'], [
  ['C1', 'Schema types', `Use: ${brief.schema_types.join(', ')}. Remove: Article and Person author. No Offer, no AggregateRating.`],
  ['C2', 'FAQPage', 'Exactly the 10 visible FAQ questions and answers, word for word (fallback versions while sign-offs are pending).'],
  ['C3', 'Enquiry form hidden fields', 'route_to=wedded-concierge, destination=Portugal, page_slug, offer, entry_point (hero, b9, region-card, costs-tab, legal-tab, closing, celebrations, sticky), utm_source, utm_medium, utm_campaign, utm_content, utm_term.'],
  ['C4', 'Form action', '/api/concierge/enquiry (confirm the real endpoint with dev).'],
  ['C5', 'Robots', 'Keep index, follow (D2: changes that need sign-off are held instead of adding noindex).'],
], [600, 2400, 6638]));

// Outside scope
children.push(heading('8. Outside this run\'s scope (dev tickets)', HeadingLevel.HEADING_1));
children.push(table(['Issue', 'Suggested fix'], [
  ['Staging (releasing-weddedwonderland.vercel.app) is indexable with a self canonical on the staging domain', 'noindex staging, or canonical to the live domain'],
  ['/destinations/europe/italy, /greece, /france and /7-ancient-and-romantic-portuguese-wedding-traditions are live but missing from the live sitemap', 'Add them to the sitemap'],
  ['Link donors should point to this page (research doc section 11)', '/trending/cristiano-ronaldo-georgina-rodriguez-wedding: one body link, anchor "wedding in Portugal"; /7-ancient-and-romantic-portuguese-wedding-traditions: contextual link here'],
  ['Wonderland Studio "Start for free" and Privacy Policy URLs are not confirmed', 'Confirm the paths before publishing'],
], [5200, 4438]));

// Part C
children.push(heading('9. Part C: do not change', HeadingLevel.HEADING_1));
children.push(...[
  'URL /destinations/europe/portugal and its canonical (correct today).',
  'index, follow (D2).',
  'The site-wide newsletter block at the foot of the page (not page copy).',
  'Parent hub /destinations/europe and its link to this page.',
].flatMap((t) => mdToParas(`- ${t}`)));

// Known issues
children.push(heading('10. Known issues already found (fixed in revision 2)', HeadingLevel.HEADING_1));
const reviewFiles = fs.readdirSync(runDir).filter((f) => /^3[0-9]-review-.*\.json$/.test(f)).sort();
if (!reviewFiles.length) children.push(para('No reviews yet.'));
for (const f of reviewFiles) {
  const r = readJson(f).payload;
  children.push(heading(`${r.lens} (${r.verdict})`, HeadingLevel.HEADING_2));
  children.push(table(['ID', 'Severity', 'Issue', 'Fix'], r.findings.map((x) => [x.id, x.severity, `${x.location}: ${x.issue}`, x.suggested_fix || '']), [800, 1100, 4400, 3338]));
}
if (exists('35-persona-copy-summary.json')) {
  const p = readJson('35-persona-copy-summary.json');
  children.push(heading('Persona panel on the copy', HeadingLevel.HEADING_2));
  children.push(table(['Persona', 'Decisions (3 runs)', 'Unanswered questions'], Object.entries(p.personas).map(([k, v]) => [k, Object.entries(v.decisions).map(([d, c]) => `${d} ${c}`).join(', '), v.unanswered_questions.join('\n')]), [2600, 2000, 5038]));
}
const pendingReviews = ['33-review-copy-facts.json'].filter((f) => !exists(f));
if (pendingReviews.length) children.push(...noteBox([`Still running when this draft was made: ${pendingReviews.join(', ')}. Its findings will be in the final version.`]));

const doc = new Document({
  creator: 'Page Studio',
  title,
  styles: {
    default: { document: { run: { font: FONT, size: 20 } } },
    paragraphStyles: [
      { id: 'Title', name: 'Title', basedOn: 'Normal', run: { size: 40, bold: true, font: FONT }, paragraph: { spacing: { after: 160 } } },
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 30, bold: true, font: FONT, color: '1F3864' }, paragraph: { spacing: { before: 300, after: 140 }, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 24, bold: true, font: FONT, color: '2E5496' }, paragraph: { spacing: { before: 240, after: 100 }, outlineLevel: 1 } },
    ],
  },
  numbering: { config: [{ reference: 'bullets', levels: [
    { level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } },
    { level: 1, format: LevelFormat.BULLET, text: '◦', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1080, hanging: 270 } } } },
  ] }] },
  sections: [{
    properties: { page: { size: { width: PAGE_W, height: 16838 }, margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [new TextRun({ text: `${brief.url}  |  page `, size: 16, color: GREY }), new TextRun({ children: [PageNumber.CURRENT], size: 16, color: GREY })] })] }) },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(outPath, buf);
  console.log(`wrote ${outPath} (${n} changes)`);
});
