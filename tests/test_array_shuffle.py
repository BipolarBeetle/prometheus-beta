import pytest
import random
from src.array_shuffle import shuffle_array

def test_shuffle_basic_list():
    """Test shuffling a basic list of integers."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Check that the shuffled list contains the same elements
    assert sorted(shuffled) == sorted(original)
    
    # Check that the list is not in the original order (unlikely to be exactly the same)
    assert shuffled != original

def test_shuffle_empty_list():
    """Test shuffling an empty list."""
    assert shuffle_array([]) == []

def test_shuffle_single_element_list():
    """Test shuffling a list with a single element."""
    single_elem = [42]
    assert shuffle_array(single_elem) == single_elem

def test_shuffle_different_types():
    """Test shuffling a list with different types of elements."""
    mixed_list = [1, 'a', True, 3.14, None]
    shuffled = shuffle_array(mixed_list)
    
    # Check that the shuffled list contains the same elements by counting
    assert len(shuffled) == len(mixed_list)
    for item in mixed_list:
        assert shuffled.count(item) == mixed_list.count(item)
    
    # Check that the list is not in the original order
    assert shuffled != mixed_list

def test_shuffle_randomness():
    """Test that multiple shuffles produce different orders."""
    original = list(range(10))
    
    # Generate multiple shuffles
    shuffles = [shuffle_array(original) for _ in range(20)]
    
    # Check that at least some shuffles are different from the original
    # This is probabilistic, but extremely unlikely to fail
    assert any(shuffle != original for shuffle in shuffles)

def test_shuffle_preserves_original():
    """Ensure the original list is not modified."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    assert original == [1, 2, 3, 4, 5]  # Original list should remain unchanged

def test_invalid_input():
    """Test that TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError):
        shuffle_array("not a list")
    
    with pytest.raises(TypeError):
        shuffle_array(123)
    
    with pytest.raises(TypeError):
        shuffle_array(None)