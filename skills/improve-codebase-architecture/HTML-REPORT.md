# HTML Report Format

The architectural review is one self-contained HTML file in the OS temp directory. It must remain readable and complete offline. Use only document-local CSS, semantic HTML, and inline SVG. Do not execute remote JavaScript or load fonts, CSS frameworks, diagram libraries, or other assets from a CDN.

## Scaffold

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Architecture review - {{repo name}}</title>
  <style>
    :root { color-scheme: light; font-family: ui-sans-serif, system-ui, sans-serif; }
    * { box-sizing: border-box; }
    body { margin: 0; background: #fafaf9; color: #0f172a; }
    main { width: min(1080px, calc(100% - 40px)); margin: 0 auto; padding: 48px 0 72px; }
    article { background: white; border: 1px solid #e2e8f0; border-radius: 14px; padding: 24px; margin: 28px 0; }
    .pair { display: grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap: 16px; }
    .diagram { min-height: 300px; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px; overflow: hidden; }
    .badge { display: inline-block; border-radius: 999px; padding: 4px 9px; font-size: 12px; font-weight: 700; }
    .strong { background: #d1fae5; color: #065f46; }
    .explore { background: #fef3c7; color: #92400e; }
    .speculative { background: #e2e8f0; color: #334155; }
    .module { fill: #fff; stroke: #334155; stroke-width: 2; }
    .deep { fill: #1e293b; stroke: #0f172a; stroke-width: 4; }
    .seam { stroke: #64748b; stroke-width: 2; stroke-dasharray: 6 5; }
    .leak { stroke: #dc2626; stroke-width: 3; }
    @media (max-width: 760px) { .pair { grid-template-columns: 1fr; } }
  </style>
</head>
<body>
  <main>
    <header>...</header>
    <section id="candidates">...</section>
    <section id="top-recommendation">...</section>
  </main>
</body>
</html>
```

The file contains no `<script>` tags and no external stylesheet, image, font, or module imports. If a logo or other small visual is truly necessary, use inline SVG rather than a network URL.

## Candidate card

Each candidate is one `<article>` with sparse prose and a strong visual comparison:

- **Title**: name the deepening
- **Badge row**: `Strong`, `Worth exploring`, or `Speculative`, plus dependency category
- **Files**: compact monospaced list
- **Before / After**: side-by-side self-contained diagrams
- **Problem**: one sentence
- **Solution**: one sentence
- **Wins**: short bullets phrased in locality, leverage, depth, interface, and seam terms
- **ADR callout**: only when the candidate conflicts with a real ADR

The diagrams carry the explanation. If a diagram needs a paragraph to make sense, redraw it.

## Diagram patterns

### Inline SVG dependency graph

Use SVG for call graphs, dependencies, and leakage. Give every edge its own explicit style so leakage styling applies to the edge itself, not to adjacent nodes.

```html
<svg viewBox="0 0 520 220" role="img" aria-label="Before: pricing leaks across the repository seam">
  <rect class="module" x="20" y="70" width="120" height="56" rx="8" />
  <rect class="module" x="200" y="70" width="120" height="56" rx="8" />
  <rect class="module" x="380" y="70" width="120" height="56" rx="8" />
  <text x="80" y="103" text-anchor="middle">Order handler</text>
  <text x="260" y="103" text-anchor="middle">Order repo</text>
  <text x="440" y="103" text-anchor="middle">Pricing</text>
  <path d="M140 98 H200" stroke="#334155" stroke-width="2" marker-end="url(#arrow)" />
  <path class="leak" d="M320 98 H380" marker-end="url(#arrow-red)" />
</svg>
```

Use `<defs><marker>...</marker></defs>` for arrow heads when needed. Keep labels in the SVG so the graphic is useful without scripts.

### Hand-built boxes and arrows

Use positioned HTML boxes with an inline SVG overlay when text wrapping matters more than graph layout. The before state can show several shallow modules; the after state can show one thick-bordered deep module with its internals faded.

### Cross-section

Stack horizontal bands to show a call crossing too many shallow modules. The after state should visibly collapse unnecessary seams.

### Mass diagram

Represent interface surface and implementation mass as two proportional rectangles. A shallow module has interface mass close to implementation mass; a deep module has a small interface and much larger hidden implementation.

### Call-graph collapse

Draw the before state as a tree of calls. Draw the after state as one deep module with internal calls faded inside the box and only the public interface exposed.

## Accessibility and resilience

- Every meaningful SVG gets `role="img"` and an `aria-label` describing the architectural point.
- Keep important meaning in text as well as color; leakage uses a label or line style in addition to red.
- Preserve sufficient contrast and a logical reading order.
- Keep the report useful when SVG cannot render by including one-sentence Problem and Solution text for each candidate.
- No runtime network dependency is permitted.

## Style guidance

Use a restrained editorial layout with generous whitespace. Avoid dashboard chrome. One neutral palette plus one accent is enough; red is reserved for leakage and amber for ADR warnings. Keep diagrams around 300-340px tall so before/after fits comfortably side by side.

## Top recommendation

End with one larger card containing the candidate name, one sentence explaining why it has the highest leverage, and an anchor link back to the candidate.

## Vocabulary

Use exactly the architecture vocabulary from `codebase-design`: module, interface, implementation, depth, deep, shallow, seam, adapter, leverage, locality.
