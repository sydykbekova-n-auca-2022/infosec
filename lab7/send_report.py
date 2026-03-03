import smtplib
from email.message import EmailMessage
from datetime import datetime

def send_email():
    msg = EmailMessage()
    msg.set_content(f"The server check was successful at {datetime.now()}")
    msg['Subject'] = "Automated Server Report"
    msg['From'] = "your_email@gmail.com"
    msg['To'] = "admin@example.com"

    # Replace with your SMTP server details
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('reciever@gmail.com', 'abcd abcd abcd abcd')  
            smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_email()


