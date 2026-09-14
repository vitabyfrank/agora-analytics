#!/usr/bin/env python3
"""Check the generated guide, local documentation links, and portable assets."""

import base64
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

from build import ROOT, OUTPUT, build_html


class GuideParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.fragments: list[str] = []
        self.lang = None
        self.external_assets: list[str] = []
        self.retention_rows: list[list[str]] = []
        self._in_retention = False
        self._row: list[str] = []
        self._cell: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "table" and "retention-matrix" in (values.get("class") or "").split():
            self._in_retention = True
        if self._in_retention:
            if tag == "tr":
                self._row = []
            elif tag in ("th", "td"):
                self._cell = ""
        if tag == "html":
            self.lang = values.get("lang")
        if values.get("id"):
            self.ids.append(values["id"])
        href = values.get("href", "") or ""
        if href.startswith("#"):
            self.fragments.append(href[1:])
        if tag in ("script", "img", "iframe", "link"):
            asset = values.get("src") or (href if tag == "link" else "")
            if asset and not asset.startswith("data:"):
                self.external_assets.append(asset)

    def handle_data(self, data: str) -> None:
        if self._cell is not None:
            self._cell += data

    def handle_endtag(self, tag: str) -> None:
        if not self._in_retention:
            return
        if tag in ("th", "td") and self._cell is not None:
            self._row.append(self._cell.strip())
            self._cell = None
        elif tag == "tr":
            self.retention_rows.append(self._row)
        elif tag == "table":
            self._in_retention = False


def numeric_cell(value: str) -> str | None:
    """Normalize a numeric table cell across English and Korean units."""
    value = value.strip().replace(",", "").replace("$", "")
    match = re.fullmatch(r"(\d+)\s*(days?|minutes?|seconds?|일|분|초|회)?", value)
    if not match:
        return None
    units = {"day": "d", "days": "d", "일": "d", "minute": "m", "minutes": "m", "분": "m",
             "second": "s", "seconds": "s", "초": "s", "회": "", None: ""}
    return match.group(1) + units[match.group(2)]


def guide_rows(path: Path) -> list[tuple[str, list[str | None]]]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        label = cells[0]
        if label in ("Starter", "Standard", "Premium", "Enterprise") or label in (
            "Call Inspector · Console", "Call Inspector · REST API",
            "Data Insights · Console", "Data Insights · REST API",
        ):
            values = [numeric_cell(cell) for cell in cells[1:]]
            if any(value is not None for value in values):
                rows.append((label, values))
    return rows


def local_markdown_links(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.findall(r"\[[^\]]*\]\(<?([^\s)>]+)>?\)", text)


def main() -> int:
    errors: list[str] = []
    if not OUTPUT.is_file():
        print("Missing index.html. Run python3 scripts/build.py first.")
        return 1
    html = OUTPUT.read_text(encoding="utf-8")
    if html != build_html():
        errors.append("Generated HTML is stale; run python3 scripts/build.py.")

    parser = GuideParser()
    parser.feed(html)
    if parser.lang != "ko":
        errors.append("The customer HTML must identify its Korean language.")
    if len(parser.ids) != len(set(parser.ids)):
        errors.append("The HTML contains duplicate element IDs.")
    for fragment in parser.fragments:
        if fragment not in parser.ids:
            errors.append(f"Missing HTML fragment: #{fragment}")
    if parser.external_assets:
        errors.append(f"Unexpected external assets: {parser.external_assets}")

    font_match = re.search(r"data:font/woff2;base64,([A-Za-z0-9+/=]+)", html)
    font = ROOT / "assets/fonts/PretendardVariable.woff2"
    if not font_match or base64.b64decode(font_match.group(1)) != font.read_bytes():
        errors.append("The embedded font does not match the bundled font.")
    if "SIL OPEN FONT LICENSE Version 1.1" not in html:
        errors.append("The generated guide is missing the embedded font license.")

    required = [
        "README.md", "README.ko.md", "docs/en/guide.md", "docs/ko/guide.md",
        "docs/en/maintenance.md", "docs/ko/maintenance.md",
        "THIRD_PARTY_NOTICES.md", "assets/fonts/OFL.txt",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required document: {relative}")

    ko_guide, en_guide = ROOT / "docs/ko/guide.md", ROOT / "docs/en/guide.md"
    if ko_guide.is_file() and en_guide.is_file():
        ko_rows, en_rows = guide_rows(ko_guide), guide_rows(en_guide)
        if not ko_rows or ko_rows != en_rows:
            errors.append("Korean and English price/retention/API table values differ.")
        md_retention = [values for label, values in ko_rows if " · " in label]
        html_retention = [[numeric_cell(cell) for cell in row[1:]] for row in parser.retention_rows[1:]]
        if len(md_retention) != 4 or md_retention != html_retention:
            errors.append("Markdown retention values differ from the customer HTML.")

    markdown_files = list(ROOT.rglob("*.md"))
    for path in markdown_files:
        for href in local_markdown_links(path):
            parsed = urlparse(href)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f"Broken local link in {path.relative_to(ROOT)}: {href}")

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix not in (".md", ".py", ".html", ".css", ".yml", ".txt"):
            continue
        content = path.read_text(encoding="utf-8")
        if re.search(r"/(?:Users|tmp|var/folders)/", content):
            errors.append(f"Personal filesystem path in {path.relative_to(ROOT)}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS: reproducible HTML, {len(parser.ids)} IDs, offline font, bilingual table parity, and local links.")
    print("Product accuracy and visual layout still require the documented source/browser review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
