from behave import *
from module_a import calc_image, start_app, test_port


use_step_matcher("re")

# The following step expression demonstrate a set of expected optional values. (application region)
# if feature provides an "invalid" option (not in regex) behave will complain for a step mismatch

# regex legend:
# aimed to match the aws region pattern eu-east, eu-west, us-east, ap-south etc.
# <region> name of var to assign match results into
# us|eu|ap|cn|ca|sa - matching options. usa, europe, asia pacific, china, canada, south america.
# (?:) - new group that needs to be matched but its result is ignored ?:
# -\w+ - minus sign followed by a sequence of alphanumeric characters (any length)


@step('deployment region is "(?P<region>us|eu|ap|cn|ca|sa)(?:-\w+)"')
def step_impl(context, region):
    context.region = region
    print ("============ > got region: " + region)


# The following step expression demonstrate a usage of multi regex matchers (step that expects many variables)
# It will implement a step statement like:
#   When I start 2 xlarge instances with "my-application-image" in the "ap-northeast" region
# 1st quantity matcher for "a" or "an" or number
# 2nd size matcher - any word. preferably should be optional list like reqion
# non catching but matching plurar s in instance(s)
# 3rd app image - expecting to match a word with -
# 4th region as in prev step implementation

@when('I start (?P<quantity>a|an|\d+) (?P<size>\w+) instance(?:s?) with "(?P<app_image>[\w|-]+)" in the "(?P<region>us|eu|ap|cn|ca|sa)(?:-\w+)" region')
def step_impl(context, quantity, size, app_image, region):
    print ("start app test args: %s %s %s %s" %
           (quantity, size, app_image, region))

    context.tested_instances = []
    if (quantity == "a" or quantity == "an"):
        quantity = 1

    for i in range(0, int(quantity)):
        instance = start_app(size, region, app_image)
        context.tested_instances.append(instance)


@then('I should be able to access (?:them|it) on port (?P<port>\d+)')
def step_impl(context, port):
    print ("port %s" % (port))
    for instance in context.tested_instances:
        result = test_port(instance["fqdn"], int(port))
        assert (result), "expected port %s on %s to be accessible but it isnt" % (
            port, instance['fqdn'])
