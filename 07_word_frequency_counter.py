"""
Exercise 07: Word Frequency Counter
Practice: dictionaries, string methods, loops
Very relevant for NLP prep later this internship!
"""


def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        # strip basic punctuation
        word = word.strip(".,!?;:\"'")
        if word == "":
            continue
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


if __name__ == "__main__":
    sample_text = (
        "Python is great. Python is fun. "
        "Learning Python for AI and ML is a great step."
    )
    result = word_frequency(sample_text)

    print("Text:", sample_text)
    print("\nWord frequencies:")
    for word, count in sorted(result.items(), key=lambda x: x[1], reverse=True):
        print(f"  {word}: {count}")
