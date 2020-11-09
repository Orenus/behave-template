from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Browser(object):

    chromeOptions = Options()
    chromeOptions.headless = True
    base_url = 'http://www.test.com'
    driver = webdriver.Chrome(
        executable_path='chromedriver',
        chrome_options=chromeOptions)
    driver.implicitly_wait(10)

    def close(self):
        """
        close the webdriver instance
        """
        self.driver.quit()

    def visit(self, location=''):
        """
        navigate webdriver to different pages
        """
        url = self.base_url + location
        #self.driver.get(url)
        self.driver.get(location)

    def find_by_id(self, selector):
        """
        find a page element in the DOM
        """
        return self.driver.find_element_by_id(selector)
