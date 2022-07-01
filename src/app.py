#!/usr/bin/python3

from os import environ
from json import load


GITHUB_EVENT_PATH = environ.get('GITHUB_EVENT_PATH', 'dummy-event')
ACCESS_TOKEN = environ.get('ACCESS_TOKEN', 'dummy-token')

print(GITHUB_EVENT_PATH, ACCESS_TOKEN)



with open(GITHUB_EVENT_PATH) as event_file:
    event = load(event_file.read())


print(type(event), event)