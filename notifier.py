import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_email(english_summary, urdu_summary):
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")

    print("Connecting to Gmail server...")

    # MIMEMultipart useing 'alternative' for HTML content support
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "📰 Daily News Digest - Smart Summary"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Professional HTML Template with CSS styling & RTL for Urdu
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f4f7f6;
                margin: 0;
                padding: 20px;
            }}
            .container {{
                max-width: 650px;
                margin: auto;
                background: #ffffff;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            }}
            .header {{
                text-align: center;
                border-bottom: 2px solid #eaeaea;
                padding-bottom: 15px;
                margin-bottom: 20px;
            }}
            .header h1 {{
                color: #2c3e50;
                font-size: 24px;
                margin: 0;
            }}
            .section-title {{
                color: #16a085;
                font-size: 18px;
                margin-top: 25px;
                margin-bottom: 10px;
                border-left: 4px solid #16a085;
                padding-left: 10px;
            }}
            .content-box {{
                color: #333333;
                font-size: 15px;
                line-height: 1.6;
                white-space: pre-line;
            }}
            .urdu-box {{
                direction: rtl;
                text-align: right;
                font-family: 'Jameel Noori Nastaleeq', 'Urdu Typesetting', Arial, sans-serif;
                background-color: #f9fbfb;
                padding: 20px;
                border-radius: 8px;
                border-right: 4px solid #2980b9;
                margin-top: 30px;
                color: #2c3e50;
                line-height: 1.8;
                font-size: 16px;
            }}
            .urdu-title {{
                color: #2980b9;
                font-size: 18px;
                margin-bottom: 10px;
                border-right: 4px solid #2980b9;
                padding-right: 10px;
                text-align: right;
            }}
            .footer {{
                text-align: center;
                font-size: 12px;
                color: #888888;
                margin-top: 35px;
                border-top: 1px solid #eaeaea;
                padding-top: 15px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>📰 Daily News Digest</h1>
                <p style="color: #7f8c8d; font-size: 13px; margin: 5px 0 0;">Automated AI-Powered Intelligence Briefing</p>
            </div>

            <div class="section-title">English Summary</div>
            <div class="content-box">
                {english_summary}
            </div>

            <div class="urdu-box">
                <div class="urdu-title">خلاصہ (Urdu Summary)</div>
                <div style="white-space: pre-line;">
                    {urdu_summary}
                </div>
            </div>

            <div class="footer">
                <p>Powered by Python, Groq AI & BeautifulSoup | Developed by Arbish</p>
            </div>
        </div>
    </body>
    </html>
    """

    # Attach HTML content
    msg.attach(MIMEText(html_content, "html", "utf-8"))

    try:
        # Establish secure connection with Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully in HTML format! 🚀")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
