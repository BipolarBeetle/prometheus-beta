def calculate_even_sum_odd_product(numbers):
    """
    Calculate the sum of even numbers and the product of odd numbers in the input array.

    Args:
        numbers (list): A list of integers to process.

    Returns:
        tuple: A tuple containing two elements:
            - The sum of all even numbers in the input list
            - The product of all odd numbers in the input list
              (1 if no odd numbers are present)

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Calculate sum of even numbers
    even_sum = sum(num for num in numbers if num % 2 == 0)
    
    # Calculate product of odd numbers
    odd_product = 1
    for num in numbers:
        if num % 2 != 0:
            odd_product *= num
    
    return even_sum, odd_product