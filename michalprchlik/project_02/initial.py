#!/bin/python3

import os


def initial():
    return 1

print(os.environ.get('GITHUB_ACTOR'))