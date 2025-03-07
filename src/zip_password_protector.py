import os
import zipfile

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

    # Create ZIP file with password protection
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # If input is a directory, walk through and add all files
        if os.path.isdir(input_path):
            for root, _, files in os.walk(input_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, input_path)
                    with open(file_path, 'rb') as f:
                        # Write file content directly
                        zipf.writestr(arcname, f.read(), zipfile.ZIP_DEFLATED)
        # If input is a file, add it directly
        else:
            with open(input_path, 'rb') as f:
                zipf.writestr(os.path.basename(input_path), f.read(), 
                              zipfile.ZIP_DEFLATED)

    # Encrypt the entire archive with a password
    with zipfile.ZipFile(output_zip_path, 'a') as zf:
        # Set zip file to use encryption
        zf.setpassword(password.encode())
        # Encrypt the entire archive
        for zinfo in zf.filelist:
            zf.writestr(zinfo, zf.read(zinfo.filename), zipfile.ZIP_DEFLATED)

    return output_zip_path