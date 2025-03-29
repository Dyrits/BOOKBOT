import sys
from stats import get_word_count, get_character_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    try:
        file_path = sys.argv[1]
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
