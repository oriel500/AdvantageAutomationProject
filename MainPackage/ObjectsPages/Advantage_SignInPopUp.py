# Sign in popup window object in Advantage site
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Advantage_SignInPopUp:
    def __init__(self, _driver: webdriver.Chrome):
        self.driver = _driver
        self.wait = WebDriverWait(self.driver, 60)

    # return the sign in popup window
    def popup_window_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".login.ng-scope")

    def username_editbox(self):
        return self.driver.find_element(By.NAME, "username")

    def password_editbox(self):
        return self.driver.find_element(By.NAME, "password")

    def sign_in_button(self):
        return self.driver.find_element(By.ID, "sign_in_btnundefined")

    # Sign in from sign in popup menu
    def sign_in(self, username, password):
        self.username_editbox().send_keys(username)  # fill username
        self.password_editbox().send_keys(password)  # fill password
        # wait to button sign in clickable
        self.wait.until(EC.element_to_be_clickable((By.ID, "sign_in_btnundefined")))
        self.sign_in_button().click()
        # wait to main page open
        self.wait.until(EC.visibility_of_element_located((By.ID, "our_products")))

    def create_account_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".create-new-account")

    def click_create_account(self):
        # wait until the create account clickable
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".create-new-account")))
        # click by execute_script in the button
        self.driver.execute_script("arguments[0].click();", self.create_account_button())


# === Check if the class work ===
#Setup
# service = Service(r"C:\seleniumQA7\chromedriver.exe")
# driver_chrome = webdriver.Chrome(service=service)
# driver_chrome.get("https://advantageonlineshopping.com/#/")
# driver_chrome.implicitly_wait(30)
# driver_chrome.maximize_window()
# toolbar = Advantage_ToolBar(driver_chrome)
# create_account_page = Advantage_CreateAccountPage(driver_chrome)
# this_page = Advantage_SignInPopUp(driver_chrome)
# user_op = Advantage_UserOperations(driver_chrome)
#
# toolbar.click_user()
# this_page.sign_in("test0001", "Aabc12")
# toolbar.click_user()
# user_op.click_my_account()
# sleep(10)