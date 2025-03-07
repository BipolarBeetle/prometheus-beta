def search_string_in_file(file_path, search_string):
    """
    Search for a specific string in a file.

    Args:
        file_path (str): Path to the file to search.
        search_string (str): String to search for in the file.

    Returns:
        list: A list of line numbers (1-indexed) where the string is found.
        If the string is not found, returns an empty list.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        TypeError: If file_path or search_string are not strings.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    if not isinstance(search_string, str):
        raise TypeError("search_string must be a string")

    # Check if file exists
    try:
        with open(file_path, 'r') as file:
            # Search for the string in each line
            matching_lines = [
                line_num 
                for line_num, line in enumerate(file, 1) 
                if search_string in line
            ]
            
            return matching_lines
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist")