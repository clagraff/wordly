"""Executable script for the wordly package."""
import wordly.cli


def main():
    """Entrypoint for wordly script."""
    parser = wordly.cli.create_parser()
    _ = parser.parse_args()

    return


if __name__ == "__main__":
    main()
