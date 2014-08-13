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
        return self.imbox.messages(sent_to=settings.TO_ADDRESS, unread=True)

    def run(self):
        everclip = Everclip()
        print "Checking for new emails..."
        emails = list(everclip.get_new_emails())
        print "No. of new emails: %d" % (len(emails),)
        for id, email in emails:
            interact()
            # TODO: mark as read


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
