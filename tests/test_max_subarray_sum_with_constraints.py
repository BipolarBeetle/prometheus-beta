import pytest
from src.max_subarray_sum_with_constraints import max_subarray_sum_with_constraints

def test_basic_case():
    """Test a basic scenario where a valid subarray exists"""
    A = [1, 2, 3, 4, 5]
    k = 2
    s = 7
    assert max_subarray_sum_with_constraints(A, k, s) == 9

def test_no_valid_subarray():
    """Test when no subarray meets the constraints"""
    A = [1, 2, 3, 4, 5]
    k = 3
    s = 20
    assert max_subarray_sum_with_constraints(A, k, s) == -1

def test_exact_k_elements():
    """Test when exactly k elements meet the constraints"""
    A = [1, 2, 3, 4, 5]
    k = 3
    s = 6
    assert max_subarray_sum_with_constraints(A, k, s) == 12

def test_multiple_valid_subarrays():
    """Test when multiple subarrays meet the constraints"""
    A = [2, 3, 4, 5, 6, 7]
    k = 2
    s = 10
    assert max_subarray_sum_with_constraints(A, k, s) == 18

def test_negative_numbers():
    """Test with negative numbers in the array"""
    A = [-1, -2, 3, 4, -5, 6, 7]
    k = 3
    s = 5
    assert max_subarray_sum_with_constraints(A, k, s) == 10

def test_single_element_array():
    """Test with a single element array"""
    A = [5]
    k = 1
    s = 5
    assert max_subarray_sum_with_constraints(A, k, s) == 5

def test_array_shorter_than_k():
    """Test when array is shorter than required k"""
    A = [1, 2]
    k = 3
    s = 5
    assert max_subarray_sum_with_constraints(A, k, s) == -1

def test_invalid_input_types():
    """Test invalid input types"""
    with pytest.raises(ValueError):
        max_subarray_sum_with_constraints("not a list", 2, 5)
    
    with pytest.raises(ValueError):
        max_subarray_sum_with_constraints([1, 2, 3], "not an int", 5)
    
    with pytest.raises(ValueError):
        max_subarray_sum_with_constraints([1, 2, 3], 2, "not an int")

def test_invalid_k_value():
    """Test invalid k value"""
    with pytest.raises(ValueError):
        max_subarray_sum_with_constraints([1, 2, 3], 0, 5)
    
    with pytest.raises(ValueError):
        max_subarray_sum_with_constraints([1, 2, 3], -1, 5)