def has_consecutive_arithmetic_progression(arr):
    """
    Determines if any three consecutive numbers in the array form an arithmetic progression.
    
    An arithmetic progression is a sequence of numbers where the difference 
    between consecutive terms is constant and values are strictly monotonic.
    
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
        # Check if the differences show a consistent arithmetic progression
        first_diff = arr[i+1] - arr[i]
        second_diff = arr[i+2] - arr[i+1]
        
        # Require exact match of differences, non-zero, and strict monotonicity
        if first_diff == second_diff and first_diff != 0:
            # Additional checks to ensure true arithmetic progression
            if first_diff > 0 and arr[i] < arr[i+1] < arr[i+2]:
                return True
            if first_diff < 0 and arr[i] > arr[i+1] > arr[i+2]:
                return True
    
    return False