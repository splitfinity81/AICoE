"""Apply a shared geometric triangle/cube accent style to every AI CoE deck.

Theme-only restyle that preserves all existing AI CoE branding (palette, logo,
canonical author title, content). Adds:

  - Title slide: a right-edge accent column of stacked navy/cyan triangles
    inspired by the reference template (geometric blue panels).
  - Every other slide: a small triangle accent in the top-right corner so the
    motif carries across the deck without disturbing existing layouts.

Run:  python apply_geometric_style.py
"""

from __future__ import annotations

import sys
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Emu, Inches

ROOT = Path(__file__).parent

# AI CoE palette (kept consistent with existing build scripts).
NAVY = RGBColor(0x0B, 0x1F, 0x3A)
BLUE = RGBColor(0x00, 0x67, 0xB8)
CYAN = RGBColor(0x50, 0xE6, 0xFF)
LIGHT_CYAN = RGBColor(0xBF, 0xEA, 0xFB)

ACCENT_TAG = "AICOE_GEO_ACCENT"  # so re-runs can detect/replace prior accents

# Decks live alongside this script.
DECKS = sorted(p.name for p in ROOT.glob("AI-CoE-*.pptx"))


def _tag(shape) -> None:
    """Tag a shape so the re-run can identify and remove prior accents."""
    shape.name = f"{ACCENT_TAG}_{shape.name}"


def _add_tri(slide, x, y, size, color, rotation: float = 0.0, alpha: int | None = None):
    s = slide.shapes.add_shape(MSO_SHAPE.RIGHT_TRIANGLE, x, y, size, size)
    s.fill.solid()
    s.fill.fore_color.rgb = color
    s.line.fill.background()
    s.shadow.inherit = False
    if rotation:
        s.rotation = rotation
    _tag(s)
    return s


def _remove_prior_accents(slide) -> None:
    spTree = slide.shapes._spTree
    for sh in list(slide.shapes):
        if sh.name.startswith(ACCENT_TAG):
            spTree.remove(sh._element)


def _add_title_accent(slide, slide_w: int, slide_h: int) -> None:
    """Vertical right-edge column: stacked navy/cyan triangles."""
    col_w = Inches(0.9)
    x0 = slide_w - col_w
    # 4 stacked triangles, alternating navy/cyan, rotated for variation.
    band_h = slide_h / 4
    palette = [(NAVY, 0.0), (CYAN, 180.0), (BLUE, 0.0), (CYAN, 90.0)]
    for i, (color, rot) in enumerate(palette):
        size = min(col_w, Emu(int(band_h * 0.85)))
        cy = int(i * band_h + (band_h - size) / 2)
        cx = int(slide_w - col_w + (col_w - size) / 2)
        _add_tri(slide, cx, cy, size, color, rotation=rot)
    # Slim navy spine along the inner edge of the column.
    spine = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, x0 - Inches(0.08), 0, Inches(0.08), slide_h
    )
    spine.fill.solid()
    spine.fill.fore_color.rgb = NAVY
    spine.line.fill.background()
    spine.shadow.inherit = False
    _tag(spine)


def _add_corner_accent(slide, slide_w: int) -> None:
    """Small triangle motif in the top-right corner for content slides."""
    size = Inches(0.35)
    margin = Inches(0.12)
    # Two overlapping triangles: navy back, cyan front.
    _add_tri(slide, slide_w - size - margin, margin, size, NAVY, rotation=90.0)
    _add_tri(
        slide,
        slide_w - int(size * 0.65) - margin,
        margin,
        int(size * 0.65),
        CYAN,
        rotation=90.0,
    )


def restyle(path: Path) -> tuple[int, int]:
    prs = Presentation(str(path))
    w, h = prs.slide_width, prs.slide_height
    title_done = 0
    corner_done = 0
    for idx, slide in enumerate(prs.slides):
        _remove_prior_accents(slide)
        if idx == 0:
            _add_title_accent(slide, w, h)
            title_done += 1
        else:
            _add_corner_accent(slide, w)
            corner_done += 1
    prs.save(str(path))
    return title_done, corner_done


def main(argv: list[str]) -> int:
    targets = argv[1:] or DECKS
    for name in targets:
        p = ROOT / name
        if not p.exists():
            print(f"SKIP (missing): {name}")
            continue
        try:
            t, c = restyle(p)
            print(f"OK   {name}  title+={t} corners+={c}")
        except Exception as e:
            print(f"FAIL {name}: {type(e).__name__}: {e}")
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
