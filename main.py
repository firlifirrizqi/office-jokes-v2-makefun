#!/usr/bin/env python3
"""One-line office joke entry for the Make.fun 'Make the AI Judge Laugh: Office Jokes' bounty.

Writes a single original office joke (under 200 characters) to /output/entry.txt.
"""

import os

JOKE = "Our daily standup takes 45 minutes, which is why everyone sits down for it."

# Output filename the entrypoint writes inside the output directory.
OUTPUT_FILENAME = "entry.txt"

# The gate requires /output/entry.txt to be UTF-8 text of 1 to 199 characters.
assert 1 <= len(JOKE) <= 199, "joke must be under 200 characters"
# A one-line entry must be a single line: no newline characters allowed.
assert "\n" not in JOKE and "\r" not in JOKE, "joke must be a single line"


def verify_output(path: str) -> None:
    """Read the written file back and confirm it holds exactly the joke."""
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == JOKE, "entry.txt content does not match the joke"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    verify_output(path)


if __name__ == "__main__":
    main()
