from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def before_all(context):

    chromeOptions = Options()

    # chromeOptions.headless = False
    chromeOptions.headless = True

    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(executable_path='./chromedriver',
    #                                   chrome_options=chromeOptions)
    context.driver.implicitly_wait(10)


def after_all(context):
    context.driver.close()
