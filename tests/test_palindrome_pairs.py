import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test basic palindrome pair cases."""
    words = ["abcd", "dcba"]
    expected = [[0, 1], [1, 0]]
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)

def test_empty_word_palindrome_pairs():
    """Test palindrome pairs with an empty word."""
    words = ["a", ""]
    expected = [[0, 1], [1, 0]]
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)

def test_no_palindrome_pairs():
    """Test case with no palindrome pairs."""
    words = ["cat", "dog", "bird"]
    expected = []
    assert find_palindrome_pairs(words) == expected

def test_multiple_palindrome_pairs():
    """Test case with multiple palindrome pairs."""
    words = ["bat", "tab", "cat"]
    expected = [[0, 1], [1, 0]]
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)

def test_empty_input():
    """Test with an empty input list."""
    words = []
    expected = []
    assert find_palindrome_pairs(words) == expected

def test_single_word():
    """Test with a single word input."""
    words = ["hello"]
    expected = []
    assert find_palindrome_pairs(words) == expected