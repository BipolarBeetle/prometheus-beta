import pytest
from src.font_logger import FontLogger

def test_font_logger_default_size(capsys):
    """Test logging with default normal size"""
    result = FontLogger.log("Test message")
    captured = capsys.readouterr()
    assert result == "[NORMAL] Test message"
    assert captured.out.strip() == "[NORMAL] Test message"

def test_font_logger_different_sizes(capsys):
    """Test logging with different font sizes"""
    sizes = [
        (FontLogger.SMALL, "[SMALL] "),
        (FontLogger.NORMAL, "[NORMAL] "),
        (FontLogger.LARGE, "[LARGE] "),
        (FontLogger.EXTRA_LARGE, "[EXTRA LARGE] ")
    ]
    
    for size, prefix in sizes:
        result = FontLogger.log("Test message", size)
        captured = capsys.readouterr()
        assert result == f"{prefix}Test message"
        assert captured.out.strip() == f"{prefix}Test message"

def test_font_logger_invalid_size():
    """Test logging with an invalid font size"""
    with pytest.raises(ValueError, match="Invalid font size"):
        FontLogger.log("Test message", "invalid_size")

def test_font_logger_invalid_message_type():
    """Test logging with a non-string message"""
    with pytest.raises(TypeError, match="Message must be a string"):
        FontLogger.log(123)
    with pytest.raises(TypeError, match="Message must be a string"):
        FontLogger.log(None)

def test_font_logger_empty_message(capsys):
    """Test logging an empty string"""
    result = FontLogger.log("")
    captured = capsys.readouterr()
    assert result == "[NORMAL] "
    assert captured.out.strip() == "[NORMAL]"