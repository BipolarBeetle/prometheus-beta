def max_subarray_sum(arr):
    """
    Implement Kadane's algorithm to find the maximum sum of a contiguous subarray.
    
    Args:
        arr (list): A list of integers to find the maximum subarray sum.
    
    Returns:
        int: The maximum sum of any contiguous subarray within the input array.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Examples:
        >>> max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
        >>> max_subarray_sum([1])
        1
        >>> max_subarray_sum([-1, -2, -3])
        -1
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm implementation
    max_so_far = current_max = arr[0]
    
    for num in arr[1:]:
        # Choose between extending the current subarray or starting a new one
        current_max = max(num, current_max + num)
        
        # Update the overall maximum if current maximum is larger
        max_so_far = max(max_so_far, current_max)
    
    return max_so_far