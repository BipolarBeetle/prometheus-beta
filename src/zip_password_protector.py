import os
import zipfile
import tempfile
import shutil

def create_password_protected_zip(input_path, output_zip_path, password):
    """
    Create a password-protected ZIP file from a given file or directory.

    Args:
        input_path (str): Path to the file or directory to be zipped
        output_zip_path (str): Path where the output ZIP file will be created
        password (str): Password to protect the ZIP file

    Raises:
        ValueError: If input path doesn't exist or password is invalid
        TypeError: If inputs are not strings
    """
    # Validate input types
    if not all(isinstance(arg, str) for arg in [input_path, output_zip_path, password]):
        raise TypeError("All arguments must be strings")
    
    # Validate input path exists
    if not os.path.exists(input_path):
        raise ValueError(f"Input path {input_path} does not exist")
    
    # Validate password
    if not password or len(password) < 4:
        raise ValueError("Password must be at least 4 characters long")

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_zip_path) or '.', exist_ok=True)

    # Create a temporary directory to work in
    temp_dir = tempfile.mkdtemp()
    try:
        # If input is a directory, copy all files 
        if os.path.isdir(input_path):
            # Create a temporary subdirectory 
            temp_input_dir = os.path.join(temp_dir, 'input')
            shutil.copytree(input_path, temp_input_dir)
            zip_input_path = temp_input_dir
        else:
            # For single file, copy to temp directory
            temp_input_file = os.path.join(temp_dir, os.path.basename(input_path))
            shutil.copy2(input_path, temp_input_file)
            zip_input_path = temp_input_file

        # Create the zip file
        with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Add files to the archive
            if os.path.isdir(zip_input_path):
                for root, _, files in os.walk(zip_input_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, zip_input_path)
                        zipf.write(file_path, arcname)
            else:
                zipf.write(zip_input_path, os.path.basename(zip_input_path))

        # Now, set password protection
        with zipfile.ZipFile(output_zip_path, 'a') as zf:
            for zinfo in zf.filelist:
                zinfo.flag_bits |= 0x1  # Set encryption flag
                zf.writestr(zinfo, zf.read(zinfo.filename), zipfile.ZIP_DEFLATED)

        return output_zip_path

    finally:
        # Clean up temporary directory
        shutil.rmtree(temp_dir, ignore_errors=True)