#!/usr/bin/env python
# pylint: disable=unused-argument
"""
Shared environment for seer tests
"""

import os
import shutil


CURRENT_PATH = os.path.realpath(__file__)
EXAMPLE_DIR_PATH = os.path.realpath(os.path.join(CURRENT_PATH, '..', 'example'))

def before_scenario(context, scenario):
    """
    Clean example directory
    """
    os.mkdir(EXAMPLE_DIR_PATH)

def after_scenario(context, scenario):
    """
    Clean example directory
    """
    shutil.rmtree(EXAMPLE_DIR_PATH)
