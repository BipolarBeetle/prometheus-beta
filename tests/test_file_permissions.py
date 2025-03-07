import os
import pytest
import tempfile
import stat
from src.file_permissions import change_file_permissions

def test_change_file_permissions_success():
    """Test successful file permission change."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
        
    # Set initial mode to read-only
    os.chmod(temp_path, 0o444)
    
    # Change to read-write for owner
    result = change_file_permissions(temp_path, 0o644)
    assert result is True
    
    # Verify permissions
    current_mode = stat.S_IMODE(os.stat(temp_path).st_mode)
    assert current_mode == 0o644
    
    # Clean up
    os.unlink(temp_path)

def test_change_file_permissions_nonexistent_file():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        change_file_permissions('/path/to/nonexistent/file', 0o755)

def test_change_file_permissions_invalid_mode():
    """Test handling of invalid permission modes."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    # Test mode too low
    with pytest.raises(ValueError):
        change_file_permissions(temp_path, -1)
    
    # Test mode too high
    with pytest.raises(ValueError):
        change_file_permissions(temp_path, 0o1000)
    
    # Clean up
    os.unlink(temp_path)

def test_change_file_permissions_invalid_inputs():
    """Test handling of invalid input types."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    # Test non-string file path
    with pytest.raises(TypeError):
        change_file_permissions(123, 0o755)
    
    # Test non-integer mode
    with pytest.raises(TypeError):
        change_file_permissions(temp_path, '755')
    
    # Clean up
    os.unlink(temp_path)