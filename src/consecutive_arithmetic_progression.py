def has_consecutive_arithmetic_progression(arr):
    """
    Determines if exactly three consecutive numbers in the array form an arithmetic progression.
    
    An arithmetic progression requires:
    1. Constant difference between exactly three consecutive terms
    2. Strictly monotonic (increasing or decreasing)
    3. No other arithmetic progressions can be formed
    
    Args:
        arr (list): A list of positive integers
    
    Returns:
        bool: True if exactly three consecutive numbers form an arithmetic progression, 
              False otherwise
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the input contains non-positive integers
    
    Examples:
        >>> has_consecutive_arithmetic_progression([3, 4, 5, 6, 7])  # True
        True
        >>> has_consecutive_arithmetic_progression([1, 3, 5, 7, 9])  # False, not consecutive
        False
        >>> has_consecutive_arithmetic_progression([1, 2, 4, 8, 16])  # False, unequal differences
        False
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for minimum length
    if len(arr) < 3:
        return False
    
    # Validate input contains only positive integers
    if not all(isinstance(x, int) and x > 0 for x in arr):
        raise ValueError("All elements must be positive integers")
    
    # Count total progressions
    progression_count = 0
    for i in range(len(arr) - 2):
        x, y, z = arr[i], arr[i+1], arr[i+2]
        
        # Two checks: increasing and decreasing
        is_increasing_prog = (x < y < z) and (y - x == z - y)
        is_decreasing_prog = (x > y > z) and (x - y == y - z)
        
        # Count valid progressions
        if is_increasing_prog or is_decreasing_prog:
            progression_count += 1
    
    # Must be exactly one progression
    return progression_count == 1