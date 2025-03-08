import pytest
from src.odd_sum_fibonacci import generate_odd_sum_fibonacci

def test_generate_odd_sum_fibonacci_basic():
    """Test basic functionality of the sequence generator."""
    result = generate_odd_sum_fibonacci(5)
    assert result == [0, 1, 1, 2, 3], "First 5 terms should match the expected sequence"

def test_generate_odd_sum_fibonacci_odd_sum_check():
    """Verify that the sum of any two consecutive terms is always odd."""
    for n in range(2, 10):  # Test for sequences of different lengths
        sequence = generate_odd_sum_fibonacci(n)
        for i in range(1, len(sequence)):
            consecutive_sum = sequence[i-1] + sequence[i]
            assert consecutive_sum % 2 == 1, \
                f"Sum of {sequence[i-1]} and {sequence[i]} should be odd, but is {consecutive_sum}"

def test_generate_odd_sum_fibonacci_edge_cases():
    """Test edge cases for the sequence generator."""
    # Test zero terms
    assert generate_odd_sum_fibonacci(0) == [], "Zero terms should return empty list"
    
    # Test single term
    assert generate_odd_sum_fibonacci(1) == [0], "First term should be 0"
    
    # Test two terms
    assert generate_odd_sum_fibonacci(2) == [0, 1], "First two terms should be 0 and 1"

def test_generate_odd_sum_fibonacci_error_handling():
    """Test error handling for invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="Number of terms must be non-negative"):
        generate_odd_sum_fibonacci(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_odd_sum_fibonacci(3.5)
    
    with pytest.raises(TypeError):
        generate_odd_sum_fibonacci("5")

def test_generate_odd_sum_fibonacci_longer_sequence():
    """Test a longer sequence to ensure consistent behavior."""
    result = generate_odd_sum_fibonacci(10)
    assert len(result) == 10, "Should generate exactly 10 terms"
    
    # Verify the odd sum property for the entire sequence
    for i in range(1, len(result)):
        assert (result[i-1] + result[i]) % 2 == 1, \
            f"Sum of {result[i-1]} and {result[i]} should be odd"