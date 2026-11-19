#!/usr/bin/env python3
"""Optional local screenshot and UI smoke test. Needs playwright + Chromium.

Uses page.set_content for self-contained local examples, no web server or network.
Not a full WCAG, screen reader, or color-contrast audit.
"""
import json
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "examples/screenshots"
OUT.mkdir(exist_ok=True)
RESULTS = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, executable_path=os.environ.get("CHROMIUM_PATH") or p.chromium.executable_path, args=["--no-sandbox"])
    for width, label in ((375, "mobile"), (768, "tablet"), (1280, "desktop")):
        page = browser.new_page(viewport={"width": width, "height": 900}, device_scale_factor=1)
        page.set_content((ROOT / "examples/revised.html").read_text(encoding="utf-8"), wait_until="load")
        page.screenshot(path=str(OUT / f"revised-{label}.png"), full_page=True)
        overflow = page.evaluate("document.documentElement.scrollWidth > window.innerWidth")
        page.keyboard.press("Tab")
        focused = page.locator(":focus")
        focused_id = focused.get_attribute("id")
        outline = focused.evaluate("el => getComputedStyle(el).outlineStyle")
        assert focused_id == "title" and outline != "none", f"keyboard focus not visible: {focused_id}, {outline}"
        page.locator("#title").fill("十二月随笔：在阴雨的街道上慢慢行走，读一本有关城市与孤独感的书")
        page.locator("#add-form button").click()
        text = page.locator("#bookmarks li").last.inner_text()
        count = page.locator("#counter").inner_text()
        status = page.locator("#feedback").inner_text()
        assert "十二月随笔" in text and count == "3 条收藏" and "刷新后不会保留" in status
        assert not overflow, f"horizontal overflow at width={width}"
        RESULTS.append({"viewport": width, "horizontal_overflow": overflow, "submit": "PASS",
                        "count": count, "keyboard_focus": "PASS", "screenshot": f"examples/screenshots/revised-{label}.png"})
        page.close()
    page = browser.new_page(viewport={"width": 1280, "height": 900}, device_scale_factor=1)
    page.set_content((ROOT / "examples/anti-pattern.html").read_text(encoding="utf-8"), wait_until="load")
    page.screenshot(path=str(OUT / "anti-pattern-desktop.png"), full_page=True)
    page.close()
    browser.close()

(OUT / "browser-smoke-results.json").write_text(json.dumps({"browser": "Chromium", "results": RESULTS,
    "limits": "No full WCAG/AT/contrast validation; local demo only."}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(RESULTS, ensure_ascii=False, indent=2))
