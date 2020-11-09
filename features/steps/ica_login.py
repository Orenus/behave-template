from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@given('se navega a "{site}"')
def step(context,site):
    context.browser.visit(site)
    pass


@when('se accede a la pagina principal')
def step(context):
    # search_field = context.find_element(By.XPATH, 'id("twotabsearchtextbox")')
    # search_field.send_keys(product)
    pass
