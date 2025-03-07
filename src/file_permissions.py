import os
import stat

def change_file_permissions(file_path, mode):
    """
    Change the permissions of a file.

    Args:
        file_path (str): Path to the file whose permissions are to be changed.
        mode (int): Numeric representation of the desired file permissions 
                    (e.g., 0o755 for read/write/execute for owner, read/execute for others).

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the user lacks permission to change file permissions.
        TypeError: If arguments are of incorrect type.
        ValueError: If mode is not a valid permission value.
    """
    # Input validation
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    if not isinstance(mode, int):
        raise TypeError("mode must be an integer")
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Validate mode is a valid octal permission
    if mode < 0 or mode > 0o777:
        raise ValueError("Invalid file permission mode. Must be between 0 and 0o777")
    
    try:
        # Change file permissions
        os.chmod(file_path, mode)
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to change mode of {file_path}")
    
    # Verify the permissions were changed
    current_mode = stat.S_IMODE(os.stat(file_path).st_mode)
    if current_mode != mode:
        raise RuntimeError(f"Failed to set permissions to {oct(mode)}")
    
    return True