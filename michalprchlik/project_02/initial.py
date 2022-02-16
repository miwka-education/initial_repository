#!/bin/python3

import os

from modules.module import function

def initial():
    return 1

print(os.environ.get('GITHUB_ACTOR'))

function()