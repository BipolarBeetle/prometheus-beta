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
    
    # Use regex to split words while preserving punctuation and spacing
    def reverse_word(match):
        word = match.group(0)
        # Check if the word contains only non-word characters (punctuation)
        if not re.search(r'\w', word):
            return word
        return word[::-1]
    
    # Use regex to find words and non-word characters, reverse words
    return re.sub(r'\S+', reverse_word, sentence)