#!/usr/bin/python3

from os import environ


GITHUB_EVENT = environ.get('GITHUB_EVENT_PATH', 'dummy-event')
ACCESS_TOKEN = environ.get('ACCESS_TOKEN', 'dummy-token')

print(GITHUB_EVENT, ACCESS_TOKEN)
