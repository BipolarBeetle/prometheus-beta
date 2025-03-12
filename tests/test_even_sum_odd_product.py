import pytest
from src.even_sum_odd_product import calculate_even_sum_odd_product

def test_mixed_numbers():
    """Test with a mix of even and odd numbers."""
    result = calculate_even_sum_odd_product([1, 2, 3, 4, 5, 6])
    assert result == (12, 15)

def test_only_even_numbers():
    """Test with only even numbers."""
    result = calculate_even_sum_odd_product([2, 4, 6, 8])
    assert result == (20, 1)

def test_only_odd_numbers():
    """Test with only odd numbers."""
    result = calculate_even_sum_odd_product([1, 3, 5, 7])
    assert result == (0, 105)

def test_empty_list():
    """Test with an empty list."""
    result = calculate_even_sum_odd_product([])
    assert result == (0, 1)

def test_negative_numbers():
    """Test with negative numbers."""
    result = calculate_even_sum_odd_product([-1, -2, -3, -4, -5, -6])
    assert result == (-12, -15)

def test_zero_included():
    """Test with zero included."""
    result = calculate_even_sum_odd_product([0, 1, 2, 3])
    assert result == (2, 3)

def test_invalid_input_type():
    """Test with invalid input type."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        calculate_even_sum_odd_product("not a list")

def test_invalid_element_type():
    """Test with list containing non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        calculate_even_sum_odd_product([1, 2, "3", 4])