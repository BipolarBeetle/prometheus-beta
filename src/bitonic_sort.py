def bitonic_sort(arr, ascending=True):
    """
    Implement the Bitonic Sort algorithm.
    
    Bitonic sort is a comparison-based sorting algorithm that can be run in parallel.
    It works by first creating a bitonic sequence and then merging it.
    
    Args:
        arr (list): The input list to be sorted
        ascending (bool, optional): Whether to sort in ascending order. Defaults to True.
    
    Returns:
        list: The sorted list
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains elements that cannot be compared
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Empty or single element list is already sorted
    if len(arr) <= 1:
        return arr.copy()
    
    def compare_and_swap(arr, i, j, direction):
        """
        Compare and swap elements if they are in the wrong order.
        
        Args:
            arr (list): The list to modify
            i (int): First index to compare
            j (int): Second index to compare
            direction (bool): Sort direction (True for ascending, False for descending)
        """
        if (direction and arr[i] > arr[j]) or (not direction and arr[i] < arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
    
    def bitonic_merge(arr, low, count, direction):
        """
        Merge a bitonic sequence in given direction.
        
        Args:
            arr (list): The list to merge
            low (int): Starting index of the sequence
            count (int): Number of elements in the sequence
            direction (bool): Sort direction
        """
        if count > 1:
            k = count // 2
            for i in range(low, low + k):
                compare_and_swap(arr, i, i + k, direction)
            
            bitonic_merge(arr, low, k, direction)
            bitonic_merge(arr, low + k, k, direction)
    
    def bitonic_sort_recursive(arr, low, count, direction):
        """
        Recursively sort a bitonic sequence.
        
        Args:
            arr (list): The list to sort
            low (int): Starting index of the sequence
            count (int): Number of elements in the sequence
            direction (bool): Sort direction
        """
        if count > 1:
            k = count // 2
            
            # Sort first half in ascending order
            bitonic_sort_recursive(arr, low, k, True)
            
            # Sort second half in descending order
            bitonic_sort_recursive(arr, low + k, k, False)
            
            # Merge entire sequence in the given direction
            bitonic_merge(arr, low, count, direction)
    
    # Create a copy to avoid modifying the original list
    result = arr.copy()
    
    # Perform bitonic sort
    bitonic_sort_recursive(result, 0, len(result), ascending)
    
    return result