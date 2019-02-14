'''
    Custom SMTP Server for testing purpose
    Run this on a command line
'''

import smtpd
import asyncore

class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print('Receiving message from:', peer)
        print('Message addressed from:', mailfrom)
        print('Message addressed to :', rcpttos)
        print('Message length :', len(data))
        print('Message:\n:', data)
        return



try:
    server = CustomSMTPServer(('localhost', 1025), None)
    print("SMTP server started....")
    asyncore.loop()
except Exception as e:    
    print(str(e))
    asyncore.ExitNow

