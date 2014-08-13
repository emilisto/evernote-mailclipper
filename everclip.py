import re

from imbox import Imbox
from goose import Goose
from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types

import settings

from emilisto.interact import interact


class Everclip(object):

    def __init__(self):
        self.imbox = Imbox(settings.IMAP_HOST, username=settings.IMAP_USERNAME,
                password=settings.IMAP_PASSWORD)

        self.evernote = EvernoteClient(token=settings.EVERNOTE_TOKEN,
                sandbox=False)
        self.noteStore = self.evernote.get_note_store()

    def get_new_emails(self):
        emails = self.imbox.messages(sent_to=settings.TO_ADDRESS, unread=True)
        return list(emails)

    def process_email(self, email):
        # Plain is given as a list - in case of multipart perhaps?

        # 1. Identify URL's in email
        plain = ' '.join(email.body['plain'])
        urls = extract_urls_from_text(plain)
        # NOTE: what to do about multiple links? include all of them? For now,
        # just choose the first one.
        url = urls[0]

        # 2. Extract URL content
        title, text = extract_url_content(url)

        # 3. Add to EverNote
        note = Types.Note()
        note.title = title
        note.content = text_to_enml(text).encode('utf8')

        attributes = Types.NoteAttributes()
        attributes.sourceURL = url
        note.attributes = attributes

        note = self.noteStore.createNote(note)

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

    urls = re.findall(r'(https?://[^\s]+)', text)
    return urls


def extract_url_content(url):
    '''Returns a tuple containing (title, plaintext_content)'''
    goose = Goose()
    article = goose.extract(url)
    return article.title, article.cleaned_text


def text_to_enml(text):
    enml = u'<?xml version="1.0" encoding="UTF-8"?>' \
           u'<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
    enml_text = text.replace('\n', u'<br/>')
    enml += u'<en-note>{}</en-note>'.format(enml_text)
    return enml


def main():
    everclip = Everclip()
    everclip.run()

if __name__ == '__main__':
    main()
