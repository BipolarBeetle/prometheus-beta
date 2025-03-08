def swap_case(input_string: str) -> str:
    """
    Swap the case of characters in the input string.
    
    Converts all lowercase characters to uppercase and 
    all uppercase characters to lowercase.
    
    Args:
        input_string (str): The input string to process
    
    Returns:
        str: A new string with swapped character cases
    
    Examples:
        >>> swap_case("Hello World!")
        'hELLO wORLD!'
        >>> swap_case("AbCdEf 123")
        'aBcDeF 123'
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return input_string.swapcase()