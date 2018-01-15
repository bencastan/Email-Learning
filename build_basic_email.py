#! /usr/bin/python3
# Foundations of Python network Programming, Third Edition
# https://github.com/brandon-rhodes/fonp/bvlob/m/py3/chapter12/build_bhasic_email.py

import email.message, email.policy, email.utils, sys

text = """Hello,
This is a basic message from Chapter 12.
- Anonymous"""

def main():
    message = email.message.EmailMessage(email.policy.SMTP)
    message['To'] = 'recipient@example.com'
    message['From'] = 'Test Sender <sender@example.com>'
    message['Subject'] = 'Test Message, Chapter 12'
    message['Date'] = email.utils.formatdate(localtime=True)
    message['Message-ID'] = email.utils.make_msgid()
    message.set_content(text)
    sys.stdout.buffer.write(message.as_bytes())

if __name__ == '__main__':
    main()
