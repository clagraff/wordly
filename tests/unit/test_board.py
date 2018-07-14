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
