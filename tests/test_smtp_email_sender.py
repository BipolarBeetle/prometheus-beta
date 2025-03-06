import pytest
import smtplib
from src.smtp_email_sender import send_email
from unittest.mock import patch

def test_send_email_valid_inputs():
    """Test sending an email with valid inputs."""
    with patch('smtplib.SMTP') as mock_smtp:
        mock_instance = mock_smtp.return_value.__enter__.return_value
        result = send_email(
            sender_email='test@example.com', 
            sender_password='password123', 
            recipient_email='recipient@example.com', 
            subject='Test Subject', 
            body='Test Body'
        )
        assert result is True
        mock_instance.starttls.assert_called_once()
        mock_instance.login.assert_called_once_with('test@example.com', 'password123')
        mock_instance.send_message.assert_called_once()

def test_send_email_missing_parameters():
    """Test sending an email with missing parameters."""
    with pytest.raises(ValueError):
        send_email(
            sender_email='', 
            sender_password='password123', 
            recipient_email='recipient@example.com', 
            subject='Test Subject', 
            body='Test Body'
        )

def test_send_email_smtp_exception():
    """Test handling of SMTP exceptions."""
    with patch('smtplib.SMTP') as mock_smtp:
        # Simulate SMTP exception
        mock_smtp.return_value.__enter__.return_value.starttls.side_effect = smtplib.SMTPException("SMTP Error")
        
        result = send_email(
            sender_email='test@example.com', 
            sender_password='password123', 
            recipient_email='recipient@example.com', 
            subject='Test Subject', 
            body='Test Body'
        )
        assert result is False

def test_send_email_unexpected_exception():
    """Test handling of unexpected exceptions."""
    with patch('smtplib.SMTP') as mock_smtp:
        # Simulate an unexpected error
        mock_smtp.return_value.__enter__.return_value.starttls.side_effect = Exception("Unexpected Error")
        
        result = send_email(
            sender_email='test@example.com', 
            sender_password='password123', 
            recipient_email='recipient@example.com', 
            subject='Test Subject', 
            body='Test Body'
        )
        assert result is False