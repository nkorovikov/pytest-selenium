from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


class TestClass:

    def test_visit_site(self):
        time.sleep(3)
        driver = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)
        driver.get('https://google.com')

        assert 'Google' in driver.title

        driver.quit()
