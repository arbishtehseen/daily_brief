import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_email(summary_text):
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")

    if not sender_email or not sender_password or not receiver_email:
        print("Error: .env file mein email credentials missing hain!")
        return

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Daily News Digest - Smart Summary 📰"

    message.attach(MIMEText(summary_text, "plain", "utf-8"))

    try:
        print("Connecting to Gmail server...")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email successfully send ho gayi! 🚀")

    except Exception as e:
        print(f"Email bhejte waqt error aa gaya: {e}")