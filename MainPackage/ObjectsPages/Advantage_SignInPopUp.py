# Sign in popup window object in Advantage site
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


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
        # wait fot the signin button appear
        self.wait.until(EC.visibility_of_element_located((By.ID, "sign_in_btnundefined")))

        self.username_editbox().send_keys(username)  # fill username
        self.password_editbox().send_keys(password)  # fill password
        # selenium think that button sign in clickable and located when the site loading
        # so put sleep to fix it
        sleep(3)
        # wait to button sign in clickable
        self.wait.until(EC.element_to_be_clickable((By.ID, "sign_in_btnundefined")))
        self.sign_in_button().click()
        # wait to category in main page located
        self.wait.until(EC.visibility_of_element_located((By.ID, "our_products")))

    # get the element create_account button
    def create_account_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".create-new-account")

    # click create account in signin popup window
    def click_create_account(self):
        # wait until the create account clickable
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".create-new-account")))
        # click by execute_script in the button
        self.driver.execute_script("arguments[0].click();", self.create_account_button())
