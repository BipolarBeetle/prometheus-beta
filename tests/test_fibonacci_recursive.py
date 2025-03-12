import pytest
from src.fibonacci_recursive import fibonacci_recursive

def test_fibonacci_base_cases():
    """Test base cases for Fibonacci sequence."""
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(2) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci numbers."""
    # Third Fibonacci number is 2 (1 + 1)
    assert fibonacci_recursive(3) == 2
    # Fourth Fibonacci number is 3 (1 + 2)
    assert fibonacci_recursive(4) == 3
    # Fifth Fibonacci number is 5 (2 + 3)
    assert fibonacci_recursive(5) == 5
    # Sixth Fibonacci number is 8 (3 + 5)
    assert fibonacci_recursive(6) == 8

def test_fibonacci_invalid_inputs():
    """Test handling of invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_recursive(0)
    
    # Test negative number
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_recursive(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_recursive(1.5)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_recursive("3")

def test_fibonacci_larger_numbers():
    """Test some larger Fibonacci numbers."""
    # 10th Fibonacci number
    assert fibonacci_recursive(10) == 55
    # 15th Fibonacci number
    assert fibonacci_recursive(15) == 610