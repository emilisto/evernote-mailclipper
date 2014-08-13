#!/usr/bin/env python

import re
from imbox import Imbox
from goose import Goose
import settings

from emilisto.interact import interact


def extract_url_content(url):
    '''Returns a tuple containing (title, plaintext_content)'''
    goose = Goose()
    article = goose.extract(url)
    return article.title, article.cleaned_text


class Everclip(object):

    def __init__(self):
        self.imbox = Imbox(settings.IMAP_HOST, username=settings.IMAP_USERNAME,
                password=settings.IMAP_PASSWORD)

    def get_new_emails(self):
        emails = self.imbox.messages(sent_to=settings.TO_ADDRESS, unread=True)
        return list(emails)

    def process_email(self, email):
        # Plain is given as a list - in case of multipart perhaps?

        plain = ' '.join(email.body['plain'])
        urls = extract_urls_from_text(plain)
        # NOTE: what to do about multiple links? include all of them? For now,
        # just choose the first one.
        url = urls[0]

        title, content = extract_url_content(url)
        print content
        # TODO: add to EverNote

    def run(self):
        print "Checking for new emails..."
        emails = self.get_new_emails()
        print "No. of new emails: %d" % (len(emails),)
        for id, email in emails:
            self.process_email(email)
            # TODO: mark as read


def extract_urls_from_text(text):
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
