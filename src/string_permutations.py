def generate_unique_permutations(s: str) -> list[str]:
    """
    Generate all possible unique permutations of a given string.
    
    Args:
        s (str): Input string to generate permutations for
    
    Returns:
        list[str]: A list of unique permutations of the input string
    
    Raises:
        TypeError: If input is not a string
    """
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not s:
        return []
    
    # Convert to list of characters for easier manipulation
    chars = list(s)
    
    # Use a set to ensure uniqueness
    unique_permutations = set()
    
    def backtrack(start: int):
        """
        Recursive backtracking to generate permutations
        
        Args:
            start (int): Starting index for permutation generation
        """
        # If we've reached the end of the list, we have a complete permutation
        if start == len(chars):
            unique_permutations.add(''.join(chars))
            return
        
        # Try swapping current character with each subsequent character
        for i in range(start, len(chars)):
            # Swap characters
            chars[start], chars[i] = chars[i], chars[start]
            
            # Recursively generate permutations for the rest of the string
            backtrack(start + 1)
            
            # Backtrack (undo the swap)
            chars[start], chars[i] = chars[i], chars[start]
    
    # Start the backtracking process
    backtrack(0)
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_permutations))