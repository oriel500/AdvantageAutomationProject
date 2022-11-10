from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class TestCalcPage(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\selenium1\chromedriver.exe")

        # Open browser (create a driver object)
        self.driver = webdriver.Chrome(service=service_chrome)

        # Go to the required URL
        self.driver.get("https://advantageonlineshopping.com/#/")

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # Create an object for the Pages


    def test(self):
        pass