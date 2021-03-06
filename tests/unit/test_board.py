"""Test placeholder until real tests are added."""
import pytest

import wordly.wordsearch as wordsearch


# Mark entire file as part of "unit" tests
pytestmark = pytest.mark.unit


class TestLine:
    """Test suite for the Line class."""
    def test__init__(self):
        """Test the line constructor correctly initializes the class."""
        index, characters = 42, "validline"
        line = wordsearch.Line(index, characters)

        assert line.index == index
        assert line.characters == characters

    def test_append_new_character(self):
        """Test that append method correctly appends provided characters."""
        index, characters = 42, "validline"
        line = wordsearch.Line(index, characters)

        line.append("a")
        line.append("b")
        line.append("c")

        assert line.characters.endswith("abc")

    @pytest.mark.parametrize(
        "value",
        [
            1337,
            42.00,
            list(),
            dict(),
            object(),
        ]
    )
    def test_raise_type_error_on_invalid_append_type(self, value):
        """Test that append method raises a TypeError on invalid arg types."""
        index, characters = 42, "validline"
        line = wordsearch.Line(index, characters)

        with pytest.raises(TypeError):
            line.append(value)

    def test_raise_value_error_on_too_many_appended_letters(self):
        """Test that a ValueError is raised if appending more than 1 letter."""
        index, characters = 42, "validline"
        line = wordsearch.Line(index, characters)

        with pytest.raises(ValueError):
            line.append("toomanyletters")

    def test_search_raises_not_implemented(self):
        """Test that search method raises NotImplemented error."""
        index, characters = 42, "validline"
        line = wordsearch.Line(index, characters)

        with pytest.raises(NotImplementedError):
            line.search("line")


class TestHorizontalLine:

    @pytest.mark.parametrize(
        "word,result",
        [
            ("this", [(0, 0), (1, 0), (2, 0), (3, 0)]),
            ("words", [(15, 0), (16, 0), (17, 0), (18, 0), (19, 0)]),
            ("has", [(8, 0), (9, 0), (10, 0)]),
        ]
    )
    def test_search(self, word, result):
        """Assert search method returns expected result for the current word."""
        index, characters = 0, "thislinehasmanywords"
        line = wordsearch.HorizontalLine(index, characters)

        assert line.search(word) == result


class TestVerticalLine:

    @pytest.mark.parametrize(
        "word,result",
        [
            ("this", [(0, 0), (0, 1), (0, 2), (0, 3)]),
            ("words", [(0, 15), (0, 16), (0, 17), (0, 18), (0, 19)]),
            ("has", [(0, 8), (0, 9), (0, 10)]),
        ]
    )
    def test_search(self, word, result):
        """Assert search method returns expected result for the current word."""
        index, characters = 0, "thislinehasmanywords"
        line = wordsearch.VerticalLine(index, characters)

        assert line.search(word) == result


class TestDiagonalEastLine:

    @pytest.mark.parametrize(
        "word,result",
        [
            ("this", [(0, 0), (1, 1), (2, 2), (3, 3)]),
            ("words", [(15, 15), (16, 16), (17, 17), (18, 18), (19, 19)]),
            ("has", [(8, 8), (9, 9), (10, 10)]),
        ]
    )
    def test_search(self, word, result):
        """Assert search method returns expected result for the current word."""
        index, characters = 0, "thislinehasmanywords"
        line = wordsearch.DiagonalEastLine(index, characters)

        assert line.search(word) == result


class TestDiagonalWestLine:

    @pytest.mark.parametrize(
        "word,result",
        [
            ("this", [(20, 0), (19, 1), (18, 2), (17, 3)]),
            ("words", [(5, 15), (4, 16), (3, 17), (2, 18), (1, 19)]),
            ("has", [(12, 8), (11, 9), (10, 10)]),
        ]
    )
    def test_search(self, word, result):
        """Assert search method returns expected result for the current word."""
        index, characters = 20, "thislinehasmanywords"
        line = wordsearch.DiagonalWestLine(index, characters)

        assert line.search(word) == result


class TestBoard_init:
    """Test suite for board __init__ method."""

    def test_missing_argument(self):
        """Test that an error is raised when initialize with no data."""
        with pytest.raises(Exception):
            board = wordsearch.Board()

    def test_not_csv(self):
        """Test that an error is raised when initializing with invalid CSV."""
        with pytest.raises(Exception):
            wordsearch.Board("this-is-not-CSV")

    def test_valid_csv(self):
        """Test no exceptions are raised when initializing with good CSV."""
        input_csv = "a,b,c,d\ne,f,g,h\ni,j,k,l\nm,n,o,p"
        board = wordsearch.Board(input_csv)

    def test_value_error_not_square(self):
        """Test that a ValueError is raised when input CSV is not a square."""
        with pytest.raises(ValueError):
            wordsearch.Board("1,2,3,4\n5,6,7,8")

    def test_value_error_on_too_many_characters(self):
        """Test ValueError raised when providing multiple chars per column."""
        with pytest.raises(ValueError):
            wordsearch.Board("too,many,chars\nper,each,col\non,this,board")

    def test_type_error_on_wrong_argument_type(self):
        """Test TypeError is raised when providing incorrect argument type."""
        with pytest.raises(TypeError):
            wordsearch.Board(1337)


class TestBoard_search:
    """Test suite for board search method."""
    test_board = wordsearch.Board("c,a,t,s\nd,o,g,s\np,i,g,s\no,w,l,s")

    def test_word_not_supplied(self):
        """Test that not providing a search word results in a TypeError."""
        with pytest.raises(TypeError):
            self.test_board.search()

    def test_not_a_string_supplied(self):
        """Test that not providing a string results in a TypeError."""
        with pytest.raises(TypeError):
            self.test_board.search(1337)

    def test_too_many_words(self):
        """Test that providing multiple words results in a ValueError."""
        with pytest.raises(ValueError):
            self.test_board.search("too many words")

    def test_missing_word(self):
        """Test that searching for a word not on board results None."""
        assert not self.test_board.search("ant")

    def test_word_too_long(self):
        """Test that searching for a word too long results in None."""
        assert not self.test_board.search("wordtoolong")

    def test_horizontal_word_on_board(self):
        """Test that searching for horizontal word returns char positions."""
        expected = [(0, 0), (1, 0), (2, 0), (3, 0)]
        assert self.test_board.search("cats") == expected

    def test_vertical_word_on_board(self):
        """Test that searching for horizontal word returns char positions."""
        expected = [(0, 0), (0, 1), (0, 2), (0, 3)]
        assert self.test_board.search("cdpo") == expected

    def test_diagonal_east_word_on_board(self):
        """Test searching for diagonal-east word returns char positions."""
        expected = [(0, 0), (1, 1), (2, 2), (3, 3)]
        assert self.test_board.search("cogs") == expected

    def test_diagonal_west_word_on_board(self):
        """Test searching for diagonal-east word returns char positions."""
        expected = [(3, 0), (2, 1), (1, 2), (0, 3)]
        assert self.test_board.search("sgio") == expected

    def test_can_find_reversed_word(self):
        """Test that searching for a reversed word returns char positions."""
        expected = [(0, 0), (1, 0), (2, 0), (3, 0)][::-1]
        assert self.test_board.search("stac") == expected

    def test_casing_doesnt_matter(self):
        """Test that searching is case-insensitive."""
        expected = [(0, 0), (1, 0), (2, 0), (3, 0)]
        assert self.test_board.search("CATS") == expected

    def test_using_large_board(self):
        """Test finding multiple words across a large board."""
        words = {
            "cats": [(10, 12), (11, 12), (12, 12), (13, 12)],
            "dogs": [(4, 3), (5, 4), (6, 5), (7, 6)],
            "pigs": [(1, 3), (1, 4), (1, 5), (1, 6)],
            "owls": [(8, 0), (7, 1), (6, 2), (5, 3)],
        }

        csv = """P,L,V,Q,I,Z,J,X,O,C,M,V,Z,Y,V
L,N,K,N,K,P,N,W,L,Z,Y,I,P,C,M
M,C,Z,Y,C,R,L,I,V,W,E,M,R,Q,I
Z,P,L,U,D,S,Y,I,F,H,C,Y,F,V,W
N,I,Z,F,B,O,N,U,V,G,V,J,V,G,Y
W,G,B,P,C,B,G,N,I,X,V,Z,E,A,T
W,S,W,D,D,M,P,S,K,J,I,Z,S,A,S
D,T,W,R,W,S,R,G,K,V,N,O,D,Q,C
V,T,B,N,X,M,A,H,S,U,B,M,M,C,T
B,I,X,G,U,J,E,R,D,Q,T,D,K,N,L
F,D,P,U,Y,Z,F,Q,P,P,V,P,D,S,L
Z,P,V,B,S,X,Q,S,V,W,F,N,V,O,D
F,W,Q,V,O,K,F,N,N,Y,C,A,T,S,X
X,C,F,C,N,A,J,I,F,D,T,E,S,L,L
I,T,F,T,R,C,J,B,X,D,B,V,K,N,Q"""

        board = wordsearch.Board(csv)
        for word, chars in words.items():
            print(word)
            assert board.search(word) == chars
