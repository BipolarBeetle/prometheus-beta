def to_alternating_case(input_string):
    """
    Convert a string to alternating case (upper and lower).
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: A string with alternating uppercase and lowercase characters.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_alternating_case("hello")
        'HeLlO'
        >>> to_alternating_case("")
        ''
        >>> to_alternating_case("a")
        'A'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty string
    if not input_string:
        return input_string
    
    # Convert to alternating case
    return ''.join(
        char.upper() if i % 2 == 0 else char.lower() 
        for i, char in enumerate(input_string)
    )