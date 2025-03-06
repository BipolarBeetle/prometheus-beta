import pytest
from datetime import date
from src.get_current_date import get_formatted_current_date

def test_get_formatted_current_date_format():
    """
    Test that the returned date string matches the expected YYYY-MM-DD format.
    """
    # Get the formatted current date
    formatted_date = get_formatted_current_date()
    
    # Check that the string matches the expected format
    assert len(formatted_date) == 10, "Date string should be 10 characters long"
    
    # Check format components
    assert formatted_date[4] == '-', "Fifth character should be a hyphen"
    assert formatted_date[7] == '-', "Eighth character should be a hyphen"
    
    # Verify each part is the correct length and type
    year = formatted_date[:4]
    month = formatted_date[5:7]
    day = formatted_date[8:]
    
    assert year.isdigit(), "Year should be digits"
    assert month.isdigit(), "Month should be digits"
    assert day.isdigit(), "Day should be digits"

def test_get_formatted_current_date_accuracy():
    """
    Test that the returned date matches the actual current date.
    """
    # Get the function's output and today's date
    formatted_date = get_formatted_current_date()
    today = date.today()
    
    # Compare with today's date formatted the same way
    expected_date = today.strftime("%Y-%m-%d")
    
    assert formatted_date == expected_date, "Formatted date should match today's date"