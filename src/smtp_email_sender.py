import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(sender_email, sender_password, recipient_email, subject, body, 
               smtp_server='smtp.gmail.com', smtp_port=587):
    """
    Send an email using SMTP protocol with TLS encryption.

    Args:
        sender_email (str): Email address of the sender
        sender_password (str): Password for the sender's email account
        recipient_email (str): Email address of the recipient
        subject (str): Subject line of the email
        body (str): Body text of the email
        smtp_server (str, optional): SMTP server address. Defaults to Gmail's SMTP server.
        smtp_port (int, optional): SMTP server port. Defaults to 587 (TLS).

    Returns:
        bool: True if email sent successfully, False otherwise

    Raises:
        ValueError: If any of the required parameters are missing or invalid
        smtplib.SMTPException: For any SMTP-related errors
    """
    # Validate input parameters
    if not all([sender_email, sender_password, recipient_email, subject, body]):
        raise ValueError("All email parameters must be non-empty")

    try:
        # Create a multipart message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Attach the body of the email
        message.attach(MIMEText(body, 'plain'))

        # Create SMTP session
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Start TLS for security
            server.starttls()

            # Login to the server
            server.login(sender_email, sender_password)

            # Send email
            server.send_message(message)

        return True

    except smtplib.SMTPException as e:
        # Log the error or handle it as needed
        print(f"SMTP error occurred: {e}")
        return False
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return False