import sys

def text_statistics(text: str) -> dict:
    words = text.lower().split()
    return {
        "characters": len(text),
        "words": len(words),
        "lines": len(text.splitlines())
    }


if __name__ == "__main__":

    try:
        filename = sys.argv[1]

        with open(filename, "r") as file:
            content = file.read()

        stats = text_statistics(content)

        print(stats)
        print("Word Count:", stats["words"])
        print("Character Count:", stats["characters"])
    except FileNotFoundError:
        print("File not found.")