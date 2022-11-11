# CREATE ACCOUNT PAGE object in Advantage site
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Advantage_CreateAccountPage:
    def __init__(self, _driver: webdriver.Chrome):
        self.driver = _driver
        self.wait = WebDriverWait(self.driver, 60)

    def username_editbox(self):
        return self.driver.find_element(By.NAME, "usernameRegisterPage")

    def email_editbox(self):
        return self.driver.find_element(By.NAME, "emailRegisterPage")

    def password_editbox(self):
        return self.driver.find_element(By.NAME, "passwordRegisterPage")

    def confirm_password_editbox(self):
        return self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")

    def agree_checkbox(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='i_agree']")

    def register_button(self):
        return self.driver.find_element(By.ID, "register_btnundefined")

    # Fill the fields in page CREATE ACCOUNT and register
    def register(self, username, email, password):
        # wait to title create account in page appear
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "article>h3"), "CREATE ACCOUNT"))
        self.username_editbox().send_keys(username)  # fill username
        self.email_editbox().send_keys(email)  # fill email
        self.password_editbox().send_keys(password)  # fill password
        self.confirm_password_editbox().send_keys(password)  # fill confirm password
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='i_agree']")))
        # mark the "i_agree" checkbox
        self.driver.execute_script("arguments[0].click();", self.agree_checkbox())
        # wait register button to clickable
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='REGISTER']")))
        self.register_button().click()
        # wait to category in main page located
        self.wait.until(EC.visibility_of_element_located((By.ID, "our_products")))
        sleep(2.5)  # the toolbar take time to reload

# === Check if the class work ===
# Setup
# service = Service(r"C:\seleniumQA7\chromedriver.exe")
# driver_chrome = webdriver.Chrome(service=service)
# driver_chrome.get("https://advantageonlineshopping.com/#/register")
# driver_chrome.implicitly_wait(30)
# driver_chrome.maximize_window()
# toolbar = Advantage_ToolBar(driver_chrome)
# toolbar1 = Advantage_ToolBar(driver_chrome)
# page = Advantage_CreateAccountPage(driver_chrome)
#
# page.register("test0001", "a@gmail.com", "Aabc12")
# sleep(20)


