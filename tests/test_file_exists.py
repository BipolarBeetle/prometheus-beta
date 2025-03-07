import os
import pytest
import tempfile

from src.file_exists import check_file_exists

def test_existing_file():
    """Test that check_file_exists returns True for an existing file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        try:
            assert check_file_exists(temp_file.name) == True
        finally:
            os.unlink(temp_file.name)

def test_non_existing_file():
    """Test that check_file_exists returns False for a non-existing file."""
    non_existent_file = os.path.join(tempfile.gettempdir(), 'this_file_does_not_exist_xyz.txt')
    assert check_file_exists(non_existent_file) == False

def test_directory():
    """Test that check_file_exists returns False for a directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert check_file_exists(temp_dir) == False

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="File path must be a string"):
        check_file_exists(123)
        check_file_exists(None)
        check_file_exists(['file.txt'])

def test_relative_path():
    """Test that check_file_exists works with relative paths."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        try:
            # Get the absolute path and compute relative path
            abs_path = temp_file.name
            rel_path = os.path.relpath(abs_path)
            assert check_file_exists(rel_path) == True
        finally:
            os.unlink(temp_file.name)

def test_path_normalization():
    """Test that check_file_exists normalizes paths correctly."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        try:
            # Create paths with different separators and extra dots
            abs_path = temp_file.name
            paths_to_test = [
                abs_path,
                os.path.normpath(abs_path),
                os.path.join(os.path.dirname(abs_path), '.', os.path.basename(abs_path))
            ]
            
            for path in paths_to_test:
                assert check_file_exists(path) == True
        finally:
            os.unlink(temp_file.name)