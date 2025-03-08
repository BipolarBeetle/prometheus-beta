import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    """Test basic LCS scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_no_common_subsequence():
    """Test when no common subsequence exists"""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_empty_strings():
    """Test behavior with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("ABC", "") == ""
    assert longest_common_subsequence("", "XYZ") == ""

def test_one_char_common():
    """Test when only one character is common"""
    assert longest_common_subsequence("A", "A") == "A"
    assert longest_common_subsequence("ABC", "CDE") == "C"

def test_type_errors():
    """Test type checking"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "ABC")
    with pytest.raises(TypeError):
        longest_common_subsequence("ABC", None)

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence("AbC", "aBc") == "A"
    assert longest_common_subsequence("hello", "HELLO") == ""

def test_repeated_characters():
    """Test LCS with repeated characters"""
    assert longest_common_subsequence("AAAAAA", "AAAA") == "AAAA"
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"