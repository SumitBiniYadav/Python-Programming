import re

def match_word(text, word):
    # Using word boundaries (\b) to match the exact word at the beginning
    pattern = fr'\b{re.escape(word)}\b'
    match = re.match(pattern, text, re.IGNORECASE)
    
    if match:
        print(f'Word "{word}" found at the beginning of the string')
    else:
        print(f'Word "{word}" not found at the beginning')

# Example usage
text = "Python is a powerful programming language."
word = input("Enter the word to match: ")
match_word(text, word)