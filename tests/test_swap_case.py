import pytest
from src.swap_case import swap_case

def test_swap_case_basic():
    """Test basic case swapping functionality"""
    assert swap_case("Hello World!") == "hELLO wORLD!"
    assert swap_case("AbCdEf") == "aBcDeF"

def test_swap_case_empty_string():
    """Test empty string input"""
    assert swap_case("") == ""

def test_swap_case_all_lowercase():
    """Test input with all lowercase characters"""
    assert swap_case("hello") == "HELLO"

def test_swap_case_all_uppercase():
    """Test input with all uppercase characters"""
    assert swap_case("WORLD") == "world"

def test_swap_case_mixed_with_numbers():
    """Test input with mixed characters and numbers"""
    assert swap_case("Hello123World") == "hELLO123wORLD"

def test_swap_case_special_characters():
    """Test input with special characters"""
    assert swap_case("Hello, World!") == "hELLO, wORLD!"

def test_swap_case_invalid_input():
    """Test invalid input type"""
    with pytest.raises(TypeError):
        swap_case(123)
    with pytest.raises(TypeError):
        swap_case(None)