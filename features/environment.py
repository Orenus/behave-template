#from browser import Browser
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_all(context):
    chromeOptions = Options()

    chromeOptions.headless = False
    #chromeOptions.headless = True

    context.driver = webdriver.Chrome(
        executable_path='chromedriver',
        chrome_options=chromeOptions)
    context.driver.implicitly_wait(10)


def after_all(context):
    context.driver.close()
