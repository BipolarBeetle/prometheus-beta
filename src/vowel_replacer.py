def replace_vowels(input_string):
    """
    Replace each vowel in the input string with the next vowel in the alphabet, 
    preserving the original case.

    Args:
        input_string (str): The input string to process.

    Returns:
        str: A new string with vowels replaced by the next vowel in the alphabet.

    Examples:
        >>> replace_vowels("hello")
        "holle"
        >>> replace_vowels("AEIOU")
        "EIOUA"
        >>> replace_vowels("Python")
        "Pythen"
    """
    # Define vowel sequences (both lowercase and uppercase)
    vowel_sequence_lower = 'aeiou'
    vowel_sequence_upper = 'AEIOU'

    # Function to replace a single vowel
    def replace_single_vowel(char):
        # Check lowercase vowels
        if char in vowel_sequence_lower:
            index = vowel_sequence_lower.index(char)
            return vowel_sequence_lower[(index + 1) % len(vowel_sequence_lower)]
        
        # Check uppercase vowels
        if char in vowel_sequence_upper:
            index = vowel_sequence_upper.index(char)
            return vowel_sequence_upper[(index + 1) % len(vowel_sequence_upper)]
        
        # If not a vowel, return the character unchanged
        return char

    # Replace vowels while preserving the original string
    return ''.join(replace_single_vowel(char) for char in input_string)