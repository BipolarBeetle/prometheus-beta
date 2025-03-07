import pytest
from src.dynamic_progress_logger import log_with_progress_bar

def test_basic_progress_bar():
    """Test basic functionality of progress bar"""
    def double(x):
        return x * 2
    
    items = list(range(5))
    results = log_with_progress_bar(items, double)
    assert results == [0, 2, 4, 6, 8]

def test_empty_iterable():
    """Test processing an empty iterable"""
    def identity(x):
        return x
    
    items = []
    results = log_with_progress_bar(items, identity)
    assert results == []

def test_disable_progress_bar():
    """Test disabling the progress bar"""
    def add_one(x):
        return x + 1
    
    items = list(range(3))
    results = log_with_progress_bar(items, add_one, disable_progress=True)
    assert results == [1, 2, 3]

def test_invalid_items_type():
    """Test raising TypeError for non-iterable input"""
    def dummy_func(x):
        return x
    
    with pytest.raises(TypeError, match="Input must be an iterable"):
        log_with_progress_bar(42, dummy_func)

def test_invalid_process_func():
    """Test raising TypeError for non-callable process function"""
    items = [1, 2, 3]
    
    with pytest.raises(TypeError, match="process_func must be a callable function"):
        log_with_progress_bar(items, "not a function")

def test_empty_description():
    """Test raising ValueError for empty description"""
    def identity(x):
        return x
    
    items = [1, 2, 3]
    
    with pytest.raises(ValueError, match="Description cannot be an empty string"):
        log_with_progress_bar(items, identity, description="")