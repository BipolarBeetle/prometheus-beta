import pytest
from src.anagram_checker import are_anagrams

def test_basic_anagrams():
    """Test simple anagram scenarios"""
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("triangle", "integral") == True

def test_non_anagrams():
    """Test strings that are not anagrams"""
    assert are_anagrams("hello", "world") == False
    assert are_anagrams("python", "java") == False

def test_case_insensitivity():
    """Test case-insensitive comparison"""
    assert are_anagrams("Listen", "Silent") == True
    assert are_anagrams("Tea", "Eat") == True

def test_whitespace_handling():
    """Test anagram detection with whitespace"""
    assert are_anagrams("debit card", "bad credit") == True
    assert are_anagrams("astronomer", "moon starer") == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert are_anagrams("", "") == True

def test_different_lengths():
    """Test strings of different lengths"""
    assert are_anagrams("abc", "abcd") == False

def test_repeated_characters():
    """Test anagrams with repeated characters"""
    assert are_anagrams("aab", "aba") == True
    assert are_anagrams("aab", "baa") == True
    assert are_anagrams("aab", "abc") == False

def test_unicode_characters():
    """Test anagram detection with unicode characters"""
    assert are_anagrams("über", "rebü") == True

def test_invalid_input():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        are_anagrams(123, "test")
    with pytest.raises(TypeError):
        are_anagrams("test", [1, 2, 3])
    with pytest.raises(TypeError):
        are_anagrams(None, "test")