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
    example_file_path = os.path.realpath(
        os.path.join(COMMON_FILE_PATH, '..', '..', 'example', filename))
    with open(example_file_path, 'w') as example_file:
        example_file.write(contents)

# pylint: disable=unused-argument
def after_scenario(context, scenario):
    """
    Clean example directory
    """
    example_file_path = os.path.realpath(
        os.path.join(COMMON_FILE_PATH, '..', '..', 'example'))
    # pylint: disable=bad-builtin,deprecated-lambda
    map(lambda f: os.remove(f), os.listdir(example_file_path))

def run_command(command_args, cwd='.'):
    """
    Run a command and populate the context provide's response
    with its stdout, stderr, and returncode.
    """
    cwd = os.path.realpath(
        os.path.join(COMMON_FILE_PATH, '..', '..', 'example', cwd))

    if isinstance(command_args, str):
        command_args.split()

    seer_call = Popen(command_args,
                      stdout=PIPE,
                      stderr=PIPE,
                      shell=True,
                      cwd=cwd)
    seer_call.wait()
    return dict(stdout=seer_call.stdout,
                stderr=seer_call.stderr,
                returncode=seer_call.returncode)
