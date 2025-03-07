from typing import Iterable, Callable, Any
from tqdm import tqdm

def log_with_progress_bar(
    items: Iterable, 
    process_func: Callable[[Any], Any], 
    description: str = "Processing", 
    disable_progress: bool = False
) -> list:
    """
    Process an iterable with a dynamically updating progress bar.

    Args:
        items (Iterable): Collection of items to process
        process_func (Callable): Function to apply to each item
        description (str, optional): Description for the progress bar. Defaults to "Processing".
        disable_progress (bool, optional): Disable progress bar if True. Defaults to False.

    Returns:
        list: Processed results from applying process_func to each item

    Raises:
        TypeError: If items is not iterable or process_func is not callable
        ValueError: If description is empty
    """
    # Input validation
    if not hasattr(items, '__iter__'):
        raise TypeError("Input must be an iterable")
    
    if not callable(process_func):
        raise TypeError("process_func must be a callable function")
    
    if not description:
        raise ValueError("Description cannot be an empty string")

    # Process items with progress bar
    results = []
    try:
        for item in tqdm(items, desc=description, disable=disable_progress):
            result = process_func(item)
            results.append(result)
    except Exception as e:
        raise RuntimeError(f"Error processing items: {e}")

    return results