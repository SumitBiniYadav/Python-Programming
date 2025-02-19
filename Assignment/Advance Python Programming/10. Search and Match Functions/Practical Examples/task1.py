import re

def search_word(text, word):
    # Using word boundaries (\b) to match the exact word
    pattern = fr'\b{re.escape(word)}\b'
    match = re.search(pattern, text, re.IGNORECASE)
    
    if match:
        print(f'Word "{word}" found at position {match.start()}')
    else:
        print(f'Word "{word}" not found')

# Example usage
text = "Python is a powerful programming language."
word = input("Enter the word to search: ")
search_word(text, word)