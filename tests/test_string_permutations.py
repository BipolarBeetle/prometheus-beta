import pytest
from src.string_permutations import generate_unique_permutations

def test_generate_unique_permutations_basic():
    """Test basic string permutations"""
    result = generate_unique_permutations('abc')
    assert sorted(result) == sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    assert len(result) == 6

def test_generate_unique_permutations_with_duplicates():
    """Test permutations with duplicate characters"""
    result = generate_unique_permutations('abb')
    assert sorted(result) == sorted(['abb', 'bab', 'bba'])
    assert len(result) == 3

def test_generate_unique_permutations_single_char():
    """Test single character input"""
    result = generate_unique_permutations('a')
    assert result == ['a']

def test_generate_unique_permutations_empty_string():
    """Test empty string input"""
    result = generate_unique_permutations('')
    assert result == []

def test_generate_unique_permutations_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        generate_unique_permutations(123)
    
    with pytest.raises(TypeError):
        generate_unique_permutations(None)

def test_generate_unique_permutations_identical_duplicates():
    """Test string with multiple identical characters"""
    result = generate_unique_permutations('aaa')
    assert result == ['aaa']

def test_generate_unique_permutations_sorted_output():
    """Verify that output is sorted lexicographically"""
    result = generate_unique_permutations('cba')
    assert result == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']