def reverse_word_chars(sentence: str) -> str:
    """
    Reverse the characters of each word in a given sentence while maintaining word order.

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
    """
    # Handle empty string case
    if not sentence:
        return ""
    
    # Split the sentence into words, reverse chars of each word, then join back
    return " ".join(word[::-1] for word in sentence.split())