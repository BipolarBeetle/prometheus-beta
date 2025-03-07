def find_median(numbers):
    """
    Find the median of a list of numbers.
    
    Args:
        numbers (list): A list of numbers to find the median of.
    
    Returns:
        float: The median value of the input list.
    
    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    # Validate input 
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if len(numbers) == 0:
        raise ValueError("Cannot find median of an empty list")
    
    # Validate all elements are numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All list elements must be numeric")
    
    # Sort the list
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    
    # Calculate median
    if n % 2 == 0:
        # Even number of elements, average of two middle values
        mid_right = n // 2
        mid_left = mid_right - 1
        return (sorted_nums[mid_left] + sorted_nums[mid_right]) / 2
    else:
        # Odd number of elements, middle value
        return sorted_nums[n // 2]