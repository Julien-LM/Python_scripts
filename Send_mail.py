#!/usr/bin/env python
import getopt
import os
import smtplib
import sys


class Mail(object):
    """
    Class Mail
    """

    def __init__(self):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login("py.sys.info@gmail.com", os.getenv('GMAIL_PASS', None))

    def send_mail(self, msg="Empty message..."):
        self.server.sendmail("py.sys.info@gmail.com", "julien.lemellec@gmail.com", msg)

    def __del__(self):
        self.server.quit()


if __name__ == "__main__":
    message = "Empty..."
    try:
        opts, args = getopt.getopt(sys.argv[1:], "m:", ["message="])
    except getopt.GetoptError:
        print "Wrong argument..."
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-m' or opt == '--message':
            message = arg

    Mail().send_mail(message)
