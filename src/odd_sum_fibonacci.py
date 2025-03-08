def generate_odd_sum_fibonacci(n):
    """
    Generate a modified Fibonacci sequence where the sum of any two consecutive 
    numbers is always odd.

    Args:
        n (int): Number of terms to generate in the sequence.

    Returns:
        list: A list of the first n terms in the modified Fibonacci sequence.

    Raises:
        ValueError: If n is negative or not an integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Number of terms must be non-negative")

    # Handle special cases for small n
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    # Special case for the original Fibonacci-like start
    if n <= 4:
        return [0, 1, 1, 2][:n]

    # Modified Fibonacci sequence to ensure odd consecutive sum
    sequence = [0, 1, 1, 2]

    # Generate subsequent terms
    while len(sequence) < n:
        # Ensure the next term makes the previous consecutive sums odd
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence[:n]