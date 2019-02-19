import sys
import send_gmail


def main():
    send_gmail.test()
    # service = send_gmail.service_factory()
    # testMessage = send_gmail.create_message('ramjal@gmail.com', 'rjalali@westlandinsurance.ca', 'This is the subject', 'Send by Google API: This is the body of the email')
    # send_gmail.send_message(service, 'me', testMessage)


if __name__ == '__main__':
    main()
