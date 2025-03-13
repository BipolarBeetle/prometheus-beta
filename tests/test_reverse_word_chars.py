import pytest
from src.reverse_word_chars import reverse_word_chars

def test_reverse_word_chars_basic():
    """Test basic word character reversal."""
    assert reverse_word_chars("hello world") == "olleh dlrow"

def test_reverse_word_chars_empty_string():
    """Test handling of empty string."""
    assert reverse_word_chars("") == ""

def test_reverse_word_chars_single_word():
    """Test reversal of a single word."""
    assert reverse_word_chars("python") == "nohtyp"

def test_reverse_word_chars_multiple_words():
    """Test reversal of multiple words."""
    assert reverse_word_chars("code is fun") == "edoc si nuf"

def test_reverse_word_chars_mixed_case():
    """Test reversal with mixed case words."""
    assert reverse_word_chars("Hello World") == "olleH dlroW"

def test_reverse_word_chars_with_punctuation():
    """Test reversal with punctuation."""
    assert reverse_word_chars("hello, world!") == "olleh, dlrow!"

def test_reverse_word_chars_single_char_words():
    """Test reversal with single character words."""
    assert reverse_word_chars("a b c") == "a b c"