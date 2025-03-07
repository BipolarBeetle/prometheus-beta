import os
import pytest
from src.file_search import search_string_in_file

def test_basic_string_search(tmp_path):
    # Create a temporary file for testing
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello world\nThis is a test\nHello again")
    
    # Search for existing string
    result = search_string_in_file(str(test_file), "Hello")
    assert result == [1, 3], "Should find 'Hello' on lines 1 and 3"

def test_case_sensitive_search(tmp_path):
    # Create a temporary file for testing
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello world\nhello again")
    
    # Search for case-sensitive string
    result = search_string_in_file(str(test_file), "Hello")
    assert result == [1], "Should find only exact case match"

def test_no_match(tmp_path):
    # Create a temporary file for testing
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Some text\nAnother line")
    
    # Search for non-existing string
    result = search_string_in_file(str(test_file), "NotFound")
    assert result == [], "Should return empty list when no match"

def test_file_not_found():
    # Test when file does not exist
    with pytest.raises(FileNotFoundError):
        search_string_in_file("non_existent_file.txt", "test")

def test_invalid_input_types():
    # Test invalid input types
    with pytest.raises(TypeError):
        search_string_in_file(123, "test")
    
    with pytest.raises(TypeError):
        search_string_in_file("file.txt", 123)

def test_empty_file(tmp_path):
    # Create an empty file
    test_file = tmp_path / "empty_file.txt"
    test_file.write_text("")
    
    # Search in empty file
    result = search_string_in_file(str(test_file), "test")
    assert result == [], "Should return empty list for empty file"