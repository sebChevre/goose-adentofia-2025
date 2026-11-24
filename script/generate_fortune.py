#!/usr/bin/env python3
"""
generate_fortune.py
===================

Consults Madame Plume the Wise, a sassy goose and self-appointed
Oracle of the Willow Pond.  Today her mood is *wise*: she has peered
into the pond, seen a great deal, and intends to tell you only what
you can take.

The result is an ASCII fortune card -- border, wise prophecy,
divider, and the sassy goose herself -- written to ``fortune.md`` in
the current directory.  If a ``fortune.md`` already exists it is
archived into the ``./old`` folder before the new one is written.

Usage:
    python3 generate_fortune.py
"""

from __future__ import annotations

import datetime
import os
import random
import shutil

# ---------------------------------------------------------------------------
# The oracle and her prophecies
# ---------------------------------------------------------------------------

TELLER_NAME = "Madame Plume the Wise"
TELLER_TITLE = "Oracle of the Willow Pond"
MOOD = "wise"

FORTUNES: tuple[str, ...] = (
    "A great journey begins with the first step -- or, in your case, the "
    "forty-seventh. Do not be discouraged: even geese waddle.",
    "The one you seek is already seeking you. Do not expect them to honk "
    "first; in matters of the heart, patience always honks last.",
    "Fortune favours the bold, but wisdom favours the calm. Be bold in "
    "your plans, calm in your heart, and the pond will part for you.",
    "You will find what you have lost under the very thing you are least "
    "likely to look. Yes, the cushion. Yes, really. I never lie -- I "
    "merely round things down.",
    "A storm of paper and deadlines approaches. Weather it with dry quills "
    "and a drier sense of humour; you have survived every storm before "
    "this one, and that one is entirely on you.",
    "Wealth will come to you the way a goose approaches a pond: slowly, "
    "confidently, and with no intention of ever leaving.",
    "Within the week someone will flatter you. Trust the content of their "
    "praise; do not trust their motives.",
    "The path you fear most is the one that leads to your growth. Walk it "
    "with your head high and your wings folded.",
    "Do not mourn the sunken bread. The river provides for those who know "
    "how to wait -- and, on the rare occasion, how to steal.",
    "An old friend will send word of themselves. Reply promptly; their "
    "patience is thinner than a swan's neck, and they are, in fact, a "
    "swan. Mind that.",
    "Wisdom is not knowing every answer, but knowing which questions are "
    "worth a honk. Ask better questions this week.",
    "What you refuse to forgive will stick to you like a duck at a buffet: "
    "awkward, persistent, and impossible to ignore. Let it go.",
)

# ---------------------------------------------------------------------------
# The sassy goose, rendered in glorious ASCII
# ---------------------------------------------------------------------------

GOOSE_ART: tuple[str, ...] = (
    '                    .--------.          "Honk.',
    '                   / ##  ##  \\          Mind your',
    '                    |  .--.  |          step."',
    "                    \\  '--'  /",
    "                     '------'",
    "                     |      |",
    "                     |      |",
    "        .------------'      '------------.",
    "        |                                  |",
    "        |                ,--.              |",
    "        |               (    )             |",
    "        |                '--'              |",
    "        |                                  |",
    "        '----------------------------------'",
    "                   |  |    |  |",
    "                   |  |    |  |",
    "                  _|  |    |  |_",
    "                 (______) (______)",
)

CARD_WIDTH = 56


# ---------------------------------------------------------------------------
# Card construction helpers
# ---------------------------------------------------------------------------

def _wrap(text: str, width: int) -> list[str]:
    """Word-wrap *text* to *width* columns."""
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        if current and len(current) + 1 + len(word) > width:
            lines.append(current)
            current = word
        else:
            current = f"{current} {word}".strip()
    if current:
        lines.append(current)
    return lines


def _center_block(lines: list[str], width: int) -> list[str]:
    """Center a block of lines within *width* columns."""
    max_w = max(len(line) for line in lines)
    offset = max(0, (width - max_w) // 2)
    return [" " * offset + line.center(max_w) for line in lines]


def build_card(width: int = CARD_WIDTH) -> str:
    """Compose the full ASCII fortune card (border included)."""
    fortune = random.choice(FORTUNES)

    inner: list[str] = []
    inner.append("")
    inner += _center_block(
        [
            "***  THE ORACLE OF THE WILLOW POND  ***",
            f"a fortune of {TELLER_NAME}",
            f"(mood: {MOOD}; attitude: sassy, as always)",
        ],
        width,
    )
    inner.append("")

    quoted = _wrap(fortune, 44)
    quoted[0] = '"' + quoted[0]
    quoted[-1] = quoted[-1] + '"'
    inner += _center_block(quoted, width)
    inner.append("")

    rule = "=" * (width - 8)
    inner += _center_block(
        [rule, "~ the sassy goose, with honks, approaches ~", rule],
        width,
    )
    inner.append("")
    inner += _center_block(list(GOOSE_ART), width)
    inner.append("")
    inner += _center_block(["*~*~*  honked with full confidence  *~*~*"], width)
    inner.append("")

    top = "+" + "=" * (width + 2) + "+"
    body = [f"| {line.ljust(width)} |" for line in inner]
    return "\n".join([top, *body, top])


# ---------------------------------------------------------------------------
# Persistence
# ---------------------------------------------------------------------------

def _archive_existing(out_path: str, cwd: str) -> None:
    """Move an existing fortune.md into ./old, never clobbering an archive."""
    old_dir = os.path.join(cwd, "old")
    os.makedirs(old_dir, exist_ok=True)

    archive = os.path.join(old_dir, "fortune.md")
    if os.path.exists(archive):
        stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        archive = os.path.join(old_dir, f"fortune_{stamp}.md")
        counter = 1
        while os.path.exists(archive):
            archive = os.path.join(old_dir, f"fortune_{stamp}_{counter}.md")
            counter += 1

    shutil.move(out_path, archive)
    print(f"Archived previous fortune -> {os.path.relpath(archive, cwd)}")


def main() -> None:
    cwd = os.getcwd()
    out_path = os.path.join(cwd, "fortune.md")

    if os.path.exists(out_path):
        _archive_existing(out_path, cwd)

    now = datetime.datetime.now()
    card = build_card()
    markdown = (
        "# 🦢 Today's Fortune\n"
        "\n"
        f"> *Drawn up by {TELLER_NAME}, {TELLER_TITLE.lower()} -- mood: **{MOOD}***\n"
        "\n"
        "```\n"
        f"{card}\n"
        "```\n"
        "\n"
        f"_Honked on {now:%Y-%m-%d %H:%M} -- the goose finds this binding._\n"
    )

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(markdown)

    print(card)
    print(f"\nFortune saved to: {out_path}")


if __name__ == "__main__":
    main()
