import re

# Function to search for a word in a string
def search_word(text, word):
    pattern = rf"\b{word}\b"  # \b ensures we match the whole word
    match = re.search(pattern, text, re.IGNORECASE)  # Case-insensitive search
    if match:
        print(f"'{word}' found at position {match.start()}")
    else:
        print(f"'{word}' not found in the text.")

# Example usage
text = "Python is a powerful programming language."
word = "powerful"
search_word(text, word)
