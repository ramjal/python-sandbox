import sys
import pickle
import os.path
import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']

def test():
    print('testing from SendGmail')


def create_message(sender, to, subject, message_text):
    """Create a message for an email.

    Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

    Returns:
    An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def send_message(service, user_id, message):
    """Send an email message.

    Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

    Returns:
    Sent Message.
    """
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Successfully sent the email! Message Id: %s' % message['id'])        
        return message
    except Exception as e:
        print('An error occurred: %s' % e)


def service_factory():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    tokenfile = r'C:\DevLcl\Sandbox\python_sandbox\email\token.pickle'
    credfile = r'C:\DevLcl\Sandbox\python_sandbox\email\credentials.json'
    if os.path.exists(tokenfile):
        with open(tokenfile, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credfile, SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)
    return service


def main():
    service = service_factory()
    #testMessage = create_message('ramjal@gmail.com', 'vancouverdevelop@gmail.com', 'This is the subject', 'Send by Google API: This is the body of the email')
    testMessage = create_message('ramjal@gmail.com', 'rjalali@westlandinsurance.ca', 'This is the subject', 'Send by Google API: This is the body of the email')
    send_message(service, 'me', testMessage)

if __name__ == '__main__':
    main()
