import pytest
from src.middle_range_indices import find_middle_range_indices

def test_middle_range_indices_odd_length():
    """Test finding indices for an odd-length list"""
    lst = [1, 2, 3, 4, 5, 6, 7]
    assert find_middle_range_indices(lst, 1) == [2, 3, 4]
    assert find_middle_range_indices(lst, 2) == [1, 2, 3, 4, 5]

def test_middle_range_indices_even_length():
    """Test finding indices for an even-length list"""
    lst = [1, 2, 3, 4, 5, 6]
    assert find_middle_range_indices(lst, 1) == [2, 3]
    assert find_middle_range_indices(lst, 2) == [1, 2, 3, 4]

def test_middle_range_indices_small_range():
    """Test with range size smaller than list"""
    lst = [10, 20, 30, 40, 50]
    assert find_middle_range_indices(lst, 0) == [2]

def test_middle_range_indices_empty_list():
    """Test with an empty list"""
    assert find_middle_range_indices([], 2) == []

def test_middle_range_indices_edge_of_list():
    """Test when range reaches the edges of the list"""
    lst = [1, 2, 3, 4, 5]
    assert find_middle_range_indices(lst, 3) == [0, 1, 2, 3, 4]

def test_middle_range_indices_input_validation():
    """Test input validation"""
    with pytest.raises(TypeError):
        find_middle_range_indices("not a list", 2)
    
    with pytest.raises(TypeError):
        find_middle_range_indices([1, 2, 3], "not an int")
    
    with pytest.raises(ValueError):
        find_middle_range_indices([1, 2, 3], -1)