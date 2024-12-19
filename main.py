def main():
    try:
        file_path = "./books/frankenstein.txt"
        text = read_file(file_path)
        generate_report(file_path, text)
    except FileNotFoundError:
        print(f"Error: File not found.")
    except Exception as error:
        print(f"An error occurred: {str(error)}")


def read_file(file_path):
    """Read and return the contents of a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def get_word_count(text):
    """Count words in text, handling multiple spaces and line breaks."""
    words = text.split()
    return len(words)


def get_character_count(text):
    """Count occurrences of alphabetic characters in text."""
    char_count = { }
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return dict(sorted(char_count.items()))  # Sort alphabetically


def print_report_header(file_path):
    """Print the report header."""
    print(f"\n--- Begin report of {file_path} ---")


def print_report_footer(file_path):
    """Print the report footer."""
    print(f"--- End report of {file_path} ---\n")


def print_character_statistics(char_count):
    """Print character occurrence statistics."""
    for char, count in char_count.items():
        print(f"The '{char}' character was found {count:,} times")


def generate_report(file_path, text):
    """Generate and print the complete text analysis report."""
    print_report_header(file_path)

    word_count = get_word_count(text)
    print(f"{word_count:,} words found in the document\n")

    char_count = get_character_count(text)
    print_character_statistics(char_count)

    print_report_footer(file_path)


if __name__ == "__main__":
    main()
