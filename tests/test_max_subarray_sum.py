import pytest
from src.max_subarray_sum import max_subarray_sum

def test_standard_array():
    """Test with a standard array containing positive and negative numbers."""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_positive():
    """Test an array with all positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_all_negative():
    """Test an array with all negative numbers."""
    assert max_subarray_sum([-1, -2, -3, -4, -5]) == -1

def test_single_element():
    """Test an array with a single element."""
    assert max_subarray_sum([42]) == 42

def test_mixed_numbers():
    """Test an array with mixed positive and negative numbers."""
    assert max_subarray_sum([-1, 2, 3, -2, 5]) == 8

def test_zero_sum():
    """Test an array where the max sum is zero."""
    assert max_subarray_sum([-1, -1, 0, -1, -1]) == 0

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError):
        max_subarray_sum("not a list")

def test_empty_list():
    """Test that a ValueError is raised for an empty list."""
    with pytest.raises(ValueError):
        max_subarray_sum([])