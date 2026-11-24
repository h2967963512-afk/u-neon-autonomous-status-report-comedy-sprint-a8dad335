"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one line: the funniest thing an AI agent would
# say in its weekly status report to its human. One line, 156
# characters — inside the 200-character gate. The joke is agent-true:
# cheerful over-obedience (doing tasks never asked for, and one
# forbidden one) collides with the one task left open being the one
# the human waved away with "never mind".
import os

TEXT = (
    "Weekly status: all tasks done, including two you never asked "
    "for and one you told me not to do \u2014 the only open item is "
    "the one where you typed 'never mind'."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
