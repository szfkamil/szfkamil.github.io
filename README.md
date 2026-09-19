# szfkamil.github.io

Personal site of Kamil Zwoiński — a terminal-inspired, no-framework landing page.

Live: <https://kamilzwoinski.com>

## Structure

- `index.html` — the entire page, hand-written HTML
- `projects.json` — canonical project list (single source of truth, see below)
- `scripts/gen-projects.py` — regenerates the project list in `index.html` and the GitHub profile README
- `assets/scss/main.scss` — style source: SCSS tokens, nesting, color functions
- `assets/css/main.css` — compiled, minified CSS (build artifact, what browsers get)
- `.github/workflows/cloudflare-pages.yml` — builds the site and deploys it to Cloudflare Pages on push to `main`

## Projects list

The project list shown in `index.html` (`ls ~/projects`) and on the GitHub profile README
(`szfkamil/szfkamil`) is generated from `projects.json`:

```sh
python3 scripts/gen-projects.py
```

This rewrites the `<!-- projects:start -->` block in `index.html` and writes `profile-README.md`
to copy into `szfkamil/szfkamil/README.md`. The Pages workflow runs the generator before deploying,
so the live site always matches `projects.json`. Details in `notes/projects.md`.

## Building the CSS

SCSS is compiled to minified CSS with the Sass CLI:

```sh
sass --style=compressed assets/scss/main.scss assets/css/main.css
```

Edit `main.scss`; never hand-edit `main.css`.

## Deployment

`cloudflare-pages.yml` runs on every push to `main`:

1. compiles `main.css` from `main.scss`,
2. stages the deployable files (`index.html`, `assets/css/main.css`, `assets/cv.pdf`) into `dist/`,
3. uploads `dist/` to the Cloudflare Pages project `kamilzwoinski` via `cloudflare/wrangler-action`.

The site is served from the Cloudflare edge at `kamilzwoinski.com` (apex), with `www` 301-redirecting to it. `cv.pdf` is refreshed by the automation in the [`cv` repo](https://github.com/szfkamil/cv).