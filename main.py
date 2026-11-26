#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line funny safety warning label for every human being
to /output/entry.txt. Fully deterministic: no network, no randomness,
no time, no input. One fixed string, written verbatim.
"""

import os

ENTRY = (
    "WARNING: This human is 70% water, 20% caffeine, and 10% feelings "
    "it refuses to discuss. Do not shake. May cry at dog food commercials."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
