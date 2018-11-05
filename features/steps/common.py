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

def make_example_file(filename, context=None, contents=''):
    """Make a file in the example directory"""
    with open(os.path.join(context.behave_dir or '.', filename), 'w') as behave_file:
        behave_file.write(contents)

def make_example_dir(dirname, context=None):
    """Make a directory in the example directory"""
    os.mkdir(os.path.join(context.behave_dir or '.', dirname))

def run_command(args, context=None, path='.', complete=True):
    """
    Run a command and populate the context provide's response
    with its stdout, stderr, and returncode.
    """
    if isinstance(args, str):
        args.split()

    if context and context.behave_dir:
        cwd = os.path.join(context.behave_dir, path)
    else:
        cwd = path

    behave_call = Popen(args, stdout=PIPE, stderr=PIPE, shell=True, cwd=cwd)
    if complete:
        behave_call.wait()

    return dict(popen=behave_call,
                stderr=behave_call.stderr,
                stdin=behave_call.stdin,
                stdout=behave_call.stdout,
                rc=behave_call.returncode)

def has_all_items(expected, actual):
    """
    Confirm actual list contains only and all expected items
    """
    actual_list = [l for l in actual.split('\n')]
    expected_list = [l for l in expected.split('\n')]
    failed = False
    for line in actual_list:
        try:
            expected_list.remove(line)
        except ValueError:
            failed = True
    if failed or expected_list:
        raise Exception('Expected output \n\n"""\n{}\n"""\n did not match\n\n"""\n{}\n"""\n'.format(
            expected, actual))
