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
