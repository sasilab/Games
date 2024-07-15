import smtplib

sender = "###@gmail.com"
receiver = "####@gmail.com"
password = "####"
subject = "Python email test"
body = "Hi, I wrote an email! :D "


message = F"""From: {sender}
To:  {receiver}
Subject: {subject}\n
"""

try:
 server =smtplib.SMTP("smtp.gamil.com", 587)
 server.starttls()
 server.login(sender, password)
 print("Logged in .....")
 server.sendmail(sender, receiver, message)
 print("Email has been sent ! ")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")