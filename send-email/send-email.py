
# For testing:
# Run the following in the command prompt: 
#       python -m smtpd -n -c DebuggingServer localhost:1025
# Or in current folder run: 
#       custom-server.py

import smtplib, ssl

from_addr = "rjalali@westlandinsurance.ca"
to_addr = "vancouverdevelop@gmail.com"
subject = "I am testing email from Python"
body = "This is the body of the email.\nSecond line is tested..."
msg = 'Subject: {}\n\n{}'.format(subject, body)

try:
    with smtplib.SMTP("localhost", 1025) as server:
        server.sendmail(from_addr, to_addr, msg)

    print("successfully sent!")
except Exception as e: 
    print("Error!", e.args[1])
    

