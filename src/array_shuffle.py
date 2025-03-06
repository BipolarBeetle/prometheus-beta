import random
from typing import List, TypeVar

T = TypeVar('T')

def shuffle_array(arr: List[T]) -> List[T]:
    """
    Shuffle the elements of an input array randomly.

    This function creates a new shuffled list using the Fisher-Yates (Knuth) shuffle algorithm,
    which provides an unbiased and uniform random permutation of the input array.

    Args:
        arr (List[T]): The input array to be shuffled.

    Returns:
        List[T]: A new list with the elements of the input array randomly shuffled.

    Raises:
        TypeError: If the input is not a list.
    
    Examples:
        >>> shuffle_array([1, 2, 3, 4, 5])  # Returns a random permutation
        >>> shuffle_array([])  # Returns an empty list
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the input list to avoid modifying the original
    shuffled = arr.copy()
    
    # If the list is empty or has only one element, return it as is
    if len(shuffled) <= 1:
        return shuffled
    
    # Fisher-Yates (Knuth) shuffle algorithm
    for i in range(len(shuffled) - 1, 0, -1):
        # Generate a random index between 0 and i (inclusive)
        j = random.randint(0, i)
        
        # Swap elements
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    
    return shuffled