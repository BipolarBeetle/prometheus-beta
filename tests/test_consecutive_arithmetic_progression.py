import pytest
from src.consecutive_arithmetic_progression import has_consecutive_arithmetic_progression

def test_basic_arithmetic_progression():
    """Test basic arithmetic progression cases"""
    assert has_consecutive_arithmetic_progression([3, 4, 5, 6, 7]) == True
    assert has_consecutive_arithmetic_progression([5, 4, 3, 2, 1]) == True

def test_no_arithmetic_progression():
    """Test cases with no arithmetic progression"""
    # Exponential or unequal progression
    assert has_consecutive_arithmetic_progression([1, 2, 4, 8, 16]) == False
    
    # Irregular intervals
    assert has_consecutive_arithmetic_progression([2, 4, 6, 9, 12]) == False
    
    # Multiple progressions or non-consecutive
    assert has_consecutive_arithmetic_progression([1, 3, 5, 7, 9]) == False
    assert has_consecutive_arithmetic_progression([1, 3, 5, 2, 4]) == False
    assert has_consecutive_arithmetic_progression([1, 2, 3, 4, 5]) == False

def test_edge_cases():
    """Test edge cases"""
    # Less than 3 elements
    assert has_consecutive_arithmetic_progression([1, 2]) == False
    assert has_consecutive_arithmetic_progression([]) == False
    
    # Exact 3 elements - valid cases
    assert has_consecutive_arithmetic_progression([1, 2, 3]) == True
    assert has_consecutive_arithmetic_progression([3, 2, 1]) == True
    
    # Invalid 3-element cases
    assert has_consecutive_arithmetic_progression([1, 3, 2]) == False
    assert has_consecutive_arithmetic_progression([2, 3, 5]) == False

def test_error_handling():
    """Test error cases"""
    # Non-list input
    with pytest.raises(TypeError):
        has_consecutive_arithmetic_progression("not a list")
    
    # Non-positive integers
    with pytest.raises(ValueError):
        has_consecutive_arithmetic_progression([1, 2, -3])
    with pytest.raises(ValueError):
        has_consecutive_arithmetic_progression([0, 1, 2])
    
    # Mixed non-integer types
    with pytest.raises(ValueError):
        has_consecutive_arithmetic_progression([1, 2, "3"])

def test_multiple_progressions():
    """Test arrays with multiple progressions"""
    # More challenging cases
    assert has_consecutive_arithmetic_progression([7, 5, 3, 1]) == True
    
    # Multiple or non-consecutive progressions should fail
    assert has_consecutive_arithmetic_progression([7, 5, 3, 1, 2, 4]) == False
    assert has_consecutive_arithmetic_progression([1, 3, 5, 2, 4]) == False
    assert has_consecutive_arithmetic_progression([1, 2, 3, 4, 5]) == False