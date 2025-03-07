class FontLogger:
    """
    A utility class for logging output with different font sizes.
    
    Supports logging messages with predefined font size levels.
    """
    
    # Font size levels
    SMALL = 'small'
    NORMAL = 'normal'
    LARGE = 'large'
    EXTRA_LARGE = 'extra_large'
    
    @classmethod
    def log(cls, message, size=NORMAL):
        """
        Log a message with a specified font size.
        
        Args:
            message (str): The message to log
            size (str, optional): Font size of the log message. 
                                  Defaults to NORMAL.
        
        Raises:
            ValueError: If an invalid font size is provided
            TypeError: If message is not a string
        """
        # Validate input types
        if not isinstance(message, str):
            raise TypeError("Message must be a string")
        
        # Validate font size
        valid_sizes = [cls.SMALL, cls.NORMAL, cls.LARGE, cls.EXTRA_LARGE]
        if size not in valid_sizes:
            raise ValueError(f"Invalid font size. Must be one of {valid_sizes}")
        
        # Simulate logging with font size
        size_prefix = {
            cls.SMALL: "[SMALL] ",
            cls.NORMAL: "[NORMAL] ",
            cls.LARGE: "[LARGE] ",
            cls.EXTRA_LARGE: "[EXTRA LARGE] "
        }
        
        print(f"{size_prefix[size]}{message}")
        
        return f"{size_prefix[size]}{message}"