import pytest
from src.two_sum import find_two_sum

def test_find_two_sum_basic():
    """Test basic scenario where two numbers sum to target"""
    assert find_two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_find_two_sum_multiple_solutions():
    """Test case where multiple solutions exist - should return first found"""
    assert find_two_sum([3, 2, 4], 6) == [1, 2]

def test_find_two_sum_end_of_list():
    """Test case where solution is at the end of the list"""
    assert find_two_sum([2, 5, 5, 11], 10) == [1, 2]

def test_find_two_sum_no_solution():
    """Test case where no solution exists"""
    assert find_two_sum([1, 2, 3, 4], 10) == []

def test_find_two_sum_negative_numbers():
    """Test with negative numbers"""
    assert find_two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

def test_find_two_sum_zero_target():
    """Test with zero as the target"""
    assert find_two_sum([0, 0], 0) == [0, 1]

def test_find_two_sum_invalid_input_type():
    """Test invalid input type raises TypeError"""
    with pytest.raises(TypeError):
        find_two_sum("not a list", 10)

def test_find_two_sum_invalid_target_type():
    """Test invalid target type raises TypeError"""
    with pytest.raises(TypeError):
        find_two_sum([1, 2, 3], "not an int")

def test_find_two_sum_insufficient_list():
    """Test list with insufficient elements raises ValueError"""
    with pytest.raises(ValueError):
        find_two_sum([1], 2)

def test_find_two_sum_large_numbers():
    """Test with large numbers"""
    assert find_two_sum([1000000, 1000001, 1000002], 2000001) == [0, 1]