from behave import given, then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import os
from dotenv import load_dotenv
load_dotenv('.env')


@given('se navega a "{site}"')
def step(context, site):
    context.driver.get(site)
    pass


@when('se accede a la pagina principal')
def step(context):

    print(context)
    SECRET_KEY = os.getenv('SECRET_00')

    box = context.driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div/div/div/div/div/div/form/div[1]/input')
    box.send_keys('joshua')
    pass
