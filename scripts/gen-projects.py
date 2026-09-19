#!/usr/bin/env python3
"""Regenerate the project list on the website and the GitHub profile README.

Single source of truth: projects.json.

Usage:
    python3 scripts/gen-projects.py

Writes:
    index.html          — replaces the <!-- projects:start -->..<!-- projects:end --> block
    profile-README.md   — full profile README for github.com/szfkamil/szfkamil (copy there)
"""
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "projects.json"
INDEX = ROOT / "index.html"
PROFILE = ROOT / "profile-README.md"

START = "<!-- projects:start -->"
END = "<!-- projects:end -->"


def load_projects():
    with open(DATA, encoding="utf-8") as f:
        return json.load(f)["projects"]


def html_block(projects):
    items = []
    for p in projects:
        items.append(
            "        <li>\n"
            f'          <a href="{p["url"]}">{p["name"]}</a>\n'
            f'          <span class="desc">\u2014 {html.escape(p["description"])}</span>\n'
            "        </li>"
        )
    return (
        f"      {START}\n"
        "      <ul class=\"output list\">\n"
        + "\n".join(items)
        + "\n      </ul>\n"
        f"      {END}"
    )


def render_index(projects):
    text = INDEX.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit(f"error: markers {START} / {END} not found in {INDEX}")
    head, _, tail = text.partition(START)
    _, _, rest = tail.partition(END)
    head = re.sub(r"[ \t]*$", "", head)
    return head + html_block(projects) + rest


def markdown_block(projects):
    return "\n".join(
        f"*   [**{p['name']}**]({p['url']}) \u2013 {p['description']}" for p in projects
    )


def render_profile(projects):
    return (
        "# Kamil Zwoi\u0144ski\n"
        "\n"
        "Computer Science student at the University of Gda\u0144sk.\n"
        "\n"
        "- **Website:** [kamilzwoinski.com](https://kamilzwoinski.com)\n"
        "- **CV:** [kamilzwoinski.com/assets/cv.pdf](https://kamilzwoinski.com/assets/cv.pdf)\n"
        "\n"
        "## Projects\n"
        "\n"
        f"{markdown_block(projects)}\n"
    )


def main():
    projects = load_projects()
    INDEX.write_text(render_index(projects), encoding="utf-8")
    PROFILE.write_text(render_profile(projects), encoding="utf-8")
    print(
        f"wrote {INDEX.name} and {PROFILE.name} from {DATA.name} "
        f"({len(projects)} project{'s' if len(projects) != 1 else ''})"
    )


if __name__ == "__main__":
    main()