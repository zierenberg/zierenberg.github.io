# Scientific website of Johannes Zierenberg

A minimal, dependency-free HTML/CSS site. CV, publications, and talks are
maintained as CSV files in `data/` and pre-rendered into static HTML at
build time — no client-side fetching or JS framework required.

```
src/       HTML templates (index.html, legal.html)
public/    static assets copied as-is (css, js, images, favicon, robots.txt)
data/      CSV content, read at build time only
scripts/   build.py — stdlib-only Python static site generator
dist/      build output (generated, not committed)
```

## Build & preview locally

```
python3 scripts/build.py
python3 -m http.server -d dist
```

## Deployment

A GitHub Actions workflow (`.github/workflows/deploy.yml`) runs
`scripts/build.py` and deploys `dist/` to GitHub Pages on every push to
`main`. Requires the repo's Pages source to be set to "GitHub Actions"
(Settings → Pages → Build and deployment → Source).
