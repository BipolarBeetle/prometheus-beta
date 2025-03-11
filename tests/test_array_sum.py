import pytest
from src.array_sum import calculate_array_sum

def test_calculate_array_sum_positive_integers():
    """Test sum of positive integers"""
    assert calculate_array_sum([1, 2, 3, 4, 5]) == 15

def test_calculate_array_sum_mixed_numbers():
    """Test sum of mixed positive and negative numbers"""
    assert calculate_array_sum([-1, 0, 1, 2.5]) == 2.5

def test_calculate_array_sum_empty_list():
    """Test sum of an empty list"""
    assert calculate_array_sum([]) == 0

def test_calculate_array_sum_single_element():
    """Test sum of a single element list"""
    assert calculate_array_sum([42]) == 42

def test_calculate_array_sum_floating_point():
    """Test sum of floating point numbers"""
    assert calculate_array_sum([1.1, 2.2, 3.3]) == pytest.approx(6.6)

def test_calculate_array_sum_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_array_sum("not a list")

def test_calculate_array_sum_non_numeric_elements():
    """Test raising TypeError for non-numeric elements"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_array_sum([1, 2, "three", 4])