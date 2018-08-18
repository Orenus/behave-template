from behave import *

@given('we have behave installed again')
def step_impl(context):
    pass
    # assert True is False

@when('we implement a second test')
def step_impl(context):
    assert True is not False

@then('my variable should be "{text}"')
def step_impl(context, text):
    myVar = "ok"
    assert text == myVar, "expected " + text + " but got " + myVar