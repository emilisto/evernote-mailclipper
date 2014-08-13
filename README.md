# Evernote Mailclipper

I store just about everything I read in EverNote but found it a bit too
cumbersome to quickly clip URL's from iOS devices for my taste.

Sending articles by emails doesn't work all that way since you end up
with a note with no more information than the title and URL.

However, most apps has a "Send as email" function! EverNote Mailclipper
will look for these emails, perform content extraction on them and add
them as nice and fat notes in your EverNote notebook.

This is faaar from, but the idea is to eventually get this up and
running as a service on Heroku or something like it, and have it do the
chore of scraping content for me.

Written by Emil Stenqvist <emsten@gmail.com> and licensed under GPL.

# Left to do before it's usable

- Make it long-running with periodic check of emails
- Mark processed emails as read
- Make it deployable to some convenient PaaS (e.g. Heroku) - (this
  probably also entails getting the settings from the env.)
- Do some useful logging of what's happening
- Catch errors
