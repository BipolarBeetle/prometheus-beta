import os
import zipfile
import pytest
import tempfile
import shutil

from src.zip_password_protector import create_password_protected_zip

def test_zip_single_file():
    # Create a temporary file to zip
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_input:
        temp_input.write("Test content")
        input_path = temp_input.name

    # Create a temporary output zip path
    output_zip_path = tempfile.mktemp(suffix='.zip')
    
    try:
        # Create password-protected zip
        result_path = create_password_protected_zip(input_path, output_zip_path, 'password123')
        
        # Verify zip was created
        assert os.path.exists(result_path)
        
        # Try to open with correct password
        with zipfile.ZipFile(result_path, 'r') as zf:
            zf.setpassword(b'password123')
            zf.extractall(tempfile.mkdtemp())
    
    finally:
        # Clean up
        if os.path.exists(input_path):
            os.unlink(input_path)
        if os.path.exists(output_zip_path):
            os.unlink(output_zip_path)

def test_zip_directory():
    # Create a temporary directory with some files
    temp_dir = tempfile.mkdtemp()
    try:
        # Create some files in the temp directory
        with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f1:
            f1.write('Content 1')
        with open(os.path.join(temp_dir, 'file2.txt'), 'w') as f2:
            f2.write('Content 2')
        
        # Create a temporary output zip path
        output_zip_path = tempfile.mktemp(suffix='.zip')
        
        # Create password-protected zip of directory
        result_path = create_password_protected_zip(temp_dir, output_zip_path, 'strongpass')
        
        # Verify zip was created
        assert os.path.exists(result_path)
        
        # Verify contents with correct password
        with zipfile.ZipFile(result_path, 'r') as zf:
            zf.setpassword(b'strongpass')
            extract_dir = tempfile.mkdtemp()
            zf.extractall(extract_dir)
            
            # Check extracted files exist
            assert os.path.exists(os.path.join(extract_dir, 'file1.txt'))
            assert os.path.exists(os.path.join(extract_dir, 'file2.txt'))
    
    finally:
        # Clean up
        shutil.rmtree(temp_dir)
        if os.path.exists(output_zip_path):
            os.unlink(output_zip_path)

def test_invalid_input_path():
    with pytest.raises(ValueError, match="Input path"):
        create_password_protected_zip('/nonexistent/path', 'output.zip', 'password123')

def test_invalid_password():
    with pytest.raises(ValueError, match="Password"):
        with tempfile.NamedTemporaryFile(delete=False) as temp_input:
            temp_input.write(b"Test")
            create_password_protected_zip(temp_input.name, 'output.zip', '')

def test_invalid_input_types():
    with pytest.raises(TypeError):
        create_password_protected_zip(123, 'output.zip', 'password')
    with pytest.raises(TypeError):
        create_password_protected_zip('input.txt', 123, 'password')
    with pytest.raises(TypeError):
        create_password_protected_zip('input.txt', 'output.zip', 123)