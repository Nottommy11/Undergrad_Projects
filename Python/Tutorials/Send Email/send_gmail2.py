# Need to set up app password
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["From"] = "Thomas Marxsen"
message["To"] = "tommy.marxsen11@gmail.com"
message["Subject"] = "This is a test"
message.attach(MIMEText("Body"))

password = input("Enter a password: ")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("tommy.marxsen11@gmail.com", password)
    smtp.send_message(message)
    print("Sent...")



