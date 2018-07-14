"""Package contains objects representing a wordsearch board."""
from collections import defaultdict


class Line:
    """Represents a directionless character line on a word search board."""

    def __init__(self, index, characters=""):
        """Initialize instance with provided starting characters."""
        self.index = index
        self.characters = characters

    def append(self, letter):
        """Append a single character to the end of the current line."""
        self.characters += letter

    def search(self, word):
        """Abtract search method to be overridden in child classes."""
        raise NotImplementedError("this method has not been implemented.")


class HorizontalLine(Line):
    """Representation of a horizontal character line on a word search board."""

    def search(self, word):
        """Search for word in the line and return character positions."""
        characters = []

        try:
            position = self.characters.index(word)
            for offset in range(len(word)):
                characters.append((position + offset, self.index))
        except ValueError:
            pass

        return characters


class VerticalLine(Line):
    """Representation of a vertical character line on a word search board."""

    def search(self, word):
        """Search for word in the line and return character positions."""
        characters = []

        try:
            position = self.characters.index(word)
            for offset in range(len(word)):
                characters.append((self.index, position + offset))
        except ValueError:
            pass

        return characters


class DiagonalEastLine(Line):
    """Representation of diagonal east character line on word search board."""

    def search(self, word):
        """Search for word in the line and return character positions."""
        characters = []

        try:
            position = self.characters.index(word)
            for offset in range(len(word)):
                characters.append(
                    (self.index+position+offset, position+offset),
                )
        except ValueError:
            pass

        return characters


class DiagonalWestLine(Line):
    """Representation of diagonal east character line on word search board."""

    def search(self, word):
        """Search for word in the line and return character positions."""
        characters = []

        try:
            position = self.characters.index(word)
            for offset in range(len(word)):
                characters.append(
                    (self.index-position-offset, position+offset),
                )
        except ValueError:
            pass

        return characters


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

        search_methods = [
            self._search_horizontal,
            self._search_vertical,
            self._search_diagonal_east,
            self._search_diagonal_west,
        ]

        for method in search_methods:
            chars = method(word)
            if chars:
                return chars

            reversed_chars = method(word[::-1])
            if reversed_chars:
                return reversed_chars[::-1]

        return None

    def _search_horizontal(self, word):
        characters = []

        for row, line in self._horizontal.items():
            try:
                index = line.index(word)
                for offset in range(len(word)):
                    characters.append((index+offset, row))
            except ValueError:
                pass

        return characters

    def _search_vertical(self, word):
        characters = []

        for column, line in self._vertical.items():
            try:
                index = line.index(word)
                for offset in range(len(word)):
                    characters.append((column, index+offset))
            except ValueError:
                pass

        return characters

    def _search_diagonal_east(self, word):
        characters = []

        for row, line in self._diagonal_east.items():
            try:
                index = line.index(word)
                for offset in range(len(word)):
                    characters.append((index+offset+row, index+offset))
            except ValueError:
                pass

        return characters

    def _search_diagonal_west(self, word):
        characters = []

        for row, line in self._diagonal_west.items():
            try:
                index = line.index(word)
                for offset in range(len(word)):
                    characters.append(
                        (row-offset, index+offset),
                    )
            except ValueError:
                pass

        return characters
