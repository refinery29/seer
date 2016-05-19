#!/usr/bin/env python
# pylint: disable=unused-argument
"""
Shared environment for seer tests
"""

import shutil
import tempfile

import git


# pylint: disable=too-few-public-methods
class BehaveEnvironment(object):
    """An Environment for behave"""

    def __init__(self):
        self.behave_dir = tempfile.mkdtemp()
        self.git = git.Git(self.behave_dir)
        self.git.init()

    def cleanup(self):
        """Clean up behave directory environment"""
        shutil.rmtree(self.behave_dir)

def before_scenario(context, scenario):
    """
    Clean example directory
    """
    scenario.environment = BehaveEnvironment()
    context.behave_dir = scenario.environment.behave_dir
    context.git = scenario.environment.git

def after_scenario(context, scenario):
    """
    Clean example directory
    """
    scenario.environment.cleanup()
    context.behave_dir = None
