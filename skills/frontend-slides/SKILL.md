---
name: html-ppt-warm-editorial
description: >-
  Create elegant HTML/CSS presentation slides with a "warm paper editorial"
  aesthetic — parchment background, serif headings, muted green/gold accent
  palette, paper-grain texture, smooth slide transitions, and keyboard/dot
  navigation. Use when the user asks to build an HTML slideshow, a web-based
  presentation, or a PPT-style deck in HTML/CSS/JS. Works with plain HTML,
  Vue, React, or any component framework.
---

# HTML PPT — Warm Paper Editorial

**Visual language:** parchment base (#F4E8C8), warm brown grain overlay, serif display type (Georgia), muted green (#4E6750) + amber gold (#C28E2D) accents, translucent card surfaces, soft warm shadows.

For complete component templates, see [components.md](components.md).  
For the full CSS token reference, see [tokens.md](tokens.md).

---

## Design tokens (CSS vars — always paste into `:root`)

```css
:root {
  --bg:        #F4E8C8;
  --surface:   rgba(255,252,242,0.68);
  --surface-s: rgba(255,252,242,0.86);
  --text:      #171512;
  --text-2:    #3A342B;
  --text-m:    rgba(58,52,43,0.62);
  --green:     #4E6750;
  --green-l:   rgba(78,103,80,0.13);
  --gold:      #C28E2D;
  --gold-l:    rgba(226,187,112,0.24);
  --rose:      #A8463E;
  --border:    rgba(93,67,33,0.16);
  --border-s:  rgba(93,67,33,0.28);
  --shadow:    0 18px 24px rgba(68,54,28,0.08);
  --shadow-md: 0 20px 34px rgba(68,54,28,0.12);
  --shadow-sm: 0 8px 18px rgba(68,54,28,0.06);
  --r:         12px;
  --r-lg:      16px;
}
```

---

## Deck shell (HTML skeleton)

```html
<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Deck Title</title>
  <style>/* paste tokens + base styles from tokens.md */</style>
</head>
<body>
  <div class="deck">
    <div class="progress-bar"><div class="progress-fill" id="progress"></div></div>
    <div class="slide-counter" id="counter"></div>
    <button class="nav-btn nav-prev" id="prev">‹</button>
    <button class="nav-btn nav-next" id="next">›</button>
    <div class="dot-nav" id="dots"></div>
    <div class="slides-wrapper" id="slides">
      <!-- slide divs go here -->
    </div>
  </div>
  <script>/* paste nav script from components.md */</script>
</body>
</html>
```

---

## Base CSS (deck + slide shell)

```css
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background: var(--bg);
  overflow: hidden;
  font-family: -apple-system, 'PingFang SC', 'Helvetica Neue', sans-serif;
}
.deck { position: fixed; inset: 0; background: var(--bg); color: var(--text); }
.slides-wrapper { width: 100%; height: 100%; position: relative; }

/* — slide — */
.slide {
  position: absolute; inset: 0;
  display: flex; flex-direction: column;
  justify-content: center; align-items: center;
  padding: 60px 80px;
  opacity: 0; pointer-events: none;
  transform: translateX(40px);
  transition: opacity 0.4s ease, transform 0.4s ease;
  background:
    radial-gradient(circle at 18% 20%, rgba(226,187,112,0.18), transparent 30%),
    radial-gradient(circle at 88% 74%, rgba(78,103,80,0.13), transparent 34%),
    var(--bg);
  overflow: hidden;
}
.slide::before {          /* paper grain */
  content: '';
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(93,67,33,0.035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(93,67,33,0.025) 1px, transparent 1px);
  background-size: 32px 32px, 44px 44px;
  mix-blend-mode: multiply;
  opacity: 0.5;
  pointer-events: none; z-index: 0;
}
.slide > * { position: relative; z-index: 1; }
.slide.active { opacity: 1; pointer-events: all; transform: translateX(0); }

/* — chrome — */
.progress-bar { position: fixed; top: 0; left: 0; right: 0; height: 3px; background: var(--border); z-index: 100; }
.progress-fill { height: 100%; background: linear-gradient(90deg, var(--green), var(--gold)); transition: width 0.4s ease; }
.slide-counter { position: fixed; top: 16px; right: 24px; font-size: 13px; color: var(--text-m); z-index: 100; font-weight: 500; }
.nav-btn {
  position: fixed; top: 50%; transform: translateY(-50%);
  background: var(--surface-s); border: 1.5px solid var(--border);
  color: var(--green); font-size: 28px; width: 44px; height: 44px;
  border-radius: 50%; cursor: pointer; z-index: 100;
  transition: all 0.2s; display: flex; align-items: center; justify-content: center;
}
.nav-btn:hover:not(:disabled) { border-color: rgba(194,142,45,0.45); color: var(--gold); }
.nav-btn:disabled { opacity: 0.3; cursor: default; }
.nav-prev { left: 20px; } .nav-next { right: 20px; }
.dot-nav { position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); display: flex; gap: 6px; z-index: 100; }
.dot { width: 6px; height: 6px; border-radius: 50%; background: rgba(93,67,33,0.22); border: none; cursor: pointer; transition: all 0.2s; }
.dot.active { background: var(--green); width: 20px; border-radius: 3px; }

/* — global type — */
.slide-tag { display: inline-block; font-size: 12px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: var(--green); margin-bottom: 14px; }
.slide-title { font-family: Georgia,'Times New Roman','Songti SC',serif; font-size: clamp(36px,4vw,54px); font-weight: 500; color: var(--text); line-height: 1.2; margin-bottom: 10px; text-align: center; }
.slide-subtitle { font-size: 18px; color: var(--green); margin-bottom: 32px; text-align: center; line-height: 1.7; font-weight: 600; }
```

---

## Navigation script

```js
(function () {
  const slides = document.querySelectorAll('.slide');
  const total = slides.length;
  let cur = 0;
  const $progress = document.getElementById('progress');
  const $counter  = document.getElementById('counter');
  const $prev     = document.getElementById('prev');
  const $next     = document.getElementById('next');
  const $dots     = document.getElementById('dots');

  slides.forEach((_, i) => {
    const b = document.createElement('button');
    b.className = 'dot'; b.onclick = () => goTo(i); $dots.appendChild(b);
  });

  function goTo(n) {
    if (n < 0 || n >= total) return;
    slides[cur].classList.remove('active');
    $dots.children[cur].classList.remove('active');
    cur = n;
    slides[cur].classList.add('active');
    $dots.children[cur].classList.add('active');
    $progress.style.width = ((cur + 1) / total * 100) + '%';
    $counter.textContent = (cur + 1) + ' / ' + total;
    $prev.disabled = cur === 0; $next.disabled = cur === total - 1;
  }

  $prev.onclick = () => goTo(cur - 1);
  $next.onclick = () => goTo(cur + 1);
  document.addEventListener('keydown', e => {
    if (['ArrowRight',' ','ArrowDown'].includes(e.key)) { e.preventDefault(); goTo(cur + 1); }
    if (['ArrowLeft','ArrowUp'].includes(e.key)) { e.preventDefault(); goTo(cur - 1); }
  });
  goTo(0);
})();
```

---

## Slide layout patterns

### Cover (image + big title)
```html
<div class="slide slide-cover">
  <div class="cover-layout">
    <div class="cover-copy">
      <h1 class="cover-title"><span>Title</span><span>Line Two</span></h1>
      <p class="cover-sub">副标题 / Subtitle</p>
    </div>
    <div class="cover-hero"><img src="hero.png" alt=""></div>
  </div>
</div>
```
```css
.cover-layout { display: grid; grid-template-columns: minmax(320px,.86fr) minmax(380px,1.14fr); align-items: center; gap: 54px; max-width: 1130px; width: 100%; }
.cover-title { font-family: Georgia,serif; font-size: clamp(52px,6vw,84px); font-weight: 500; line-height: 1.06; display: flex; flex-direction: column; }
.cover-sub { font-size: 22px; color: var(--green); letter-spacing: 6px; margin-top: 18px; }
.cover-hero img { width: 100%; filter: drop-shadow(var(--shadow)) saturate(.96); }
```

### Split (text + image/content)
```html
<div class="slide">
  <div class="split-layout">
    <div class="split-left"><!-- heading, copy, quote --></div>
    <div class="split-right"><!-- image, cards, code --></div>
  </div>
</div>
```
```css
.split-layout { display: grid; grid-template-columns: minmax(340px,.86fr) minmax(480px,1.14fr); align-items: center; gap: 52px; width: min(1160px,100%); }
.split-left, .split-right { min-width: 0; }
@media (max-width: 980px) { .split-layout { grid-template-columns: 1fr; gap: 24px; } }
```

### Full-bleed image slide
```html
<div class="slide" style="justify-content: flex-start; padding: 32px 60px 24px;">
  <h2 class="slide-title" style="margin-bottom:18px;">Slide Title</h2>
  <img src="diagram.png" style="max-width:min(90vw,1100px); max-height:calc(100vh - 160px); object-fit:contain;">
  <p class="note-block">Optional footnote or caption text goes here.</p>
</div>
```

### Two-column element (badge + heading + points / code)
```html
<div class="slide slide-element">
  <div class="el-two-col">
    <div>
      <div class="el-badge">01 / Section</div>
      <h2 class="el-title">Main Concept</h2>
      <p class="el-subtitle">One-line description</p>
      <div class="core-statement">Key insight or quote here.</div>
      <div class="point-list">
        <div class="el-point"><span class="cp-num">①</span><div><strong>Item</strong>：detail text</div></div>
      </div>
    </div>
    <div class="example-panel"><!-- code blocks or cards --></div>
  </div>
</div>
```
```css
.slide-element { padding: 54px 72px; }
.el-two-col { display: grid; grid-template-columns: minmax(340px,.86fr) minmax(480px,1.14fr); align-items: center; gap: 52px; width: min(1160px,100%); }
.el-badge { font-size: 12px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: var(--green); margin-bottom: 14px; }
.el-title { font-family: Georgia,serif; font-size: clamp(34px,4vw,52px); font-weight: 500; line-height: 1.14; color: var(--text); margin-bottom: 12px; }
.el-subtitle { font-size: 18px; color: var(--green); font-weight: 600; line-height: 1.7; }
.point-list { margin-top: 16px; display: flex; flex-direction: column; gap: 9px; }
.el-point { display: flex; gap: 10px; align-items: flex-start; font-size: 14px; color: var(--text-2); line-height: 1.7; background: var(--surface); border: 1.5px solid var(--border); border-radius: 8px; padding: 11px 13px; box-shadow: var(--shadow-sm); }
.el-point strong { color: var(--text); }
.cp-num { font-weight: 700; color: var(--gold); flex-shrink: 0; font-size: 15px; line-height: 1.7; }
```

---

## Common components

### Card
```html
<div class="illus-card" style="padding:16px 18px;">Card content</div>
```
```css
.illus-card { background: var(--surface); border: 1.5px solid var(--border); border-radius: var(--r); box-shadow: var(--shadow-sm); }
```

### Gold quote block
```html
<div class="core-statement">Quoted insight or key statement.</div>
```
```css
.core-statement { margin-top: 20px; padding: 18px 20px; border-left: 4px solid var(--gold); background: var(--surface); color: #2D291F; font-size: 17px; line-height: 1.78; font-weight: 600; }
```

### Note / callout block
```html
<p class="note-block">Footnote or context note.</p>
```
```css
.note-block { padding: 12px 18px; background: var(--surface); border: 1.5px solid var(--border); border-left: 4px solid var(--gold); border-radius: 8px; box-shadow: var(--shadow-sm); color: var(--text-2); font-size: 14px; line-height: 1.68; }
```

### Dark code block
```html
<div class="illus-code">
  <div class="code-label">filename.sh</div>
  <pre><code>// code here</code></pre>
</div>
```
```css
.illus-code { background: rgba(42,37,30,0.92); border: 1.5px solid var(--border); border-radius: 8px; overflow: hidden; box-shadow: var(--shadow); }
.illus-code .code-label { padding: 8px 16px; background: rgba(255,252,242,0.08); border-bottom: 1.5px solid rgba(255,252,242,0.1); font-size: 12px; color: rgba(255,252,242,0.62); font-weight: 600; }
.illus-code pre { padding: 16px; overflow: auto; margin: 0; }
.illus-code code { font-family: 'JetBrains Mono','Fira Code',monospace; font-size: 12px; color: #FFF7DF; line-height: 1.7; white-space: pre-wrap; }
```

### Data table
```html
<table class="illus-table">
  <thead><tr><th>列1</th><th>列2</th></tr></thead>
  <tbody><tr><td>项</td><td>说明</td></tr></tbody>
</table>
```
```css
.illus-table { width: 100%; border-collapse: collapse; font-size: 13px; background: rgba(255,252,242,0.68); border: 1.5px solid var(--border); border-radius: 8px; overflow: hidden; box-shadow: var(--shadow-sm); }
.illus-table th, .illus-table td { border: 1px solid rgba(93,67,33,0.12); padding: 9px 11px; text-align: left; vertical-align: top; line-height: 1.55; }
.illus-table th { background: var(--green-l); color: var(--green); font-weight: 800; white-space: nowrap; }
.illus-table td:first-child { font-weight: 700; color: var(--text); white-space: nowrap; }
```

### Hover tooltip
```html
<span class="term-tip">hover me
  <span class="term-tip-body" role="tooltip">
    <span class="tip-lead">Title line</span>
    <span class="tip-row">Detail line</span>
  </span>
</span>
```
```css
.term-tip { position: relative; cursor: help; border-bottom: 1.5px dashed rgba(194,142,45,0.45); }
.term-tip:hover { border-bottom-color: rgba(194,142,45,0.85); }
.term-tip-body { position: absolute; left: 0; bottom: calc(100% + 10px); z-index: 20; width: min(320px,80vw); padding: 12px 14px; border-radius: 8px; border: 1.5px solid var(--border); background: #FFF7DF; box-shadow: var(--shadow-md); font-size: 13px; line-height: 1.55; color: var(--text-2); pointer-events: none; opacity: 0; transform: translateY(4px); transition: opacity 0.15s, transform 0.15s; }
.term-tip:hover .term-tip-body { opacity: 1; transform: translateY(0); }
.tip-lead { display: block; margin-bottom: 6px; color: var(--text); font-weight: 600; }
.tip-row { display: block; margin-top: 4px; font-size: 12px; line-height: 1.5; }
```

---

## Utility classes

```css
.accent-text { color: var(--green); font-weight: 700; }
.gold-text   { color: var(--gold);  font-weight: 700; }
.rose-text   { color: var(--rose);  font-weight: 700; }
.muted-text  { color: var(--text-m); }
.res-links a { font-size: 13px; color: var(--green); text-decoration: none; font-weight: 700; }
.res-links a:hover { color: var(--gold); text-decoration: underline; }
```

---

## Workflow

1. **Gather content** — titles, body text, images, code snippets, key quotes
2. **Assign slide types** — cover / split / full-image / element / summary
3. **Paste base** — tokens + base CSS + deck shell + nav script
4. **Build each slide** — pick the matching layout pattern and drop in content
5. **Polish** — tweak `clamp()` font sizes, spacing, adjust radial gradient positions per slide
6. **Accessibility** — add `alt` on all images, `role="tooltip"` on tooltips, `aria-label` on nav buttons
