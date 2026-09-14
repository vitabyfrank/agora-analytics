#!/usr/bin/env python3
"""Build the self-contained customer guide without network access."""

import argparse
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "index.html"


def build_html() -> str:
    return runpy.run_path(str(ROOT / "src/render.py"))["html"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="Check that index.html matches its sources."
    )
    args = parser.parse_args()
    content = build_html()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != content:
            print("index.html is out of date. Run: python3 scripts/build.py")
            return 1
        print("index.html matches its sources.")
        return 0
    OUTPUT.write_text(content, encoding="utf-8")
    print(f"Built index.html ({OUTPUT.stat().st_size:,} bytes).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
