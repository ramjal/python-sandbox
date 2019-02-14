'''
    On your gmail account you need to turn 'Allow less secure apps' to ON.
    https://myaccount.google.com/lesssecureapps
    Be aware that this makes it easier for others to gain access to your account. 
'''

import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 465  # For SSL
from_addr = "rjalali@westlandinsurance.ca"
to_addr = "vancouverdevelop@gmail.com"
subject = "I am testing email from Python"
body = "This is the body of the email.\nSecond line is tested..."
msg = 'Subject: {}\n\n{}'.format(subject, body)

password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("vancouverdevelop@gmail.com", password)
    server.sendmail(from_addr, to_addr, msg)   

print("successfully sent!")

