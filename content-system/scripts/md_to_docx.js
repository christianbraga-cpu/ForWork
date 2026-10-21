#!/usr/bin/env node
// Turn a post's body markdown into a Word document for human review.
//
// Usage: node content-system/scripts/md_to_docx.js <body.md> <out.docx> [publish-package.json]
// - Front matter and hidden comments are removed (fact markers, CTA markers).
// - Image-slot comments become shaded "Image needed" boxes.
// - [[VERIFY: ...]] notes are highlighted yellow.
// - If a publish package is given, a review note (title, meta, sign-offs,
//   draft note) goes at the top.
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, ExternalHyperlink,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
  LevelFormat, AlignmentType,
} = require('docx');

const SITE = 'https://weddedwonderland.com';
const [, , mdPath, outPath, pkgPath] = process.argv;
if (!mdPath || !outPath) {
  console.error('Usage: node md_to_docx.js <body.md> <out.docx> [publish-package.json]');
  process.exit(1);
}

let md = fs.readFileSync(mdPath, 'utf8');
md = md.replace(/^---\n[\s\S]*?\n---\n/, '');
md = md.replace(/<!--\s*IMAGE SLOT\s*([\w-]+):\s*([\s\S]*?)-->/g, (_, id, brief) =>
  `\n@@IMAGE ${id}|${brief.replace(/\s+/g, ' ').trim()}\n`);
md = md.replace(/<!--[\s\S]*?-->/g, '');

// Inline: **bold**, [text](url), [[VERIFY: ...]]
function inline(text, base = {}) {
  const out = [];
  const re = /(\[\[VERIFY:[^\]]*\]\])|\*\*\[([^\]]+)\]\(([^)]+)\)\*\*|\[([^\]]+)\]\(([^)]+)\)|\*\*([^*]+)\*\*|\*([^*]+)\*/g;
  let last = 0, m;
  const push = (t, o = {}) => t && out.push(new TextRun({ text: t, ...base, ...o }));
  while ((m = re.exec(text))) {
    push(text.slice(last, m.index));
    if (m[1]) push(m[1], { highlight: 'yellow' });
    else if (m[2] || m[4]) {
      const label = m[2] || m[4];
      let url = m[3] || m[5];
      if (url.startsWith('/')) url = SITE + url;
      out.push(new ExternalHyperlink({ link: url, children: [
        new TextRun({ text: label, style: 'Hyperlink', bold: !!m[2], ...base }),
      ] }));
    } else if (m[6]) push(m[6], { bold: true });
    else if (m[7]) push(m[7], { italics: true });
    last = re.lastIndex;
  }
  push(text.slice(last));
  return out;
}

const CONTENT_W = 9026; // A4 with 1" margins, in DXA
const border = { style: BorderStyle.SINGLE, size: 4, color: 'BBBBBB' };
const borders = { top: border, bottom: border, left: border, right: border };

function imageBox(id, brief) {
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: [CONTENT_W],
    rows: [new TableRow({ children: [new TableCell({
      width: { size: CONTENT_W, type: WidthType.DXA },
      borders,
      shading: { type: ShadingType.CLEAR, color: 'auto', fill: 'EDE7DD' },
      margins: { top: 100, bottom: 100, left: 140, right: 140 },
      children: [
        new Paragraph({ children: [new TextRun({ text: `Image needed: ${id}`, bold: true })] }),
        new Paragraph({ children: [new TextRun({ text: brief, italics: true, size: 18 })] }),
      ],
    })] })],
  });
}

function mdTable(lines) {
  const rows = lines
    .filter(l => !/^\|\s*-/.test(l))
    .map(l => l.replace(/^\||\|$/g, '').split('|').map(c => c.trim()));
  const n = rows[0].length;
  const w = Math.floor(CONTENT_W / n);
  const widths = Array(n).fill(w);
  widths[n - 1] += CONTENT_W - w * n;
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: widths,
    rows: rows.map((r, i) => new TableRow({ tableHeader: i === 0, children: r.map((c, j) =>
      new TableCell({
        width: { size: widths[j], type: WidthType.DXA },
        borders,
        shading: i === 0 ? { type: ShadingType.CLEAR, color: 'auto', fill: 'E4DCCF' } : undefined,
        margins: { top: 60, bottom: 60, left: 100, right: 100 },
        children: [new Paragraph({ children: inline(c, { size: 18, bold: i === 0 }) })],
      })) })),
  });
}

const children = [];

if (pkgPath && fs.existsSync(pkgPath)) {
  const raw = JSON.parse(fs.readFileSync(pkgPath, 'utf8'));
  const p = raw.payload || raw;
  children.push(new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun(p.title || '')] }));
  const note = (label, value) => value && children.push(new Paragraph({ children: [
    new TextRun({ text: `${label}: `, bold: true }), new TextRun(String(value)) ] }));
  note('Status', 'DRAFT for review. Not published.');
  note('URL', p.seo && p.seo.canonical);
  note('Primary category', p.primary_category);
  note('Meta title', p.seo && p.seo.meta_title);
  note('Meta description', p.seo && p.seo.meta_description);
  (p.needs_signoff || []).forEach(s => note('Needs sign-off', s));
  if (p.draft_note) {
    children.push(new Paragraph({ spacing: { before: 120 }, children: [new TextRun({ text: 'Review note', bold: true })] }));
    p.draft_note.split(/\n+/).filter(Boolean).forEach(l =>
      children.push(new Paragraph({ children: inline(l.replace(/^[-*]\s*/, ''), { size: 18 }) })));
  }
  children.push(new Paragraph({
    border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: 'B89A66', space: 6 } },
    spacing: { after: 240 }, children: [],
  }));
}

const lines = md.split('\n');
for (let i = 0; i < lines.length; i++) {
  const line = lines[i].trimEnd();
  if (!line.trim()) continue;
  if (line.startsWith('@@IMAGE ')) {
    const [id, brief] = line.slice(8).split('|');
    children.push(imageBox(id, brief || ''));
    children.push(new Paragraph({ children: [] }));
  } else if (line.startsWith('|')) {
    const block = [];
    while (i < lines.length && lines[i].trim().startsWith('|')) block.push(lines[i++].trim());
    i--;
    children.push(mdTable(block));
    children.push(new Paragraph({ children: [] }));
  } else if (/^#{1,4} /.test(line)) {
    const level = line.match(/^#+/)[0].length;
    const map = { 1: HeadingLevel.HEADING_1, 2: HeadingLevel.HEADING_1, 3: HeadingLevel.HEADING_2, 4: HeadingLevel.HEADING_3 };
    children.push(new Paragraph({ heading: map[level], children: inline(line.replace(/^#+ /, '')) }));
  } else if (/^\s*[-*] /.test(line)) {
    children.push(new Paragraph({ numbering: { reference: 'bullets', level: 0 }, children: inline(line.replace(/^\s*[-*] /, '')) }));
  } else if (line.startsWith('> ')) {
    children.push(new Paragraph({ indent: { left: 360 }, children: inline(line.slice(2), { italics: true }) }));
  } else {
    children.push(new Paragraph({ spacing: { after: 140 }, children: inline(line) }));
  }
}

const doc = new Document({
  styles: {
    default: { document: { run: { font: 'Calibri', size: 22 } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 32, bold: true, font: 'Georgia', color: '3A2E22' }, paragraph: { spacing: { before: 360, after: 160 }, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 26, bold: true, font: 'Georgia', color: '3A2E22' }, paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1 } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 23, bold: true, font: 'Georgia' }, paragraph: { spacing: { before: 200, after: 100 }, outlineLevel: 2 } },
    ],
  },
  numbering: { config: [{ reference: 'bullets', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•',
    alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] }] },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    children,
  }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(outPath, buf);
  console.log(`Wrote ${outPath}`);
});
