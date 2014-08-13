# Evernote Mailclipper

I store just about everything I read in EverNote but found it a bit too
cumbersome for my taste to quickly clip web pages from iOS devices.

Sending articles by emails doesn't work all that well since you end up
with a lot of notes with nothing more than a title and a URL.

Most apps, however, has a "Send as email" functionality! EverNote
Mailclipper will look for these emails, perform content extraction on
them and add them as nice and content-rich notes.

This is faaar from done and working, but the idea is to eventually get
this up and running as a service on Heroku or something like it, and
have it do the chore of scraping content for me.

Written by Emil Stenqvist ([@svammel](https://twitter.com/svammel/) and
licensed under the GPL.

# Left to do before it's usable

- Make it long-running with periodic check of emails
- Mark processed emails as read
- Make it deployable to some convenient PaaS (e.g. Heroku) - (this
  probably also entails getting the settings from the env.)
- Do some useful logging of what's happening
- Catch errors
