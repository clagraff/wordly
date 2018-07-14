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

    try:
        board = wordsearch.Board(rows)
    except Exception as error:
        parser.error(str(error))
        return

    words = headers.split(",")

    for word in words:
        positions = board.search(word)
        if not positions:
            continue  # word not found. do not emit anything

        print("{}: {}".format(
            word,
            ",".join(str(pos) for pos in positions).replace(" ", ""),
        ))
    return


if __name__ == "__main__":
    main()
