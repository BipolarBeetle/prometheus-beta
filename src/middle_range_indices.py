def find_middle_range_indices(sorted_list, range_size):
    """
    Find indices of elements within a given range of the middle value in a sorted list.

    Args:
        sorted_list (list): A sorted list of integers 
        range_size (int): Number of indices to return on each side of the middle value

    Returns:
        list: Indices of elements within the specified range of the middle value

    Raises:
        ValueError: If the input list is empty or range_size is negative
        TypeError: If inputs are not of the correct type
    """
    # Validate inputs
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(range_size, int):
        raise TypeError("Range size must be an integer")
    
    if range_size < 0:
        raise ValueError("Range size cannot be negative")
    
    # Handle empty list
    if not sorted_list:
        return []
    
    # Calculate the middle index 
    # For odd-length lists, use integer division to get the center
    # For even-length lists, use the lower middle index
    mid_index = len(sorted_list) // 2
    
    # Calculate start and end indices for the range
    start_index = max(0, mid_index - range_size)
    end_index = min(len(sorted_list), mid_index + range_size + 1)
    
    # Return the indices within the specified range
    return list(range(start_index, end_index))