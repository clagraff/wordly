"""Package contains objects representing a wordsearch board."""
from collections import defaultdict


class Board:
    """Representation of a wordsearch board."""

    def __init__(self, csv):
        """Parse CSV into current board instance."""
        if not csv:
            raise ValueError("must provide CSV text")

        if not isinstance(csv, str):
            raise TypeError("CSV argument must be a string")

        self._horizontal = defaultdict(str)
        self._vertical = defaultdict(str)
        self._diagonal = defaultdict(str)

        self._parse_input(csv)

    def _parse_input(self, csv):
        row, column = 0, 0
        for line in csv.split("\n"):
            column = 0

            for char in line.split(","):
                if len(char) != 1:
                    raise ValueError("only single letters allowed per column")

                if char.isdigit():
                    raise ValueError("numbers not allowed in board")

                self._horizontal[row] += char
                self._vertical[column] += char
                self._diagonal[column - row] += char

                column += 1
            row += 1

        if row != column:
            raise ValueError("provide word search board must be a square")
