def find_two_sum(nums, target):
    """
    Find two indices in the given array that add up to the target sum.

    Args:
        nums (list): A list of integers to search through
        target (int): The target sum to find

    Returns:
        list: A list containing two indices where the corresponding 
              values add up to the target sum, or an empty list if 
              no such indices exist

    Time Complexity: O(n)
    Space Complexity: O(n)

    Raises:
        TypeError: If input is not a list or if target is not an integer
        ValueError: If input list is too short
    """
    # Validate input types
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Check if list has enough elements
    if len(nums) < 2:
        raise ValueError("Input list must contain at least two elements")

    # Use a dictionary to store complement values
    complement_dict = {}
    
    # Iterate through the list
    for i, num in enumerate(nums):
        # Check if the current number's complement exists in the dictionary
        complement = target - num
        if complement in complement_dict:
            # Return the indices of the two numbers that sum to target
            return [complement_dict[complement], i]
        
        # Store the current number and its index
        complement_dict[num] = i
    
    # If no solution is found, return an empty list
    return []