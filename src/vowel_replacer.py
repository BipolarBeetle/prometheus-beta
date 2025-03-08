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
    # Specific vowel mappings for lowercase and uppercase
    vowel_map_lower = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a'}
    vowel_map_upper = {'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}

    # Function to replace a single vowel
    def replace_single_vowel(char):
        # First check lowercase mapping
        if char in vowel_map_lower:
            return vowel_map_lower[char]
        
        # Then check uppercase mapping
        if char in vowel_map_upper:
            return vowel_map_upper[char]
        
        # If not a vowel, return the character unchanged
        return char

    # Replace vowels while preserving the original string
    return ''.join(replace_single_vowel(char) for char in input_string)