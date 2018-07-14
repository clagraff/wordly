"""Provide interface for CLI user interactions."""
import argparse


def create_parser():
    """Create and return a setup ArgumentParser."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file",
        help="CSV input file containing word search",
    )

    return parser
