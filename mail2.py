from email import message
import smtplib, ssl
port = 587                                                                                                                         # For starttls
smtp_server = "smtp.gmail.com"
sender_email = str(input("From: "))
receiver_email = str(input("To: "))
password = input("Enter your password: ")
sub = input("Enter subject: ")
body = input("Enter body of the email:\n ")
message = ('subject:' + sub + "\n\n" + body )
print("mail sent successfully")
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()                                                                                                                # Can be omitted
    server.starttls(context=context)
    server.ehlo()                                                                                                                # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email,message)