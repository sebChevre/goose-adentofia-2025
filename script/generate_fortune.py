#!/usr/bin/env python3
"""
generate_fortune.py
===================

Consults Madame Plume the Wise, a sassy goose and self-appointed
Oracle of the Willow Pond.  Her mood today is *wise*: she has peered
into the pond, seen a great deal, and intends to tell you only what
you can take (plus one parting jab).

The result is an ASCII fortune card:

    +==============================================+
    |            the wise fortune                 |
    |   -----------------------------------------  |
    |            the sassy goose, honking          |
    +==============================================+

with the fortune above the goose, a divider between them, and an
ASCII border around the whole thing.  The card is written to
``fortune.md`` in the current directory.  If a ``fortune.md``
already exists, it is first moved into the ``./old`` folder.

Usage:
    python3 script/generate_fortune.py
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
    "A river never argues with the stone; it simply goes around it. "
    "Do the same this week, with grace, and with a little drama.",
    "The answer you seek is already in your hands. You have simply not "
    "yet stopped honking long enough to look.",
    "Patience is not waiting. It is the art of honking while the soup "
    "is still cooking.",
    "You will be offered a choice that seems small. It is not. Weigh "
    "it carefully, or it will weigh you.",
    "Trust the quiet ones. The loudest swimmers make the least splash.",
    "Someone who seems far away is quietly rooting for you. They have "
    "merely not yet mastered the art of the wave.",
    "You will lose something small before the next moon. The universe "
    "is making room for something you cannot yet imagine.",
    "Do what is kind before you do what is impressive. In the end, "
    "it will also be impressive.",
    "Wisdom is not knowing every answer. It is knowing which questions "
    "are worth a honk. Ask better questions this week.",
    "A door you almost walked past will open for you. Do not be late; "
    "it is holding your schedule, not its own.",
)

# ---------------------------------------------------------------------------
# The sassy goose, rendered in glorious ASCII.
# Winked eye, raised wing, one leg lifted: sass in all four directions.
# ---------------------------------------------------------------------------

GOOSE_ART = r"""                      .----.
                      |    |
        .----.        |  . |
       / o  - \       |  | |
       \   ^  /       |  . |
        '.__'         |  | |
         | |          '----'
          /          \
         /            \
        /              \
        \              /
         \            /
          _____________
              |   |
              |   \
              v"""

GOOSE_LINES: list[str] = [line.rstrip() for line in GOOSE_ART.splitlines()]
GOOSE_CAPTION = "~ head tilted, one wing up, deeply unimpressed ~"

CARD_WIDTH = 60  # inner width of the card, between the | | borders


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
    """Center a block of lines within *width* columns (aligned as a block)."""
    max_w = max(len(line) for line in lines)
    offset = max(0, (width - max_w) // 2)
    return [" " * offset + line.ljust(max_w) for line in lines]


def build_card(fortune: str) -> str:
    """Compose the full ASCII fortune card (border included)."""
    rule = "-" * (CARD_WIDTH - 12)

    inner: list[str] = []
    inner.append("")
    inner += _center_block(
        [
            "***  THE ORACLE OF THE WILLOW POND  ***",
            f"a fortune from {TELLER_NAME}",
            f"(mood: {MOOD}; sass: 100%, as always)",
        ],
        CARD_WIDTH,
    )
    inner.append("")

    quoted = _wrap(fortune, 50)
    quoted[0] = '"' + quoted[0]
    quoted[-1] = quoted[-1] + '"'
    inner += _center_block(quoted, CARD_WIDTH)
    inner.append("")

    # divider between the fortune (above) and the goose (below)
    inner += _center_block([rule], CARD_WIDTH)
    inner.append("")

    inner += _center_block(GOOSE_LINES, CARD_WIDTH)
    inner.append("")
    inner += _center_block([GOOSE_CAPTION], CARD_WIDTH)
    inner.append("")

    inner += _center_block([rule], CARD_WIDTH)
    inner.append("")
    inner += _center_block(
        [
            f"-- divined by {TELLER_NAME}, {TELLER_TITLE}",
            "honked with full confidence, to be read before noon",
        ],
        CARD_WIDTH,
    )
    inner.append("")

    top = "+" + "=" * (CARD_WIDTH + 2) + "+"
    body = [f"| {line.ljust(CARD_WIDTH)} |" for line in inner]
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

    fortune = random.choice(FORTUNES)
    card = build_card(fortune)
    now = datetime.datetime.now()
    markdown = (
        "# \U0001f9a2 Today's Fortune\n"
        "\n"
        f"> *Drawn up by {TELLER_NAME}, {TELLER_TITLE} -- mood: **{MOOD}***\n"
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
