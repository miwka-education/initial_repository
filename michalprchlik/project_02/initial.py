#!/bin/python3

import os

username = os.environ.get('GITHUB_ACTOR')
name = "project_02.modules.module"

function = getattr(__import__(username, fromlist=[name]), name)

def initial():
    return 1

print(os.environ.get('GITHUB_ACTOR'))

function()