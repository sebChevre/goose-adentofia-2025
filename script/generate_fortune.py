#!/usr/bin/env python3
"""generate_fortune.py -- a small daily ritual for the modern soul.

Generates an introspective fortune from Madame Ganderella, the sassy
goose oracle, framed in ASCII art, and writes it to ``fortune.md`` in
the current directory.

If a ``fortune.md`` already exists, it is moved into the ``old/``
folder first (with a timestamp if ``old/fortune.md`` is already taken).

Usage:
    python3 generate_fortune.py
"""

from __future__ import annotations

import os
import random
import shutil
import textwrap
from datetime import datetime, timezone

# --------------------------------------------------------------------------
# The oracle's words -- introspective mood, sassy delivery
# --------------------------------------------------------------------------

FORTUNES = [
    "You keep asking the universe for signs, my dear, while the answer "
    "has been sitting in the pond behind your thoughts all along, "
    "watching you swim in circles. Tonight, look at the reflection "
    "instead of the water. Yes, it is you. No, it is not a joke. Breathe.",

    "The card shows a long, dignified neck. The reading is this: you "
    "have been holding your head very high while refusing to turn it "
    "around. Whatever you are afraid to look at from behind has been "
    "looking at you for a long time. Turn around. Gently. The oracle "
    "means it.",

    "Someone is overthinking you, and the someone is you, so the "
    "oracle is simply introducing you to yourself. The fortune: you "
    "are allowed to be unfinished. Even a goose is allowed to waddle, "
    "and this one has a doctorate in it. hmph. Be kind to the waddle.",
]

ORACLE_NAME = "M A D A M E   G A N D E R E L L A"
ORACLE_SUBTITLE = "~ the sassy goose oracle of introspection ~"
ATTRIBUTION = "- Madame Ganderella, goose oracle of the deep pond"
FOOTER = "hmph. The oracle has spoken. It is about you. All of you."

# --------------------------------------------------------------------------
# The sassy goose -- facing forward, wings akimbo, one eye not fooled
# --------------------------------------------------------------------------

GOOSE_ART = [
    "           _--.",
    "          (o  _)    hmph.",
    "           \\__/",
    "            ||",
    "            ||",
    "           /||\\",
    "   .-------'  '-------.",
    "   /   .----------.   \\",
    "  /   |            |   \\",
    " /    |            |    \\",
    "  \\   |            |   /",
    "     \\'------------'/",
    "          |    |",
    "         _|    |_",
]

# --------------------------------------------------------------------------
# Layout helpers
# --------------------------------------------------------------------------

WIDTH = 64  # inner width of the ASCII frame


def _center(text: str) -> str:
    """Center a single line within the frame width."""
    if len(text) <= WIDTH:
        return text.center(WIDTH)
    return text[: WIDTH - 1] + "~"


def _indent_block(lines: list[str], width: int = WIDTH) -> list[str]:
    """Left-pad a multi-line block uniformly so its internal grid survives.

    (Centering each row independently would misalign rows of differing
    lengths, because the art shares one common column grid.)
    """
    stripped = [line.rstrip() for line in lines]
    max_len = max(len(line) for line in stripped)
    pad = max(0, (width - max_len) // 2)
    return [" " * pad + line for line in stripped]


def _frame(inner_lines: list[str]) -> str:
    edge = "+" + "=" * WIDTH + "+"
    rows = [edge]
    for line in inner_lines:
        rows.append("|" + line.ljust(WIDTH)[:WIDTH] + "|")
    rows.append(edge)
    return "\n".join(rows)


def _wrap_fortune(text: str) -> list[str]:
    lines = textwrap.fill(text, width=54).splitlines()
    lines[0] = '" ' + lines[0]
    lines[-1] += ' "'
    return lines


def build_document(fortune_text: str, stamp: str) -> str:
    """Assemble the full markdown document (title, fortune, divider, goose)."""
    inner: list[str] = [
        _center(ORACLE_NAME),
        _center(ORACLE_SUBTITLE),
        "",
        *_indent_block(_wrap_fortune(fortune_text)),
        "",
        _center(ATTRIBUTION),
        "",
        _center("*~" * (WIDTH // 2)),
        "",
        *_indent_block(GOOSE_ART),
        "",
        _center(FOOTER),
    ]
    framed = _frame(inner)
    return (
        "# Fortune from Madame Ganderella\n"
        "\n"
        f"*{stamp}*\n"
        "\n"
        "```text\n"
        f"{framed}\n"
        "```\n"
    )


# --------------------------------------------------------------------------
# File management
# --------------------------------------------------------------------------


def archive_existing(path: str, file_stamp: str) -> str | None:
    """Move an existing fortune.md into ./old/. Returns destination or None."""
    if not os.path.exists(path):
        return None
    old_dir = os.path.join(os.path.dirname(path) or ".", "old")
    os.makedirs(old_dir, exist_ok=True)
    dest = os.path.join(old_dir, "fortune.md")
    if os.path.exists(dest):
        dest = os.path.join(old_dir, f"fortune_{file_stamp}.md")
    shutil.move(path, dest)
    return dest


def main() -> None:
    now = datetime.now(timezone.utc)
    stamp = now.strftime("%Y-%m-%d %H:%M UTC")
    file_stamp = now.strftime("%Y%m%d_%H%M%S")

    fortune = random.choice(FORTUNES)
    document = build_document(fortune, stamp)

    out_path = os.path.join(os.getcwd(), "fortune.md")
    archived = archive_existing(out_path, file_stamp)

    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(document)

    print(document)
    print(f"Wrote {out_path}")
    if archived:
        print(f"Previous fortune archived to {archived}")


if __name__ == "__main__":
    main()
