import re

def reverse_word_chars(sentence: str) -> str:
    """
    Reverse the characters of each word in a given sentence while maintaining word order.
    Preserves punctuation and spacing around words.

    Args:
        sentence (str): The input sentence to process.

    Returns:
        str: A new sentence with each word's characters reversed.

    Examples:
        >>> reverse_word_chars("hello world")
        'olleh dlrow'
        >>> reverse_word_chars("")
        ''
        >>> reverse_word_chars("a b c")
        'a b c'
        >>> reverse_word_chars("hello, world!")
        'olleh, dlrow!'
    """
    # Handle empty string case
    if not sentence:
        return ""
    
    # Split the sentence into tokens (words and punctuation)
    tokens = re.findall(r'\w+|[^\w\s]|\s+', sentence)
    
    # Reverse only the words, keeping punctuation and spaces intact
    reversed_tokens = [token[::-1] if token.isalnum() else token for token in tokens]
    
    return ''.join(reversed_tokens)