# Gmail no longer supports less secure app access. Won't work like this
# Adding an app password might work
import smtplib
import ssl
from email.message import EmailMessage

# https://youtu.be/Oz3W-LKfafE?t=2543

subject = "Email from Python"
body = "This is a test email from Python."
sender_email = "tommy.marxsen11@gmail.com"
receiver_email = "tommy.marxsen11@gmail.com"
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
# message.set_content(body)

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending Email")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
print("Success")
