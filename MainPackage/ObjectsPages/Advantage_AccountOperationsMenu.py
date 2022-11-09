# Account operations menu object in Advantage site
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Advantage_AccountOperationsMenu:
    def __init__(self, _driver: webdriver.Chrome):
        self.driver = _driver
        self.wait = WebDriverWait(self.driver, 60)

# ===Operations in ACCOUNT OPERATIONS MENU===
    def get_operations(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "#loginMiniTitle>label")

    # Click one of the operation by index
    # 0 = My account
    # 1 = My_Orders
    # 2 = Sign out
    def click_operation(self, index):
        self.wait.until(EC.element_to_be_clickable((By.ID, "loginMiniTitle")))
        self.get_operations()[index].click()

    # logout from the account
    def logout(self):
        self.click_operation(2)

    # click to my account in operations
    def click_my_account(self):
        self.click_operation(0)

    # click to my orders in operations
    def click_my_orders(self):
        self.click_operation(1)