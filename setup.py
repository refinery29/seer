#!/usr/bin/env python

#
#   Copyright 2017 Brandon Schlueter
#   This file is part of Seer.
#
#   Seer is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program. If not, see <https://www.gnu.org/licenses/agpl.txt>.
#

import os
import sys

sys.path.insert(0, os.path.abspath('lib'))

# pylint: disable=import-error
from release import __version__, __author__
from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup( name='Seer'
     , description="Simple Effective Endeavor Runner"
     , author_email='seer@schlueter.blue'
     , url='http://seer.schlueter.blue'
     , license='GNU Affero General Public License v3 or later (AGPLv3+)'
     , install_requires=requirements
     , package_dir = {'': 'lib'}
     , author=__author__
     , version=__version__
     , scripts=[os.path.join('bin', f) for f in os.listdir('bin')]
     , classifiers=[ 'Development Status :: 5 - Production/Stable'
                   , 'Environment :: Console'
                   , 'Intended Audience :: Developers'
                   , 'Intended Audience :: Information Technology'
                   , 'Intended Audience :: System Administrators'
                   , 'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)'
                   , 'Natural Language :: English'
                   , 'Operating System :: POSIX'
                   , 'Operating System :: MacOS :: MacOS X'
                   , 'Programming Language :: Python'
                   , 'Programming Language :: Python :: 2.7'
                   , 'Topic :: Software Development :: Testing'
                   , 'Topic :: Software Development :: Build Tools'
                   , 'Topic :: Utilities'
    ])
