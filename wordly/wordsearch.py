"""Package contains objects representing a wordsearch board."""
from collections import defaultdict


class Board:
    """Representation of a wordsearch board."""

    def __init__(self, csv):
        if not csv:
            raise ValueError("must provide CSV text")

        self._horizontal = defaultdict(str)
        self._vertical = defaultdict(str)
        self._diagonal = defaultdict(str)

        self._parse_input(csv)

    def _parse_input(self, csv):
        x, y = 0, 0
        for line in csv.split("\n"):
            x = 0

            for char in line.split(","):
                if len(char) != 1:
                    raise ValueError("only single letters allowed per column.")

                self._horizontal[y] += char
                self._vertical[x] += char
                self._diagonal[x-y] += char

                x += 1
            y += 1

        if x != y:
            raise ValueError("provide word search board must be a square")
