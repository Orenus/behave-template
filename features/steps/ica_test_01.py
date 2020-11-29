import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@given('se navega a "{site}"')
def step(context, site):
    context.driver.get(site)
