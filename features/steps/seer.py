#!/usr/bin/env python
# pylint: disable=unused-argument,function-redefined,missing-docstring
"""
Step definitions for the seer feature
"""

from subprocess import call
# pylint: disable=no-name-in-module
from behave import given, when, then

import common


@given(u'seer is available on the path')
def step_impl(context):
    return_code = call('which seer', shell=True)

    if return_code != 0:
        raise Exception('Seer could not be found on the path')

@when(u'seer is run')
def step_impl(context):
    context.response = common.run_command(['seer'], cwd='features/example')

@then(u'seer\'s usage will be output')
def step_impl(context):
    if context.response['stdout'].read().startswith(context.text) \
            and not context.response['stderr']:
        raise Exception("Seer's usage output did not match expected")

@given(u'a <definition_file> present in the project')
def step_impl(context):
    context.response = {}
    for row in context.table:
        definition_file = row['definition file']
        common.make_example_file(definition_file, context.text)
        context.response[definition_file] = common.run_command(['seer'],
                                                               cwd='features/example')
        common.remove_example_file(definition_file)

@then(u'the seer.yml\'s scripts will be run')
def step_impl(context):
    for row in context.table:
        definition_file = row['definition file']
        row_context = context.response[row['definition file']]
        print(row_context['stdout'])

@then(u'the .travis.yml\'s scripts will be run')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the .travis.yml\'s scripts will be run')

@then(u'the ci.yml\'s scripts will be run')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the ci.yml\'s scripts will be run')
