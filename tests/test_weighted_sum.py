import pytest
from src.weighted_sum import compute_weighted_sum

def test_basic_weighted_sum():
    """Test basic weighted sum calculation."""
    numbers = [1, 2, 3]
    weights = [0.5, 1, 1.5]
    assert compute_weighted_sum(numbers, weights) == pytest.approx(7.0)

def test_single_element():
    """Test weighted sum with a single element."""
    numbers = [10]
    weights = [2]
    assert compute_weighted_sum(numbers, weights) == 20

def test_zero_weights():
    """Test weighted sum with some zero weights."""
    numbers = [1, 2, 3]
    weights = [0, 1, 0]
    assert compute_weighted_sum(numbers, weights) == 2

def test_negative_numbers_and_weights():
    """Test weighted sum with negative numbers and weights."""
    numbers = [-1, 2, -3]
    weights = [1, -2, 0.5]
    assert compute_weighted_sum(numbers, weights) == pytest.approx(-6.5)

def test_different_length_lists_raises_error():
    """Test that different length lists raise a ValueError."""
    with pytest.raises(ValueError, match="lists must have the same length"):
        compute_weighted_sum([1, 2], [1, 2, 3])

def test_empty_lists_raises_error():
    """Test that empty lists raise a ValueError."""
    with pytest.raises(ValueError, match="must be non-empty"):
        compute_weighted_sum([], [])

def test_non_numeric_inputs_raises_error():
    """Test that non-numeric inputs raise a TypeError."""
    with pytest.raises(TypeError, match="must be numeric"):
        compute_weighted_sum([1, 'a'], [1, 2])

def test_string_numeric_inputs():
    """Test that string numeric inputs are converted correctly."""
    numbers = ['1', '2', '3']
    weights = ['0.5', '1', '1.5']
    assert compute_weighted_sum(numbers, weights) == pytest.approx(7.0)