#!/usr/bin/env python3
"""Pre-render CV/publications/talks from CSV into static HTML.

Stdlib only, no external dependencies. Reads src/ + data/ + public/,
writes a fully static site to dist/.
"""
import csv
import html
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DATA = ROOT / "data"
PUBLIC = ROOT / "public"
DIST = ROOT / "dist"

SITE_URL = "https://zierenberg.github.io"


def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=";")
        return [
            {k: (v or "").strip() for k, v in row.items() if k}
            for row in reader
            if any((v or "").strip() for v in row.values())
        ]


def e(value):
    return html.escape(value, quote=True)


def render_cv(rows):
    out = []
    seen_sections = set()
    for row in rows:
        section = row.get("section", "")
        if section and section not in seen_sections:
            out.append(f'<h3 class="cv-section" data-section="{e(section)}">{e(section)}</h3>')
            seen_sections.add(section)

        note = row.get("note", "")
        location = row.get("location", "")
        note_html = f'<div class="cv-note">{e(note)}</div>' if note else ""
        out.append(f"<dt>{e(row.get('date', ''))}</dt>")
        out.append(
            "<dd>"
            f"<strong>{e(row.get('role', ''))}</strong><br>"
            f"{e(row.get('institution', ''))}{', ' + e(location) if location else ''}"
            f"{note_html}"
            "</dd>"
        )
    return "\n".join(out)


def render_publications(rows):
    out = []
    for row in rows:
        volume = row.get("volume", "")
        pages = row.get("pages", "")
        vol_pages = volume + (", " + pages if pages else "")
        title = e(row.get("title", ""))
        url = row.get("url", "")
        title_html = f'<a href="{e(url)}" target="_blank" rel="noopener">{title}</a>' if url else title
        out.append(
            "<li>"
            f"{e(row.get('authors', ''))}, <strong>{title_html}</strong>, "
            f"<em>{e(row.get('journal', ''))}</em> "
            f'<span class="mono">{e(vol_pages)} ({e(row.get("year", ""))})</span>'
            "</li>"
        )
    return "\n".join(out)


def render_talks(rows):
    out = []
    for row in rows:
        type_ = row.get("type", "")
        venue_place = ", ".join(x for x in (row.get("venue", ""), row.get("place", "")) if x)
        comments = row.get("comments", "")
        type_html = f"({e(type_)})" if type_ else ""
        comment_html = f" - {e(comments)}" if comments else ""
        out.append(
            "<li>"
            f"{e(row.get('title', ''))} {type_html}<br>"
            f'<em>{e(venue_place)}</em>, <span class="mono">{e(row.get("date", ""))}</span>'
            f"{comment_html}"
            "</li>"
        )
    return "\n".join(out)


def build_index():
    template = (SRC / "index.html").read_text(encoding="utf-8")
    cv_html = render_cv(read_csv(DATA / "cv.csv"))
    pub_html = render_publications(read_csv(DATA / "publications.csv"))
    talk_html = render_talks(read_csv(DATA / "talks.csv"))

    out = template.replace("<!--CV-->", cv_html)
    out = out.replace("<!--PUBLICATIONS-->", pub_html)
    out = out.replace("<!--TALKS-->", talk_html)
    (DIST / "index.html").write_text(out, encoding="utf-8")


def build_sitemap():
    urls = ["/", "/legal.html"]
    entries = "\n".join(f"  <url><loc>{SITE_URL}{u}</loc></url>" for u in urls)
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{entries}\n"
        "</urlset>\n"
    )
    (DIST / "sitemap.xml").write_text(sitemap, encoding="utf-8")


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    shutil.copytree(PUBLIC, DIST, dirs_exist_ok=True)
    shutil.copy(SRC / "legal.html", DIST / "legal.html")
    build_index()
    build_sitemap()
    print(f"Built site to {DIST}")


if __name__ == "__main__":
    main()
