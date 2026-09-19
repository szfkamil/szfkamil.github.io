# szfkamil.github.io

Personal site of Kamil Zwoiński — a terminal-inspired, no-framework landing page.

Live: <https://szfkamil.github.io/>

## Structure

- `index.html` — the entire page, hand-written HTML
- `assets/scss/main.scss` — style source: SCSS tokens, nesting, color functions
- `assets/css/main.css` — compiled, minified CSS (build artifact, what browsers get)
- `.github/workflows/pages.yml` — deploys the repo as static content to GitHub Pages on push to `main`

## Building the CSS

SCSS is compiled to minified CSS with the Sass CLI:

```sh
sass --style=compressed assets/scss/main.scss assets/css/main.css
```

Edit `main.scss`; never hand-edit `main.css`.