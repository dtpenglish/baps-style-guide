#!/usr/bin/env python
"""Build the BAPS SAP Style Guide as a single PDF.

Workflow:
1. Run `mkdocs build` so mkdocs-print-site-plugin produces the
   consolidated page at site/print_page/index.html.
2. Inject our print stylesheet into that page.
3. Launch Chromium via Playwright and print the page to PDF.

Output: site/pdf/baps-style-guide.pdf

First-time setup on a fresh machine:
    pip install -r requirements.txt
    python -m playwright install chromium

Run from the project root:
    python build-pdf.py
"""

from __future__ import annotations

import asyncio
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"
PRINT_PAGE = SITE / "print_page" / "index.html"
PRINT_CSS = ROOT / "resources" / "print.css"
OUTPUT = SITE / "pdf" / "baps-style-guide.pdf"


def build_site() -> None:
    print("[1/3] Building site (mkdocs build) ...")
    subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--clean"],
        cwd=ROOT,
        check=True,
    )


def inject_print_css() -> None:
    """Copy print.css into the site and link it from the print page."""
    print("[2/3] Injecting print stylesheet ...")
    if not PRINT_PAGE.exists():
        raise SystemExit(
            f"Print page not found at {PRINT_PAGE}. "
            "Is mkdocs-print-site-plugin installed and enabled in mkdocs.yml?"
        )

    # Copy print.css into the built site so file:// URLs can resolve it.
    dest_css = SITE / "assets" / "stylesheets" / "print-pdf.css"
    dest_css.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(PRINT_CSS, dest_css)

    # Inject the <link> into the print page's <head>.
    html = PRINT_PAGE.read_text(encoding="utf-8")
    link_tag = '<link rel="stylesheet" href="../assets/stylesheets/print-pdf.css">'
    if link_tag not in html:
        html = html.replace("</head>", f"  {link_tag}\n</head>", 1)
        PRINT_PAGE.write_text(html, encoding="utf-8")


async def render_pdf() -> None:
    print(f"[3/3] Rendering PDF -> {OUTPUT.relative_to(ROOT)} ...")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    from playwright.async_api import async_playwright  # imported here so the
    # script gives a friendly error if Playwright isn't installed.

    file_url = "file:///" + PRINT_PAGE.resolve().as_posix()

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(file_url, wait_until="networkidle", timeout=120_000)
        # Wait an extra moment for any client-side rendering (Mermaid).
        await page.wait_for_timeout(2_500)
        await page.emulate_media(media="print")
        await page.pdf(
            path=str(OUTPUT),
            format="A4",
            margin={
                "top": "25mm",
                "bottom": "22mm",
                "left": "22mm",
                "right": "22mm",
            },
            print_background=True,
            display_header_footer=False,
            prefer_css_page_size=True,
        )
        await browser.close()

    size_mb = OUTPUT.stat().st_size / 1024 / 1024
    print(f"\n[OK] Wrote {OUTPUT.relative_to(ROOT)} ({size_mb:.1f} MB)")


def main() -> None:
    build_site()
    inject_print_css()
    asyncio.run(render_pdf())


if __name__ == "__main__":
    main()
