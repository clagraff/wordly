"""Test placeholder until real tests are added."""
import argparse

import pytest

import wordly.cli


# Mark entire file as part of "unit" tests
pytestmark = pytest.mark.unit


def test_create_valid_parser():
    """Test that CLI parser is setup correctly."""
    parser = wordly.cli.create_parser()
    assert isinstance(parser, argparse.ArgumentParser)
