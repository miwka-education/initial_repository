#!/bin/python3

import os

username = os.environ.get('GITHUB_ACTOR')

function = getattr(__import__(username, fromlist=[project_02.modules.module]), project_02.modules.module)

def initial():
    return 1

print(os.environ.get('GITHUB_ACTOR'))

function()