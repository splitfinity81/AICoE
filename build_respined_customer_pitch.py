"""Generate AI-CoE-Customer-Pitch-Respined.pptx.

5-slide customer-facing variant of the re-spined pitch.
Mirrors slides 1, 3, 5, 6, 8 of AI-CoE-Pitch-Deck-Respined.pptx.
"""

from __future__ import annotations

from build_respined_pitch_deck import (
    new_prs, s1_title, s3_moat_grid, s5_ato, s6_operating, s8_ask,
)
from pathlib import Path

OUT = Path(__file__).parent / "AI-CoE-Customer-Pitch-Respined.pptx"


def main() -> None:
    prs = new_prs()
    s1_title(prs)
    s3_moat_grid(prs)
    s5_ato(prs)
    s6_operating(prs)
    s8_ask(prs)
    prs.save(str(OUT))
    print(f"Wrote {OUT.name} with {len(prs.slides)} slides")


if __name__ == "__main__":
    main()
