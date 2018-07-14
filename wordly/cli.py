"""Provide interface for CLI user interactions."""
import argparse


def create_parser():
    """Create and return a setup ArgumentParser."""
    parser = argparse.ArgumentParser(
        "wordly",
        description="Find and display the character positions of words hidden "
                    "within a word search grid."
    )

    parser.add_argument(
        "csv",
        help="CSV input file containing word search",
        type=argparse.FileType('r'),
    )

    return parser
