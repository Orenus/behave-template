from behave import given, then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# from environs import Env

# env = Env()
# # Read .env into os.environ
# env.read_env()

# env.bool("DEBUG")  # => True
# env.int("PORT")  # => 4567

@given('se navega a "{site}"')
def step(context, site):
    context.driver.get(site)
    pass


@when('se accede a la pagina principal')
def step(context):

    #SECRET_KEY = os.getenv('SECRET_00')

    box = context.driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div/div/div/div/div/div/form/div[1]/input')
    #box.send_keys('{}'.format(SECRET_KEY))
    box.send_keys('{}'.format('joshua'))

    #SECRET_KEY = os.getenv('SECRET_10')
    box = context.driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div/div/div/div/div/div/form/div[2]/input')
    #box.send_keys('{}'.format(SECRET_KEY))
    box.send_keys('{}'.format(12345678))

    button = context.driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div/div/div/div/div/div/form/div[3]/button')
    button.click()

    delay = 10  # seconds
    try:
        h1_title = WebDriverWait(context.driver, delay).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div/div[1]/h2')))
    except TimeoutException:
        print('timeout !')

    pass
