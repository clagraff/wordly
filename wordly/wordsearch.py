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

        self._size = 0

        self._horizontal = defaultdict(str)
        self._vertical = defaultdict(str)
        self._diagonal_east = defaultdict(str)
        self._diagonal_west = defaultdict(str)

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

                char = char.lower()

                self._horizontal[row] += char
                self._vertical[column] += char
                self._diagonal_east[column - row] += char
                self._diagonal_west[column + row] += char

                column += 1
            row += 1

        if row != column:
            raise ValueError("provide word search board must be a square")

        self._size = row

    def search(self, word):
        """Return position of all characters of search term on the board."""
        if not isinstance(word, str):
            raise TypeError("must provide a string")

        if not word or len(word.split(" ")) > 1:
            raise ValueError("must provide a single word to search for")

        if len(word) > self._size:
            return None

        word = word.lower()
        characters = []

        for row, line in self._horizontal.items():
            try:
                index = line.index(word)
                for offset in range(len(word)):
                    characters.append((row, index+offset))
            except ValueError:
                pass

        return characters