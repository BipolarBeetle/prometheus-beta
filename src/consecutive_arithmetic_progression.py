def has_consecutive_arithmetic_progression(arr):
    """
    Determines if any three consecutive numbers in the array form an arithmetic progression.
    
    An arithmetic progression is a sequence of numbers where:
    1. The difference between consecutive terms is constant
    2. The numbers are strictly monotonic (increasing or decreasing)
    3. The progression uses consecutive array elements
    
    Args:
        arr (list): A list of positive integers
    
    Returns:
        bool: True if any three consecutive numbers form an arithmetic progression, 
              False otherwise
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the input contains non-positive integers
    
    Examples:
        >>> has_consecutive_arithmetic_progression([1, 2, 3, 4, 5])  # True (2,3,4 or 3,4,5)
        True
        >>> has_consecutive_arithmetic_progression([1, 3, 5, 7, 9])  # True (1,3,5 or 3,5,7 or 5,7,9)
        True
        >>> has_consecutive_arithmetic_progression([1, 2, 4, 8, 16])  # False
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
    
    # Check consecutive triplets
    for i in range(len(arr) - 2):
        x, y, z = arr[i], arr[i+1], arr[i+2]
        
        # Check increasing arithmetic progression
        if x < y < z:
            diff1 = y - x
            diff2 = z - y
            if diff1 == diff2 and diff1 != 0:
                return True
        
        # Check decreasing arithmetic progression
        if x > y > z:
            diff1 = x - y
            diff2 = y - z
            if diff1 == diff2 and diff1 != 0:
                return True
    
    return False