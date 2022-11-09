# Toolbar object in Advantage site
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Advantage_ToolBar:
    def __init__(self, _driver: webdriver.Chrome):
        self.driver = _driver
        self.wait = WebDriverWait(self.driver, 60)
        self.actions = ActionChains(self.driver)

    def logo_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".logo>a")

    def search_element(self):
        return self.driver.find_element(By.ID, "menuSearch")

    def user_element(self):
        return self.driver.find_element(By.ID, "menuUser")

    def cart_element(self):
        return self.driver.find_element(By.ID, "menuCart")

    def help_element(self):
        return self.driver.find_element(By.ID, "menuHelp")

    # click on the logo of the site and navigate to main page
    def click_logo(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".logo>a")))
        self.logo_element().click()

    # hovering with the mouse on cart icon
    def hover_cart(self):
        # wait for cart icon appear
        self.wait.until(EC.visibility_of_element_located((By.ID, "menuCart")))
        self.actions.move_to_element(self.cart_element())
        self.actions.perform()
        # wait for cart menu popup window appear
        self.wait.until(EC.visibility_of_element_located((By.ID, "toolTipCart")))

    # click on the cart icon in toolbar
    def click_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "menuCart")))
        self.cart_element().click()

    # click on the checkout button in cart popup window
    def click_cart_checkout_popup(self):
        self.hover_cart()
        self.driver.find_element(By.ID, "checkOutPopUp").click()

    # get the list of products in cart menu popup window
    def cart_list_products(self):
        self.hover_cart()
        return self.driver.find_elements(By.CSS_SELECTOR, "div>table")

    # get the product from the list of products in cart menu popup window
    def cart_product_by_index(self, index):
        self.hover_cart()
        return self.cart_list_products()[index].find_elements(By.TAG_NAME, "td")

    # get the name of product in cart menu popup window by index
    def get_name_product_by_index(self, index):
        # choose td from product
        choose_td = self.cart_product_by_index(index)[1]
        # get 'a' tag
        a_tag = choose_td.find_element(By.TAG_NAME, "a")
        # took from 'a' tag, h3 tag
        name = a_tag.find_element(By.TAG_NAME, "h3").text
        return name

    # get the price of product in cart menu popup window by index
    def get_price_product_by_index(self, index):
        # choose td from product
        choose_td = self.cart_product_by_index(index)[2]
        # get the price text
        price_str = choose_td.find_element(By.TAG_NAME, "p").text
        # return float price
        return price_str

    # get the QTY of product in cart menu popup window by index
    def get_qty_product_by_index(self, index):
        # choose td from product
        choose_td = self.cart_product_by_index(index)[1]
        # get 'a' tag
        a_tag = choose_td.find_element(By.TAG_NAME, "a")
        # get labels tags
        label_tags = a_tag.find_elements(By.TAG_NAME, "label")
        # return the price
        return label_tags[0].text.split()[1]

    # get the color of product in cart menu popup window by index
    def get_color_product_by_index(self, index):
        # choose td from product
        choose_td = self.cart_product_by_index(index)[1]
        # get 'a' tag
        a_tag = choose_td.find_element(By.TAG_NAME, "a")
        # get labels tags
        label_tags = a_tag.find_elements(By.TAG_NAME, "label")
        # return the color
        return label_tags[1].find_element(By.TAG_NAME, "span").text

    # click on the user icon in toolbar
    def click_user(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "menuUser")))
        self.user_element().click()


# === Check if the class work ===
# Setup
# service = Service(r"C:\seleniumQA7\chromedriver.exe")
# driver_chrome = webdriver.Chrome(service=service)
# driver_chrome.get("https://advantageonlineshopping.com/#/")
# driver_chrome.implicitly_wait(30)
# driver_chrome.maximize_window()
# page = Advantage_ToolBar(driver_chrome)
# sign_in_page = Advantage_SignInPopUp(driver_chrome)
#
# page.click_user()
# sign_in_page.sign_in("test0001", "Aabc12")
# print(page.get_color_product_by_index(0))
# page.click_cart_checkout_popup()
# sleep(5)


