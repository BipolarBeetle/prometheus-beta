import pytest
import logging
import io
from contextlib import redirect_stderr
from src.memory_logger import log_memory_usage

# Configure logging
logging.basicConfig(level=logging.INFO)

def test_memory_logger_basic_function(caplog):
    """Test memory logging on a simple function."""
    @log_memory_usage
    def sample_function(x, y):
        """A simple function to test memory logging."""
        return x + y
    
    # Set log level to INFO
    caplog.set_level(logging.INFO)
    
    # Call the function
    result = sample_function(10, 20)
    
    # Check result
    assert result == 30
    
    # Check log messages
    log_messages = caplog.messages
    assert any("Memory before sample_function" in msg for msg in log_messages)
    assert any("Memory after sample_function" in msg for msg in log_messages)
    assert any("Memory change for sample_function" in msg for msg in log_messages)

def test_memory_logger_memory_allocation(caplog):
    """Verify memory logging works with memory-intensive function."""
    @log_memory_usage
    def memory_intensive_function():
        """Create a large list to consume memory."""
        return [i * i for i in range(100000)]
    
    # Set log level to INFO
    caplog.set_level(logging.INFO)
    
    # Call the function
    result = memory_intensive_function()
    
    # Check result
    assert len(result) == 100000
    
    # Check log messages
    log_messages = caplog.messages
    memory_before_msgs = [msg for msg in log_messages if "Memory before" in msg]
    memory_after_msgs = [msg for msg in log_messages if "Memory after" in msg]
    memory_change_msgs = [msg for msg in log_messages if "Memory change" in msg]
    
    assert len(memory_before_msgs) == 1
    assert len(memory_after_msgs) == 1
    assert len(memory_change_msgs) == 1

def test_memory_logger_exception_handling(caplog):
    """Test memory logging with a function that raises an exception."""
    @log_memory_usage
    def exception_function():
        """A function that raises an exception."""
        raise ValueError("Test exception")
    
    # Set log level to ERROR
    caplog.set_level(logging.ERROR)
    
    # Verify exception is re-raised and logged
    with pytest.raises(ValueError, match="Test exception"):
        exception_function()
    
    # Check log messages include error
    log_messages = caplog.messages
    assert any("Error in exception_function" in msg for msg in log_messages)