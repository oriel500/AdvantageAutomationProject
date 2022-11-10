# Actions about create order and order payment
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.service import Service
from time import sleep
from Advantage_SignInPopUp import Advantage_SignInPopUp
from Advantage_ToolBar import Advantage_ToolBar
from Advantage_AccountOperationsMenu import Advantage_AccountOperationsMenu
from selenium.webdriver.common.keys import Keys

class Advantage_OrderPayment_Actions:
    def __init__(self, _driver: webdriver.Chrome):
        self.driver = _driver
        self.wait = WebDriverWait(self.driver, 60)
        self.actions = ActionChains(self.driver)
        self.keys = Keys()

    # username from order payment page
    def username_editbox(self):
        return self.driver.find_element(By.NAME, "usernameInOrderPayment")

    # password from order payment page
    def password_editbox(self):
        return self.driver.find_element(By.NAME, "passwordInOrderPayment")

    def login_button(self):
        return self.driver.find_element(By.ID, "login_btnundefined")

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "login_btnundefined")))
        self.login_button().click()

    # login to user from order payment page
    def login_from_order_payment(self, username, password):
        self.username_editbox().send_keys(username)
        self.password_editbox().send_keys(password)
        self.click_login()

    def next_button(self):
        return self.driver.find_element(By.ID, "next_btn")

    def click_next(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "next_btn")))
        self.next_button().click()

    def safepay_radio_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='safepay']")

    def master_credit_radio_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='masterCredit'")

    def click_safepay(self):
        self.safepay_radio_button().click()

    def click_master_credit(self):
        self.master_credit_radio_button().click()

    def safepay_username_editbox(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='safepay_username']")

    def safepay_password_editbox(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='safepay_password']")

    def safepay_pay_now_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button#pay_now_btn_SAFEPAY")

    def master_pay_now_button(self):
        return self.driver.find_element(By.ID, "pay_now_btn_ManualPayment")

    def click_pay_now_safepay(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#pay_now_btn_SAFEPAY")))
        self.driver.execute_script("arguments[0].click();", self.safepay_pay_now_button())

    def click_pay_now_master(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "pay_now_btn_ManualPayment")))
        self.driver.execute_script("arguments[0].click();", self.master_pay_now_button())


    # pay now by safepay method with username and password
    def pay_now_by_safepay(self, username, password):
        self.click_safepay()
        self.safepay_username_editbox().clear()
        self.safepay_password_editbox().clear()
        self.safepay_username_editbox().send_keys(username)
        self.safepay_password_editbox().send_keys(password)
        self.click_pay_now_safepay()

    def master_card_number_editbox(self):
        return self.driver.find_element(By.ID, "creditCard")

    def master_cvv_editbox(self):
        return self.driver.find_element(By.NAME, "cvv_number")

    def master_cardholder_editbox(self):
        return self.driver.find_element(By.NAME, "cardholder_name")

    def month_select(self, mm: str):
        select = Select(self.driver.find_element(By.CSS_SELECTOR, "select[name='mmListbox']"))
        select.select_by_value(mm)

    def year_select(self, yyyy: str):
        select = Select(self.driver.find_element(By.CSS_SELECTOR, "select[name='yyyyListbox']"))
        select.select_by_value(yyyy)

    # pay now by master credit method
    def pay_now_by_master_credit(self, card_number, cvv, cardholder, mm, yyyy):
        # click master credit
        self.click_master_credit()
        # scroll down
        self.actions.scroll_to_element(self.master_card_number_editbox())
        # type card number
        self.master_card_number_editbox().send_keys(card_number)
        # type cvv
        self.master_cvv_editbox().send_keys("0"+cvv)
        # type cardholder
        self.master_cardholder_editbox().send_keys(cardholder)
        self.month_select(yyyy)
        self.year_select(yyyy)
        self.click_pay_now_master()

    # string from thank you page
    def thank_you_text(self):
        # wait until locate the text "Thank you..."
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2>span")))
        return self.driver.find_element(By.CSS_SELECTOR, "h2>span").text

    # tracking number from thank you page
    def tracking_number_from_thankYou_page(self):
        # wait until locate the text "Thank you..."
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2>span")))
        return self.driver.find_element(By.ID, "trackingNumberLabel").text

    # order number from thank you page
    def order_number_from_thankYou_page(self):
        # wait until locate the text "Thank you..."
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2>span")))
        return self.driver.find_element(By.ID, "orderNumberLabel").text

    def get_orders_table(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='MY ORDERS']")))
        return self.driver.find_element(By.CSS_SELECTOR, "div.cover>table")

    # get only the rows with order number
    def get_orders_rows(self):
        return self.get_orders_table().find_elements(By.CSS_SELECTOR, "tr[class='ng-scope']")

    # get the row of order by index
    def get_order_by_index(self, index):
        list_rows = self.get_orders_rows()
        return list_rows[index]

    # get the row of last order added
    def get_last_order(self):
        list_rows = self.get_orders_rows()
        return list_rows[-1]

    # get the id of order by index of rows in the table
    def get_id_order_by_index(self, index):
        # get row of order
        order = self.get_order_by_index(index)
        # get columns of row
        order_cols = order.find_elements(By.TAG_NAME, "td")
        # get id from column 0
        order_id = order_cols[0].find_element(By.TAG_NAME, "label").text
        return order_id

    # get the id of last order added
    def get_id_last_order(self):
        # get row of order
        order = self.get_order_by_index(-1)
        # get columns of row
        order_cols = order.find_elements(By.TAG_NAME, "td")
        # get id from column 0
        order_id = order_cols[0].find_element(By.TAG_NAME, "label").text
        return order_id

    def regstration_button(self):
        return self.driver.find_element(By.ID, "registration_btnundefined")

    def registration_click(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "registration_btnundefined")))
        self.regstration_button().click()


# === Check if the class work ===
# Setup
# service = Service(r"C:\seleniumQA7\chromedriver.exe")
# driver_chrome = webdriver.Chrome(service=service)
# driver_chrome.get("https://advantageonlineshopping.com/#/")
# driver_chrome.implicitly_wait(30)
# driver_chrome.maximize_window()
# toolbar = Advantage_ToolBar(driver_chrome)
# sign_in_page = Advantage_SignInPopUp(driver_chrome)
# orders_actions = Advantage_OrderPayment_Actions(driver_chrome)
# account_menu = Advantage_AccountOperationsMenu(driver_chrome)
#
# toolbar.click_user()
# sign_in_page.sign_in("test0001", "Aabc12")
# toolbar.click_cart_checkout_popup()
# sleep(1)
# orders_actions.click_next()
# sleep(2)

# master carf
# orders_actions.click_master_credit()
# sleep(2)
# orders_actions.pay_now_by_master_credit("123412341234", "123", "Oriel Naim", "01", "2026")
# sleep(10)

# safepay check
# orders_actions.pay_now_by_safepay("Test0001", "Aabc12")
# print(orders_actions.order_number_from_thankYou_page())
# toolbar.click_user()
# account_menu.click_my_orders()
# sleep(1)
# print(orders_actions.get_id_last_order())
# sleep(10)


