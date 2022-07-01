from os import environ

GITHUB_EVENT_PATH = environ.get('GITHUB_EVENT_PATH', './test/event.json')
ACCESS_TOKEN = environ.get('ACCESS_TOKEN', 'dummy-token')
GITHUB_WORKSPACE = environ.get('GITHUB_WORKSPACE', '')
VERSION = 'v1.5.1'