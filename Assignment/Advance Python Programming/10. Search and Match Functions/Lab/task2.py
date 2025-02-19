import re

# Function to match a word at the beginning of a string
def match_word(text, word):
    pattern = rf"^{word}\b"  # ^ ensures it matches at the start, \b ensures whole word match
    match = re.match(pattern, text, re.IGNORECASE)  # Case-insensitive match
    if match:
        print(f"'{word}' is at the beginning of the text.")
    else:
        print(f"'{word}' is NOT at the beginning of the text.")

# Example usage
text = "Python is a great programming language."
word = "Python"
match_word(text, word)
