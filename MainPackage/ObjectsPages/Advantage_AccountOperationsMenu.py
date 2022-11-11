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

    # delete account when the account operations menu open
    def delete_account(self):
        self.click_my_account()
        # wait until my account page appear
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='MY ACCOUNT']")))
        # click delete button
        self.driver.find_element(By.XPATH, "//*[text()='Delete Account']").click()
        # wait until 'Are you sure' window located
        self.wait.until(EC.visibility_of_element_located((By.ID, "deleteAccountPopup")))
        self.driver.execute_script("arguments[0].click();", self.red_button())
        # wait to category in main page located
        self.wait.until(EC.visibility_of_element_located((By.ID, "our_products")))

    def red_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".deletePopupBtn.deleteRed")

    def green_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".deletePopupBtn.deleteGreen")


# === Check if the class work ===
# Setup
# service = Service(r"C:\seleniumQA7\chromedriver.exe")
# driver_chrome = webdriver.Chrome(service=service)
# driver_chrome.get("https://advantageonlineshopping.com/#/")
# driver_chrome.implicitly_wait(30)
# driver_chrome.maximize_window()
# toolbar = Advantage_ToolBar(driver_chrome)
# this_page = Advantage_AccountOperationsMenu(driver_chrome)
# sign_in_page = Advantage_SignInPopUp(driver_chrome)
#
# toolbar.click_user()
# sign_in_page.sign_in("test0001", "Aabc12")
# toolbar.click_user()
# this_page.delete_account()
# sleep(10)