# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step
from environs import Env
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.headless = True


env = Env()
env.read_env()

env.str("SECRET_USER")
env.str("SECRET_PWD")


@given('se navega a "{page}"')
def step_impl(context, page):
    driver = webdriver.Chrome(
        executable_path="./drivers/armhf/chromedriver", options=chromeOptions)
    # driver.maximize_window()
    driver.get(page)
    driver.quit()
    pass


@when('se accede a la pagina principal')
def step_impl(context):
    pass
