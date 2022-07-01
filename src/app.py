#!/usr/bin/python3

from os import environ
from json import loads


GITHUB_EVENT_PATH = environ.get('GITHUB_EVENT_PATH', './test/event.json')
ACCESS_TOKEN = environ.get('ACCESS_TOKEN', 'dummy-token')

print(GITHUB_EVENT_PATH, ACCESS_TOKEN)



with open(GITHUB_EVENT_PATH, "r") as event_file:
    event = loads(event_file.read())


print(type(event), event)

from pprint import pprint

pprint(event)