import smtplib
import pandas as pd
from email.message import EmailMessage

#Read email list from the CSV file
df = pd.read_csv('dummy_emails.csv')

# Read email content from file
with open('email.html', 'r', encoding='utf-8') as file:
    email_content = file.read()

# SMTP Configuration
smtp_server = "smtp.gmail.com"
port = 587
sender_email = "overnightbomb@gmail.com"
app_password = input("Enter App Password: ")  # Use an App Password instead of a regular password

# Sending email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # Start TLS for security
    server.login(sender_email, app_password)
    
    for name,email in zip(df["Name"], df["Email"]):

        msg = EmailMessage()
        msg['Subject'] = f"Hello {name}!, from Python!"
        msg['From'] = sender_email
        msg["To"] = email

        my_message_to_them = email_content.replace("{{name}}", name)
        msg.add_alternative(my_message_to_them, subtype='html')

        server.send_message(msg)
        print(f"Email sent to {name}, {email}")
except Exception as e:
    print("Error:", e)
finally:
    server.quit()
