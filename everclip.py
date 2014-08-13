#!/usr/bin/env python

import re
from imbox import Imbox
import settings

from emilisto.interact import interact


class Everclip(object):

    def __init__(self):
        self.imbox = Imbox(settings.IMAP_HOST, username=settings.IMAP_USERNAME,
                password=settings.IMAP_PASSWORD)

    def get_new_emails(self):
        emails = self.imbox.messages(sent_to=settings.TO_ADDRESS, unread=True)
        return list(emails)

    def run(self):
        print "Checking for new emails..."
        emails = self.get_new_emails()
        print "No. of new emails: %d" % (len(emails),)
        for id, email in emails:
            # Plain is given as a list - in case of multipart perhaps?
            plain = ' '.join(email.body['plain'])

            links = extract_links_from_text(plain)
            print links
            # TODO: scrape the supplied article using Goose
            # TODO: mark as read
            # TODO: add to EverNote


def extract_links_from_text(text):
    '''
    Takes a chunk of text and returns a list of all HTTP links identified in it
    '''

    links = re.findall(r'(https?://[^\s]+)', text)
    return links


def main():
    everclip = Everclip()
    everclip.run()

if __name__ == '__main__':
    main()
