def max_subarray_sum_with_constraints(A, k, s):
    """
    Find the maximum sum of a contiguous subarray with at least k elements 
    and a sum greater than or equal to s.
    
    Args:
    A (list): Input array of integers
    k (int): Minimum number of elements in the subarray
    s (int): Minimum sum threshold for the subarray
    
    Returns:
    int: Maximum sum of a subarray meeting the constraints, 
         or -1 if no such subarray exists
    
    Raises:
    ValueError: If input parameters are invalid
    """
    # Validate input parameters
    if not isinstance(A, list):
        raise ValueError("Input A must be a list")
    if not isinstance(k, int) or k < 1:
        raise ValueError("k must be a positive integer")
    if not isinstance(s, int):
        raise ValueError("s must be an integer")
    
    # If array is too short to meet k requirement
    if len(A) < k:
        return -1
    
    # Initialize variables for sliding window approach
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    
    # Sliding window to find maximum sum subarray
    for end in range(len(A)):
        # Add current element to the window
        current_sum += A[end]
        
        # Ensure we have at least k elements
        while end - start + 1 > k and start < end:
            # If window size exceeds k, remove first element
            current_sum -= A[start]
            start += 1
        
        # Check if current window meets constraints
        if (end - start + 1 >= k) and (current_sum >= s):
            max_sum = max(max_sum, current_sum)
    
    # Return maximum sum or -1 if no valid subarray found
    return max_sum if max_sum != float('-inf') else -1