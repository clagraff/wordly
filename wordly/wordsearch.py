"""Package contains objects representing a wordsearch board."""


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


class Lines:
    """Manager for lines of a similar class."""

    def __init__(self, cls):
        """Initialize class instance with the provided Line class type."""
        self.cls = cls
        self.lines = {}

    def get(self, key):
        """Return the desired line instance by key; create if doesn't exist."""
        if key not in self.lines:
            self.lines[key] = self.cls(key)
        return self.lines[key]


class Board:
    """Representation of a wordsearch board."""

    def __init__(self, csv):
        """Parse CSV into current board instance."""
        if not csv:
            raise ValueError("must provide CSV text")

        if not isinstance(csv, str):
            raise TypeError("CSV argument must be a string")

        self.size = 0
        self.horizontals = Lines(HorizontalLine)
        self.verticals = Lines(VerticalLine)
        self.diagonal_easts = Lines(DiagonalEastLine)
        self.diagonal_wests = Lines(DiagonalWestLine)

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

                self.horizontals.get(row).append(char)
                self.verticals.get(column).append(char)
                self.diagonal_easts.get(column - row).append(char)
                self.diagonal_wests.get(column + row).append(char)

                column += 1
            row += 1

        if row != column:
            raise ValueError("provide word search board must be a square")

        self.size = row

    def search(self, word):
        """Return position of all characters of search term on the board."""
        if not isinstance(word, str):
            raise TypeError("must provide a string")

        if not word or len(word.split(" ")) > 1:
            raise ValueError("must provide a single word to search for")

        if len(word) > self.size:
            return None

        word = word.lower()
        all_possible_lines = [
            *self.horizontals.lines.values(),
            *self.verticals.lines.values(),
            *self.diagonal_easts.lines.values(),
            *self.diagonal_wests.lines.values(),
        ]

        for line in all_possible_lines:
            chars = line.search(word)
            if chars:
                return chars

            reversed_chars = line.search(word[::-1])
            if reversed_chars:
                return reversed_chars[::-1]

        return None
