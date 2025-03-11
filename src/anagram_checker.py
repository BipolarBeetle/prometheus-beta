def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of another word or phrase.
    This function is case-insensitive and ignores whitespace.
    
    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    
    Raises:
        TypeError: If input is not a string
    """
    # Check for valid input
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    # Remove whitespace and convert to lowercase
    clean_str1 = ''.join(str1.lower().split())
    clean_str2 = ''.join(str2.lower().split())
    
    # Check if lengths are different
    if len(clean_str1) != len(clean_str2):
        return False
    
    # Use character counting to check for anagrams
    char_count = {}
    
    # Count characters in first string
    for char in clean_str1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Subtract characters from second string
    for char in clean_str2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    return True