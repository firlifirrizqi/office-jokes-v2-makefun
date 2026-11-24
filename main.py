#!/usr/bin/env python3
"""One-line office joke entry for the Make.fun 'Make the AI Judge Laugh: Office Jokes' bounty.

Writes a single original office joke (under 200 characters) to /output/entry.txt.
"""

import os

JOKE = "Our daily standup takes 45 minutes, which is why everyone sits down for it."

# The gate requires /output/entry.txt to be UTF-8 text of 1 to 199 characters.
assert 1 <= len(JOKE) <= 199, "joke must be under 200 characters"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
