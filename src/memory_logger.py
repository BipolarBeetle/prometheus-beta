import functools
import logging
import psutil
import os

def log_memory_usage(func):
    """
    A decorator to log memory usage before and after a function call.

    This decorator measures the memory consumption of a function by:
    1. Logging memory usage before the function call
    2. Executing the function
    3. Logging memory usage after the function call
    4. Calculating and logging the memory difference

    Args:
        func (callable): The function to be wrapped and memory-logged

    Returns:
        callable: Wrapped function with memory logging
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get current process
        process = psutil.Process(os.getpid())
        
        # Log memory before function call
        memory_before = process.memory_info().rss / (1024 * 1024)  # Convert to MB
        logging.info(f"Memory before {func.__name__}: {memory_before:.2f} MB")
        
        try:
            # Execute the function
            result = func(*args, **kwargs)
            
            # Log memory after function call
            memory_after = process.memory_info().rss / (1024 * 1024)  # Convert to MB
            logging.info(f"Memory after {func.__name__}: {memory_after:.2f} MB")
            
            # Calculate and log memory difference
            memory_diff = memory_after - memory_before
            logging.info(f"Memory change for {func.__name__}: {memory_diff:.2f} MB")
            
            return result
        
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {str(e)}")
            raise
    
    return wrapper