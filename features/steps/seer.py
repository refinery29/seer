#!/usr/bin/env python
# pylint: disable=unused-argument,function-redefined,missing-docstring

from subprocess import call

# pylint: disable=no-name-in-module
from behave import given, when, then
from hamcrest import assert_that, equal_to, starts_with
from jinja2 import Template

import common


@given(u'seer is available on the path')
def step_impl(context):
    return_code = call('which seer', shell=True)
    assert_that(return_code, equal_to(0))

@when(u'seer is run')
def step_impl(context):
    context.response = common.run_command('seer -p')

@then(u'seer\'s usage will be output')
def step_impl(context):
    output = dict(std=context.response['stdout'].read(),
                  err=context.response['stderr'].read())
    expected = context.text
    assert_that(output['std'], starts_with(expected))
    assert_that('', equal_to(output['err']))


@given(u'a <definition_file> present in the project')
def step_impl(context):
    definition_file = context.active_outline['definition file']
    common.make_example_file(definition_file, context.text)

@then(u'the seer.yml\'s scripts will be run')
def step_impl(context):
    definition_file = context.active_outline['definition file']
    output = context.response['stdout'].read()
    expected = Template(context.text).render(definition_file=definition_file)
    assert_that(output, equal_to(expected))

@then(u'the .travis.yml\'s scripts will be run')
def step_impl(context):
    definition_file = context.active_outline['definition file']
    output = context.response['stdout'].read()
    expected = Template(context.text).render(definition_file=definition_file)
    assert_that(output, equal_to(expected))

@then(u'the ci.yml\'s scripts will be run')
def step_impl(context):
    definition_file = context.active_outline['definition file']
    output = context.response['stdout'].read()
    raise Exception("output=\n%s" % output)
    expected = Template(context.text).render(definition_file=definition_file)
    assert_that(output, equal_to(expected))
