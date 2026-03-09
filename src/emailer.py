# src/emailer.py
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_digest(html_body: str, sender: str, password: str, recipient: str) -> None:
    """Send the HTML digest via Gmail SMTP."""
    today   = datetime.now().strftime("%B %d, %Y")
    subject = f"🤖 Your Daily AI Digest — {today}"

    msg            = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"]    = sender
    msg["To"]      = recipient

    plain = "Your daily AI digest is ready. Please view in an HTML-capable email client."
    msg.attach(MIMEText(plain, "plain"))

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Daily AI Digest</title>
</head>
<body style="margin:0;padding:0;background:#f4f4f8;font-family:system-ui,-apple-system,sans-serif;">
  <div style="max-width:680px;margin:0 auto;padding:24px 16px;">
    {html_body}
    <p style="text-align:center;color:#9ca3af;font-size:12px;margin-top:32px;">
      Generated automatically · Powered by Gemini AI · Free forever 🎉
    </p>
  </div>
</body>
</html>"""

    msg.attach(MIMEText(full_html, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())