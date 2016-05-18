#!/usr/bin/env python
# pylint: disable=unused-argument,function-redefined,missing-docstring
"""
Step definitions for the seer feature
"""

from subprocess import call
# pylint: disable=no-name-in-module
from behave import given, when, then
import yaml

import common


@given(u'seer is available on the path')
def step_impl(context):
    return_code = call('which seer', shell=True)

    if return_code != 0:
        raise Exception('Seer could not be found on the path')

@when(u'seer is run')
def step_impl(context):
    context.response = common.run_command(['seer'])

@then(u'seer\'s usage will be output')
def step_impl(context):
    output = context.response['stdout'].read()
    expected = context.text
    if not output.startswith(expected):
        exception_text = (
            "Seer's usage output:\n\n```\n{}\n```\n\n" +
            "did not begin with expected:\n\n```\n{}\n```\n\n"
        ).format(output, expected)
        raise Exception(exception_text)

@given(u'a <definition_file> present in the project')
def step_impl(context):
    context.response = {}
    for row in context.table:
        definition_file = row['definition file']
        common.make_example_file(definition_file, yaml.load(context.text)['ci_file'])
        context.response[definition_file] = common.run_command(['seer'],
                                                               cwd='features/example')
        common.remove_example_file(definition_file)

@then(u'the seer.yml\'s scripts will be run')
def step_impl(context):
    for row in context.table:
        definition_file = row['definition file']
        row_context = context.response[definition_file]
        if not row_context.stdout == yaml.load(context.text)['output']:
            raise Exception("Seer did not run defined scripts")

@then(u'the .travis.yml\'s scripts will be run')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the .travis.yml\'s scripts will be run')

@then(u'the ci.yml\'s scripts will be run')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the ci.yml\'s scripts will be run')
