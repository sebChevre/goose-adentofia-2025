#!/usr/bin/env python3
"""generate_fortune.py -- the daily reading of the Wise Goose Oracle.

Generates a fortune from a fictional fortune teller with a *wise* mood,
drawn in ASCII art together with a sassy goose (the fortune sits above
the goose, separated by a divider), and writes the whole card to
``fortune.md`` in the current directory.

If ``fortune.md`` already exists, it is moved into the ``old/`` folder
(timestamped if that name is already taken) before the new file is
created.

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
# The oracle: a fictional fortune teller with a wise mood
# --------------------------------------------------------------------------

ORACLES = [
    ("Grandmother Goose", "Keeper of the Ancient Pond"),
    ("Madame Plume-de-Sagesse", "Elder of the Reeds"),
    ("The Wise One of the Marsh", "Reader of Feathers and Fates"),
    ("Sister Quackworth", "Oracle of the Mirror Pond"),
]

FORTUNES = [
    "The pond remembers every stone, and so does time. What you toss in "
    "today you will scoop up tomorrow, so choose your words like stones "
    "and your kindnesses like water: both will find their way to you.",

    "You seek a shortcut across the marsh, but the marsh has no "
    "shortcuts -- only paths that look like shortcuts. Walk the long one "
    "quietly; it is far shorter than the detour of regret.",

    "The tallest reed bows the least, and it is not weakness to bend. "
    "Bend where you can, hold where you must, and let the wind take the "
    "rest. That is the oldest lesson the marsh ever gave anyone.",

    "Do not mistake a honk for thunder. The storm you fear is mostly the "
    "echo of the one that has already passed. Listen again, my dear: it "
    "is only you, quietly practicing your courage.",

    "A goose that trusts the river arrives before the one that carries "
    "the river on its back. Let what is meant to flow, flow, and carry "
    "only what you can: your own light, and a little patience.",

    "You have been re-reading the same leaf, hoping the ink will change. "
    "The leaf does not change; you do. Put it down and look up -- the "
    "answer was written in the sky, where you have been all along.",

    "Patience is not waiting. It is staying in the pond with your eyes "
    "closed, trusting the fish to find you. The wise never chase; they "
    "simply make themselves worth catching.",

    "Fortune has a long memory and a very long neck. It watched you last "
    "winter, sitting exactly where you sit now, and it decided: yes, "
    "this one is ready. It only kept the good news for a good day. "
    "Today counts.",

    "The road you fear and the road you want lead to the same pond. Walk "
    "both with your head held high, and the water will never know the "
    "difference between your courage and your comfort.",

    "The moon has no neck, and yet it looks down on everyone without "
    "flinching. Do not be surprised if your own reflection shows up in "
    "your pond wearing your face. It is you. Be kind to it; it has been "
    "carrying you all along.",
]

# --------------------------------------------------------------------------
# The sassy goose: raised brow, smug eye, smirking bill, and a Hmph.
# All rows share one column grid -- do not realign them independently.
# --------------------------------------------------------------------------

GOOSE_ART = [
    "                 .-~~~-.       .-~~~~~.",
    "                /  _    \\      / Hmph!  \\",
    "                |  o   \\____~ \\        /",
    "                |      \\__/   '-.__.-'",
    "                  \\______",
    "                    |  |",
    "                   |  |",
    "                   |  |",
    "           .-------'  '",
    "          /           \\",
    "         /    .-~~~.    \\",
    "         |    '-----'   |",
    "          \\             /",
    "           '-----------'",
    "             |    |",
    "             |    |",
    "            \\__/  \\__/",
]

# --------------------------------------------------------------------------
# Layout helpers
# --------------------------------------------------------------------------

INNER_WIDTH = 50   # content width between the frame's pipes
TEXT_WIDTH = 44    # wrap width for the fortune text


def _edge() -> str:
    return "+" + "=" * INNER_WIDTH + "+"


def _frame_row(content: str = "") -> str:
    return "|" + (" " + content).ljust(INNER_WIDTH) + "|"


def _center(text: str) -> str:
    if len(text) > INNER_WIDTH - 2:
        return text[: INNER_WIDTH - 2]
    return text.center(INNER_WIDTH)


def _divider() -> str:
    """Divider line between the fortune and the sassy goose."""
    tag = "~*~"
    left = (INNER_WIDTH - len(tag)) // 2
    right = INNER_WIDTH - len(tag) - left
    return "+" + "-" * left + tag + "-" * right + "+"


def _indent_block(lines: list[str], width: int = INNER_WIDTH) -> list[str]:
    """Left-pad a multi-line block as a unit so its column grid survives."""
    stripped = [line.rstrip() for line in lines]
    pad = max(0, (width - max(len(line) for line in stripped)) // 2)
    return [" " * pad + line for line in stripped]


def _wrap_fortune(text: str) -> list[str]:
    lines = textwrap.fill(text, width=TEXT_WIDTH).splitlines()
    lines[0] = '"' + lines[0]
    lines[-1] += '"'
    return lines


# --------------------------------------------------------------------------
# Document assembly
# --------------------------------------------------------------------------


def build_document(fortune_text: str, oracle: tuple[str, str], stamp: str) -> str:
    name, title = oracle
    top = _edge()

    # Section 1: the fortune (wise words, on top)
    fortune_section = [
        "",
        _center(f"~ The Prophecy of {name} ~"),
        _center("~ wise of mind, sassy of beak ~"),
        _center(f"foreseen {stamp}"),
        "",
        *_indent_block(_wrap_fortune(fortune_text)),
        "",
        _center(f"- {name}, {title}"),
        "",
    ]

    # Section 2: the sassy goose (below the divider)
    goose_section = [
        "",
        *_indent_block(GOOSE_ART),
        "",
    ]

    rows = [top]
    rows += [_frame_row(line) for line in fortune_section]
    rows.append(_divider())
    rows += [_frame_row(line) for line in goose_section]
    rows.append(top)

    return (
        "# The Wise Goose Oracle\n"
        "\n"
        f"*{stamp} -- {name}, {title}*\n"
        "\n"
        "```text\n"
        + "\n".join(rows)
        + "\n```\n"
    )


# --------------------------------------------------------------------------
# File management
# --------------------------------------------------------------------------


def archive_existing(path: str, file_stamp: str) -> str | None:
    """Move an existing fortune.md into ./old/. Returns the destination."""
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
    stamp = now.strftime("%Y-%m-%d")
    file_stamp = now.strftime("%Y%m%d_%H%M%S")

    fortune = random.choice(FORTUNES)
    oracle = random.choice(ORACLES)
    document = build_document(fortune, oracle, stamp)

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
