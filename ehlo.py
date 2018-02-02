#!/usr/bin/env python3
# Foundations of Python network Programming, Third Edition
# https://github.com/brandon-rhodes/fonp/bvlob/m/py3/chapter13/ehlo.py


import sys
import smtplib
import socket

message_template = """To: {}
From: {}
Subject: Test Message from simple.py
Hello,
This is a test message sent to you from the simple.py program
in Foundations of Python Network Programming.
"""

def main():
    if len(sys.argv) < 4:
        name = sys.argv[0]
        print("Usage: () server fromaddr toaddr [toaddr...]".format(name))
        sys.exit(2)

    server , fromaddr, toaddrs = sys.argv[1], sys.argv[2], sys.argv[3:]
    message = message_template.format(', '.join(toaddrs), fromaddr)

    try:
        connection = smtplib.SMTP(server)
        report_on_message_size(connection, fromaddr, toaddrs, message)
    except (socket.gaierror, socket.error, socket.herror,smtplib.SMTPException) as e:
        print("Your messgae may not have been sent!")
        print(e)
    else:
        a = '' if len(toaddrs) == 1 else 's'
        print("Message sent to {} recipient{}".format(len(toaddrs), s))
        connection.quit()


def report_on_message_size(connection, fromaddr, toaddrs, message):
    code = connection.ehlo()[0]
    uses_esmtp = (200 <= code <= 299)
    if not uses_esmtp:
        code = connection.helo()[0]
        if not (200 <= code <= 299):
            print('Remote sever refused HELO; code:', code)
            sys.exit(1)

    if uses_esmtp and connection.has_extn('size'):
        print("Maximuim messgae size is", connection.esmtp_features['size'])
        if len(message) > int(connection.esmtp_features['size']):
            print("Message to large; aborting.")
            sys.exit(1)

    connection.sendmail(fromaddr, toaddrs, message)


if __name__ == '__main__':
    main()
