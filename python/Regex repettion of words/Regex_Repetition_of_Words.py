import re
from collections import Counter


def read_file(filename):
    """Read the content of a file and return it as a list of lines."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()


def find_words(text):
    """Find all words in the given text using a regex pattern."""
    return re.findall(r'\b\w+\b', text.lower())


def count_word_occurrences(lines, words_to_count):
    """Count occurrences of specified words in the lines."""
    word_counter = Counter()

    for line in lines:
        words = find_words(line)
        word_counter.update(word for word in words if word in words_to_count)

    return word_counter


def display_word_occurrences(word_counter):
    """Display word occurrences in order."""
    for word, count in word_counter.most_common():
        print(f'{word}: {count}')


def main():
    while True:
        filename = input("Enter the filename (or 'exit' to quit): ")

        if filename.lower() == 'exit':
            break

        try:
            words_to_count = input("Enter words to count (comma-separated): ").split(',')

            lines = read_file(filename.strip())
            word_counter = count_word_occurrences(lines, words_to_count)
            display_word_occurrences(word_counter)
        except FileNotFoundError:
            print(f"File '{filename}' not found. Please enter a valid filename.")


if __name__ == "__main__":
    main()
