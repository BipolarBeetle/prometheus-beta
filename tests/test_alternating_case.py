import pytest
from src.alternating_case import to_alternating_case

def test_basic_alternating_case():
    """Test basic string conversion to alternating case."""
    assert to_alternating_case("hello") == "HeLlO"
    assert to_alternating_case("world") == "WoRlD"

def test_empty_string():
    """Test empty string handling."""
    assert to_alternating_case("") == ""

def test_single_character():
    """Test single character conversion."""
    assert to_alternating_case("a") == "A"
    assert to_alternating_case("B") == "B"

def test_mixed_case_input():
    """Test input with mixed case."""
    assert to_alternating_case("hElLo") == "HeLlO"

def test_special_characters():
    """Test handling of special characters and spaces."""
    assert to_alternating_case("hello world!") == "HeLlO WoRlD!"
    assert to_alternating_case("123 abc") == "123 AbC"

def test_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        to_alternating_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_case(None)
    
    with pytest.raises(TypeError):
        to_alternating_case(["hello"])