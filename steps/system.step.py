from behave import *
from tested_module import calc_image, get_image_price


@given('number of CPUs is {cpu}')
def step_impl(context, cpu):
    context.cpu = int(cpu)


@given('memory is {mem}')
def step_impl(context, mem):
    context.mem = int(mem)


@step('price should be {pph} per hour')
def step_impl(context, pph):
    actual_price = get_image_price(context.image, context.region)
    assert (actual_price == float(
        pph)), "expected price per hour of %s but got %.2f instead" % (pph, actual_price)


@then('image class should be {image_class}')
def step_impl(context, image_class):
    cpu = context.cpu
    mem = context.mem
    actual_image = calc_image(cpu, mem)
    assert (actual_image == image_class)
    context.image = actual_image
