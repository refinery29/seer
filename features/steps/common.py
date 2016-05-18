#!/usr/bin/env python
"""
Shared environment for seer tests
"""

import os
from subprocess import Popen, PIPE


COMMON_FILE_PATH = os.path.realpath(__file__)
SEER_BIN_PATH = os.path.join(COMMON_FILE_PATH, '..', '..', '..', 'bin')
REAL_SEER_BIN_PATH = os.path.realpath(SEER_BIN_PATH)
os.environ['PATH'] = ':'.join([REAL_SEER_BIN_PATH, os.environ['PATH']])

def make_example_file(filename, contents=''):
    """
    Make a file in the example directory
    """
    with open(os.path.join('..', 'example', filename), 'w') as example_file:
        example_file.write(contents)

def remove_example_file(filename):
    """
    Remove an example file
    """
    os.remove(filename)

def run_command(command_args, cwd='.'):
    """
    Run a command and populate the context provide's response
    with its stdout, stderr, and returncode.
    """
    seer_call = Popen(command_args, stdout=PIPE, stderr=PIPE, shell=True, cwd=cwd)
    seer_call.wait()
    return dict(stdout=seer_call.stdout,
                stderr=seer_call.stderr,
                returncode=seer_call.returncode)
