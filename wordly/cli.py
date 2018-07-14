"""Provide interface for CLI user interactions."""
import argparse


def create_parser():
    """Create and return a setup ArgumentParser."""
    parser = argparse.ArgumentParser(
        "wordly",
        description="wordly can solve word searches provided in the form of "
                    "a CSV input file."
    )

    parser.add_argument(
        "file",
        help="CSV input file containing word search",
    )

    return parser
