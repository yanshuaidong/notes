# Components Reference — Warm Paper Editorial

Complete, copy-paste-ready HTML+CSS blocks for every component used in this
design system. Each block is self-contained: paste the HTML where needed and
add the CSS once to your stylesheet.

---

## 1. Cover slide

```html
<div class="slide slide-cover active">
  <div class="cover-layout">
    <div class="cover-copy">
      <h1 class="cover-title">
        <span>Main</span>
        <span>Title</span>
      </h1>
      <p class="cover-sub">副标题 · Subtitle</p>
    </div>
    <div class="cover-hero">
      <img src="hero.png" alt="Hero illustration">
    </div>
  </div>
</div>
```

```css
.slide-cover {
  background:
    radial-gradient(circle at 22% 26%, rgba(226,187,112,0.20), transparent 30%),
    radial-gradient(circle at 82% 68%, rgba(78,103,80,0.12),  transparent 34%),
    #F4E8C8;
}
.slide-cover::before { display: none; } /* replace grain with custom version if needed */

.cover-layout {
  display: grid;
  grid-template-columns: minmax(320px,.86fr) minmax(380px,1.14fr);
  align-items: center;
  gap: 54px;
  max-width: 1130px;
  width: 100%;
}
.cover-copy { text-align: left; }
.cover-hero { justify-self: end; width: min(55vw, 620px); }
.cover-hero img { display: block; width: 100%; filter: drop-shadow(0 18px 24px rgba(68,54,28,.08)) saturate(.96); }

.cover-title {
  font-family: Georgia,'Times New Roman','Songti SC',serif;
  font-size: clamp(52px,6.2vw,84px);
  font-weight: 500;
  line-height: 1.06;
  display: flex;
  flex-direction: column;
  color: #171512;
}
.cover-sub {
  font-size: 22px;
  color: #4E6750;
  letter-spacing: 6px;
  margin-top: 18px;
}

@media (max-width: 860px) {
  .cover-layout { grid-template-columns: 1fr; gap: 22px; }
  .cover-hero { justify-self: center; width: min(78vw, 480px); }
  .cover-title { font-size: 48px; }
}
```

---

## 2. Split slide (text + visual)

```html
<div class="slide">
  <div class="split-layout">
    <div class="split-left">
      <div class="slide-tag">Section Tag</div>
      <h2 class="slide-title" style="text-align:left;">Slide Heading</h2>
      <p class="slide-subtitle" style="text-align:left; margin-bottom:0;">Subtitle / lead sentence.</p>
      <div class="core-statement">Key insight or pull quote goes here.</div>
    </div>
    <div class="split-right">
      <!-- image, cards, or code block -->
      <img src="visual.png" alt="" style="width:100%; border-radius:12px; box-shadow:var(--shadow);">
    </div>
  </div>
</div>
```

```css
.split-layout {
  display: grid;
  grid-template-columns: minmax(340px,.86fr) minmax(480px,1.14fr);
  align-items: center;
  gap: 52px;
  width: min(1160px,100%);
}
.split-left, .split-right { min-width: 0; }
.core-statement {
  margin-top: 22px;
  padding: 18px 20px;
  border-left: 4px solid var(--gold);
  background: var(--surface);
  color: #2D291F;
  font-size: 17px;
  line-height: 1.78;
  font-weight: 600;
}

@media (max-width: 980px) {
  .split-layout { grid-template-columns: 1fr; gap: 24px; }
}
```

---

## 3. Two-column element slide (badge + points + code)

```html
<div class="slide slide-element">
  <div class="el-two-col">

    <div class="el-left">
      <div class="el-badge">01 / Topic</div>
      <h2 class="el-h2">Concept Title</h2>
      <p class="el-subtitle">One-line description of this concept.</p>
      <div class="core-statement">Central insight or quoted statement.</div>
      <div class="point-list">
        <div class="el-point"><span class="cp-num">①</span><div><strong>First point</strong>：explanation</div></div>
        <div class="el-point"><span class="cp-num">②</span><div><strong>Second point</strong>：explanation</div></div>
        <div class="el-point"><span class="cp-num">③</span><div><strong>Third point</strong>：explanation</div></div>
      </div>
    </div>

    <div class="el-right">
      <div class="illus-code">
        <div class="code-label">example.sh</div>
        <pre><code># your code here
echo "Hello"</code></pre>
      </div>
    </div>

  </div>
</div>
```

```css
.slide-element { padding: 54px 72px; align-items: center; }
.el-two-col { display: grid; grid-template-columns: minmax(340px,.86fr) minmax(480px,1.14fr); align-items: center; gap: 52px; width: min(1160px,100%); }
.el-left, .el-right { min-width: 0; }
.el-badge { font-size: 12px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: var(--green); margin-bottom: 14px; }
.el-h2 { font-family: Georgia,serif; font-size: clamp(34px,4vw,52px); font-weight: 500; line-height: 1.14; color: var(--text); margin-bottom: 12px; }
.el-subtitle { font-size: 18px; color: var(--green); font-weight: 600; line-height: 1.7; }
.point-list { margin-top: 16px; display: flex; flex-direction: column; gap: 9px; }
.el-point { display: flex; gap: 10px; align-items: flex-start; font-size: 14px; color: var(--text-2); line-height: 1.7; background: var(--surface); border: 1.5px solid var(--border); border-radius: 8px; padding: 11px 13px; box-shadow: var(--shadow-sm); }
.el-point strong { color: var(--text); }
.cp-num { font-weight: 700; color: var(--gold); flex-shrink: 0; font-size: 15px; line-height: 1.7; }

@media (max-width: 980px) {
  .el-two-col { grid-template-columns: 1fr; gap: 24px; }
  .slide-element { padding: 48px 28px; }
}
```

---

## 4. Summary slide (left panel + table)

```html
<div class="slide">
  <div class="split-layout">
    <div class="split-left">
      <div class="slide-tag">总结</div>
      <h2 class="slide-title" style="text-align:left; font-size:clamp(42px,5vw,68px);">
        Closing<br>Statement.
      </h2>
      <p style="font-size:19px; color:var(--green); letter-spacing:2px; margin-top:14px;">Chinese subtitle</p>
      <div class="core-statement">
        <span class="term-tip">Key quoted phrase.
          <span class="term-tip-body" role="tooltip">
            <span class="tip-lead">Tooltip headline</span>
            <span class="tip-row">Detail line one</span>
          </span>
        </span>
        <span style="display:block; margin-top:8px; font-size:13px; color:var(--green); font-weight:700;">— Author · Org</span>
      </div>
    </div>

    <div class="split-right">
      <div style="margin-bottom:12px;">
        <h3 style="font-size:16px; font-weight:800; color:var(--text); margin-bottom:6px;">Best Practices</h3>
        <p style="font-size:13px; color:var(--text-m); line-height:1.5;">Short description of what the table covers.</p>
      </div>
      <table class="illus-table">
        <thead><tr><th>要点</th><th>怎么做</th></tr></thead>
        <tbody>
          <tr><td>First item</td><td>How to do it, including <code>code snippet</code> if needed</td></tr>
          <tr><td>Second item</td><td>Explanation</td></tr>
        </tbody>
      </table>
      <div style="margin-top:14px;">
        <div style="font-size:12px; color:var(--text-m); margin-bottom:8px;">参考资源</div>
        <div class="res-links">
          <a href="#" target="_blank">Link one</a>
          <a href="#" target="_blank">Link two</a>
        </div>
      </div>
    </div>
  </div>
</div>
```

```css
.illus-table { width:100%; border-collapse:collapse; font-size:13px; background:rgba(255,252,242,.68); border:1.5px solid var(--border); border-radius:8px; overflow:hidden; box-shadow:var(--shadow-sm); }
.illus-table th, .illus-table td { border:1px solid rgba(93,67,33,.12); padding:9px 11px; text-align:left; vertical-align:top; line-height:1.55; }
.illus-table th { background:var(--green-l); color:var(--green); font-weight:800; white-space:nowrap; }
.illus-table td:first-child { font-weight:700; color:var(--text); white-space:nowrap; width:1%; }
.illus-table code { font-family:'JetBrains Mono','Fira Code',monospace; font-size:.92em; background:var(--green-l); color:var(--green); padding:1px 5px; border-radius:4px; }
.res-links { display:flex; gap:12px; flex-wrap:wrap; }
.res-links a { font-size:13px; color:var(--green); text-decoration:none; font-weight:700; }
.res-links a:hover { color:var(--gold); text-decoration:underline; }
```

---

## 5. Dark code block (with optional highlight demo badge)

```html
<div class="illus-code">
  <div class="code-label">filename.ts</div>
  <pre><code><span class="c"># comment in amber</span>
const result = await agent.run(task);</code></pre>
</div>

<!-- demo/highlight variant -->
<div class="illus-code demo-code">
  <div class="code-label demo-label">🌟 Demo — highlighted example</div>
  <pre><code>// highlighted code block</code></pre>
</div>
```

```css
.illus-code { background:rgba(42,37,30,.92); border:1.5px solid var(--border); border-radius:8px; overflow:hidden; box-shadow:var(--shadow); }
.illus-code .code-label { padding:8px 16px; background:rgba(255,252,242,.08); border-bottom:1.5px solid rgba(255,252,242,.1); font-size:12px; color:rgba(255,252,242,.62); font-weight:600; }
.illus-code pre { padding:16px; overflow:auto; margin:0; }
.illus-code code { font-family:'JetBrains Mono','Fira Code',monospace; font-size:12px; color:#FFF7DF; line-height:1.7; white-space:pre-wrap; }
.illus-code .c { color:rgba(226,187,112,.72); } /* amber comments */

.demo-code { border-color:rgba(194,142,45,.55) !important; box-shadow:0 0 0 1px rgba(194,142,45,.15),var(--shadow) !important; }
.demo-label { color:rgba(226,187,112,.88) !important; }
```

---

## 6. Hover tooltip

```html
<span class="term-tip">hover phrase
  <span class="term-tip-body" role="tooltip">
    <span class="tip-lead">Tooltip title</span>
    <span class="tip-row tip-before"><strong>Before</strong>: old situation</span>
    <span class="tip-row tip-now"><strong>Now</strong>: new situation</span>
  </span>
</span>
```

```css
.term-tip { position:relative; cursor:help; border-bottom:1.5px dashed rgba(194,142,45,.45); outline:none; }
.term-tip:hover, .term-tip:focus-visible { border-bottom-color:rgba(194,142,45,.85); }
.term-tip-body { position:absolute; left:0; bottom:calc(100% + 10px); z-index:20; width:min(320px,80vw); padding:12px 14px; border-radius:8px; border:1.5px solid var(--border); background:#FFF7DF; box-shadow:var(--shadow-md); font-size:13px; font-weight:500; line-height:1.55; color:var(--text-2); pointer-events:none; opacity:0; transform:translateY(4px); transition:opacity .15s,transform .15s; }
.term-tip:hover .term-tip-body, .term-tip:focus-visible .term-tip-body { opacity:1; transform:translateY(0); }
.tip-lead { display:block; margin-bottom:6px; color:var(--text); font-weight:600; }
.tip-row { display:block; margin-top:4px; font-size:12px; line-height:1.5; }
.tip-before { color:var(--rose); }
.tip-now { color:var(--green); }
```

---

## 7. Note / callout block (gold left border)

```html
<p class="note-block">
  Contextual note, caption, or footnote. Supports <strong>bold</strong> and <code>code</code>.
</p>
```

```css
.note-block { padding:12px 18px; background:rgba(255,252,242,.78); border:1.5px solid var(--border); border-left:4px solid var(--gold); border-radius:8px; box-shadow:var(--shadow-sm); color:var(--text-2); font-size:14px; line-height:1.68; }
```

---

## 8. Detail card stack

```html
<div class="detail-stack">
  <div class="detail-card">
    <div class="detail-card-title">Card Title</div>
    Body text with <strong>bold</strong> and <code>code</code>.
    <div class="detail-card-muted">Muted supplementary text</div>
  </div>
  <div class="detail-card">…</div>
</div>
```

```css
.detail-stack { display:grid; gap:14px; }
.detail-card { background:var(--surface); border:1.5px solid var(--border); border-radius:8px; padding:16px 18px; color:var(--text-2); line-height:1.74; box-shadow:var(--shadow-sm); }
.detail-card-title { color:var(--text); font-size:16px; font-weight:700; margin-bottom:7px; }
.detail-card-muted { color:var(--text-m); font-size:14px; margin-top:6px; }
.detail-card code { background:var(--green-l); color:var(--green); padding:1px 6px; border-radius:4px; font-size:.92em; }
```

---

## 9. Utility classes

```css
/* text accents */
.accent-text { color:var(--green); font-weight:700; }
.gold-text   { color:var(--gold);  font-weight:700; }
.rose-text   { color:var(--rose);  font-weight:700; }
.muted-text  { color:var(--text-m); }

/* inline code (light bg) */
code { font-family:'JetBrains Mono','Fira Code',monospace; font-size:.9em; background:var(--green-l); color:var(--green); padding:1px 6px; border-radius:4px; }

/* reduced-motion */
@media (prefers-reduced-motion: reduce) {
  .slide, .progress-fill, .nav-btn, .dot, .term-tip-body { transition: none !important; }
}

/* responsive slide padding */
@media (max-width: 980px) {
  .slide { padding: 48px 28px; overflow-y: auto; }
  .slide-title { font-size: 36px; }
}
```
