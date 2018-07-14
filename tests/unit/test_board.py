"""Test placeholder until real tests are added."""
import pytest

import wordly.wordsearch as wordsearch


# Mark entire file as part of "unit" tests
pytestmark = pytest.mark.unit


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
        expected = [(3, 3), (2, 2), (1, 1), (0, 0)]
        assert self.test_board.search("sgio") == expected

    def test_can_find_reversed_word(self):
        """Test that searching for a reversed word returns char positions."""
        expected = [(0, 0), (1, 0), (2, 0), (3, 0)][::-1]
        assert self.test_board.search("stac") == expected

    def test_casing_doesnt_matter(self):
        """Test that searching is case-insensitive."""
        expected = [(0, 0), (1, 0), (2, 0), (3, 0)]
        assert self.test_board.search("CATS") == expected
