#!/usr/bin/python3

from os import listdir
from json import loads
from config import *

def get_github_event(GITHUB_EVENT_PATH):
    json_event = {}
    try:
        with open(GITHUB_EVENT_PATH, "r") as event_file:
            string_event = event_file.read()
            json_event = loads(string_event)
    except Exception as ex:
        pass
    finally:
        return json_event


def get_filenames(extension):
    output = listdir(GITHUB_WORKSPACE)
    return output


def push_medium(commits_info):
    commit_sha = commits_info.get('id')
    filename = get_filenames(".md")
    print('Will be pushing --> ', filename)



if __name__ == '__main__':
    KEYWORDS = {
        '[push:medium]' : push_medium
    }
    
    event = get_github_event(GITHUB_EVENT_PATH)
    commits_info = event.get('commits',[{}])[0]

    for key in KEYWORDS.keys():
        if key in commits_info.get('message', ''):
            print(f'Found {key} in commit. Executing {KEYWORDS[key].__name__}')
            KEYWORDS[key].__call__(commits_info)          
    else:
        print('Nothing found!!')