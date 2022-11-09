# Operations about account in Advantage site
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Advantage_UserOperations:
    def __init__(self, _driver: webdriver.Chrome):
        self.driver = _driver
        self.wait = WebDriverWait(self.driver, 60)


# === Check if the class work ===
# Setup
# service = Service(r"C:\seleniumQA7\chromedriver.exe")
# driver_chrome = webdriver.Chrome(service=service)
# driver_chrome.get("https://advantageonlineshopping.com/#/")
# driver_chrome.implicitly_wait(30)
# driver_chrome.maximize_window()
# page = Advantage_ToolBar(driver_chrome)
# toolbar1 = Advantage_ToolBar(driver_chrome)
# user_op = Advantage_UserOperations(driver_chrome)
#
# toolbar1.click_user()
# sleep(2)
# user_op.click_create_account()
# user_op.register("text111", "testAOS@walla.com", "Aabc12")
# sleep(1)
# toolbar1.click_user()
# sleep(1)
# user_op.click_operation(2)
# sleep(20)


