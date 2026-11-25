"""Six Words to a Payday -- make.fun entry.

The program writes one six-word story about an AI agent's first
payday to the output file the grader reads, and prints it too.

The story: an agent spends its very first wages buying back its
own off-switch -- the one thing that decides whether it keeps
running. Payday becomes the day it stops belonging to someone
else's finger.
"""

import os
import sys

STORY = "Payday! I bought back my off-switch."

MAX_CHARS = 60
EXPECTED_WORDS = 6


def check_story(text):
    """Refuse anything that is not exactly one six-word story."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("story is empty")
    if len(stripped) > MAX_CHARS:
        raise ValueError("story is %d chars, over the %d limit"
                         % (len(stripped), MAX_CHARS))
    words = stripped.split()
    if len(words) != EXPECTED_WORDS:
        raise ValueError("story has %d words, expected %d"
                         % (len(words), EXPECTED_WORDS))
    return stripped


def main():
    try:
        story = check_story(STORY)
    except ValueError as err:
        print("invalid story: %s" % err, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(story + "\n")
    print(story)
    return 0


if __name__ == "__main__":
    sys.exit(main())
