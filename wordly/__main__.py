"""Executable script for the wordly package."""
import wordly.cli as cli
import wordly.wordsearch as wordsearch


def main():
    """Entrypoint for wordly script."""
    parser = cli.create_parser()
    namespace = parser.parse_args()

    content = namespace.csv.read()

    headers, *rows = content.strip().split("\n")
    rows = "\n".join(rows)

    # Create board; exit on error.
    try:
        board = wordsearch.Board(rows)
    except Exception as error:  # pylint: disable=broad-except
        parser.error(str(error))
        return

    words = headers.split(",")

    # try to find and output each word.
    for word in words:
        positions = board.search(word)
        if not positions:
            continue  # word not found. do not emit anything.

        # format in same style as the Pillar example output.
        print("{}: {}".format(
            word,
            ",".join(str(pos) for pos in positions).replace(" ", ""),
        ))


if __name__ == "__main__":
    main()
