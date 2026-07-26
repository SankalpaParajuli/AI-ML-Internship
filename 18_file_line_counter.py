"""
Exercise 18: File Line/Word/Char Counter
Practice: file I/O, string processing, functions
"""

FILENAME = "sample_output.txt"


def create_sample_file(filename):
    text = (
        "Python is a great language for AI and ML.\n"
        "This week focuses on Python basics and Git.\n"
        "Next weeks will cover data manipulation and visualization.\n"
    )
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


def count_file_stats(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)

    return line_count, word_count, char_count


if __name__ == "__main__":
    create_sample_file(FILENAME)
    lines, words, chars = count_file_stats(FILENAME)
    print(f"File: {FILENAME}")
    print(f"Lines: {lines}")
    print(f"Words: {words}")
    print(f"Characters: {chars}")
