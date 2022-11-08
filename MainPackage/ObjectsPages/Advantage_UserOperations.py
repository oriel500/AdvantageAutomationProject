# Operations about account in Advantage site
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Advantage_UserOperations:
    def __init__(self, _driver: webdriver.Chrome):
        self.driver = _driver
        self.wait = WebDriverWait(self.driver, 60)

    # ===Operations in CREATE ACCOUNT PAGE===
    def username_editbox_register(self):
        return self.driver.find_element(By.NAME, "usernameRegisterPage")

    def email_editbox_register(self):
        return self.driver.find_element(By.NAME, "emailRegisterPage")

    def password_editbox_register(self):
        return self.driver.find_element(By.NAME, "passwordRegisterPage")

    def confirm_password_editbox_register(self):
        return self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")

    def agree_checkbox(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='i_agree']")

    def register_button(self):
        return self.driver.find_element(By.ID, "register_btnundefined")

    # Fill the fields in page CREATE ACCOUNT and register
    def register(self, username, email, password):
        # wait to title create account in page appear
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "article>h3"), "CREATE ACCOUNT"))
        self.username_editbox_register().send_keys(username)  # fill username
        self.email_editbox_register().send_keys(email)  # fill email
        self.password_editbox_register().send_keys(password)  # fill password
        self.confirm_password_editbox_register().send_keys(password)  # fill confirm password
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='i_agree']")))
        # check the "i_agree" checkbox
        self.driver.execute_script("arguments[0].click();", self.agree_checkbox())
        # wait register button to clickable
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='REGISTER']")))
        self.register_button().click()
        # wait to main page open
        self.wait.until(EC.visibility_of_element_located((By.ID, "our_products")))

    # ===Operations in POPUP SIGN IN===
    def username_editbox_sign_in(self):
        return self.driver.find_element(By.NAME, "username")

    def password_editbox_sign_in(self):
        return self.driver.find_element(By.NAME, "password")

    def sign_in_button(self):
        return self.driver.find_element(By.ID, "sign_in_btnundefined")

    # Sign in from sign in popup menu
    def sign_in(self, username, password):
        self.username_editbox_sign_in().send_keys(username)  # fill username
        self.password_editbox_sign_in().send_keys(password)  # fill password
        # wait to button sign in clickable
        self.wait.until(EC.element_to_be_clickable((By.ID, "sign_in_btnundefined")))
        self.sign_in_button().click()

    def create_account_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".create-new-account")

    def click_create_account(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".create-new-account")))
        self.driver.execute_script("arguments[0].click();", self.create_account_button())

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
        self.click_operation(1)

    # click to my orders in operations
    def click_my_orders(self):
        self.click_operation(1)


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


