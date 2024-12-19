def main():
    get_file_info("./books/frankenstein.txt")

def get_number_of_words(text):
    return len(text.split(" "))

def count_characters_occurrences(text):
    characters_occurrences = {}
    for character in text:
        character = character.lower()
        if character.isalpha():
            if character in characters_occurrences:
                characters_occurrences[character] += 1
            else:
                characters_occurrences[character] = 1
    return characters_occurrences

def get_file_info(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        num_words = get_number_of_words(file_contents)
        print(f"--- Begin report of {file_path} ---")
        print(f"{num_words} words found in the document")
        characters_occurrences = count_characters_occurrences(file_contents)
        for character, occurrences in characters_occurrences.items():
            print(f"The {character} character was found {occurrences} times")
        print(f"--- End report of {file_path} ---")


if __name__ == "__main__":
    main()