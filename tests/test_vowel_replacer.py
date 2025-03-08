import pytest
from src.vowel_replacer import replace_vowels

def test_replace_vowels_lowercase():
    assert replace_vowels("hello") == "hillu"
    assert replace_vowels("python") == "pythun"
    assert replace_vowels("world") == "wurld"

def test_replace_vowels_uppercase():
    assert replace_vowels("HELLO") == "HILLU"
    assert replace_vowels("PYTHON") == "PYTHUN"
    assert replace_vowels("WORLD") == "WURLD"

def test_replace_vowels_mixed_case():
    assert replace_vowels("HeLLo") == "HiLLu"
    assert replace_vowels("PyThOn") == "PyThUn"

def test_replace_vowels_all_vowels():
    assert replace_vowels("aeiou") == "eioua"
    assert replace_vowels("AEIOU") == "EIOUA"

def test_replace_vowels_no_vowels():
    assert replace_vowels("rhythm") == "rhythm"
    assert replace_vowels("123") == "123"

def test_replace_vowels_edge_cases():
    assert replace_vowels("") == ""
    assert replace_vowels(" ") == " "
    assert replace_vowels("a") == "e"
    assert replace_vowels("U") == "A"