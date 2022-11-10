# Shopping cart methods in advantage site
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from selenium.webdriver.chrome.service import Service
# from time import sleep
# from Advantage_SignInPopUp import Advantage_SignInPopUp
# from Advantage_ToolBar import Advantage_ToolBar
# from Advantage_AccountOperationsMenu import Advantage_AccountOperationsMenu

class Advantage_ShoppingCart:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    # return the title
    def shopping_cart_title_element(self):
        return self.driver.find_element(By.LINK_TEXT, "SHOPPING CART")

    # A method that returns the shopping cart list
    def products_table(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#shoppingCart>table>tbody')

    def products_list(self):
        return self.products_table().find_elements(By.TAG_NAME, 'tr')

    def get_row_by_index(self, index):
        return self.products_list()[index]

    def get_columns_by_rowIndex(self, index):
        row = self.get_row_by_index(index)
        cols = row.find_elements(By.TAG_NAME, "td")
        return cols

    def product_name_by_rowIndex(self, index):
        cols = self.get_columns_by_rowIndex(index)
        name = cols[1].find_element(By.TAG_NAME, "label").text
        if len(name) > 27:
            new_name = name[:27]
            return new_name
        return name

    def product_color_by_rowIndex(self, index):
        cols = self.get_columns_by_rowIndex(index)
        return cols[-3].find_element(By.TAG_NAME, "span").get_attribute("title")

    def product_qty_by_rowIndex(self, index):
        cols = self.get_columns_by_rowIndex(index)
        label_list = cols[-2].find_elements(By.TAG_NAME, "label")
        return int(label_list[1].text)

    def product_price_by_rowIndex(self, index):
        cols = self.get_columns_by_rowIndex(index)
        price_non_space = cols[-1].find_element(By.TAG_NAME, "p").text.replace(" ","")
        price = float(price_non_space[1:].replace(",",""))
        return price

    def edit_product_by_rowIndex(self, index):
        cols = self.get_columns_by_rowIndex(index)
        span_tag = cols[-1].find_element(By.TAG_NAME, "span")
        a_list = span_tag.find_elements(By.TAG_NAME, "a")
        self.driver.execute_script("arguments[0].click();", a_list[0])

    # A method that checks if that shopping cart is empty
    def is_empty(self):
        if len(self.products_list()) == 0:
            return True
        else:
            return False

    # get the total price as integer
    def total_price(self):
        table_foot = self.driver.find_element(By.CSS_SELECTOR, '#shoppingCart>table>tfoot')
        rows = table_foot.find_elements(By.TAG_NAME, "tr")
        cols = rows[0].find_elements(By.TAG_NAME, "td")
        span_list = cols[1].find_elements(By.TAG_NAME, "span")
        price_str = span_list[1].text[1:].replace(",", "")
        price = float(price_str)
        return price

    def checkout_button(self):
        return self.driver.find_element(By.ID, "checkOutButton")

    def click_checkout(self):
        # wait until the button clickable
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkOutButton")))
        self.checkout_button().click()


# === Check if the class work ===
# Setup
# service = Service(r"C:\seleniumQA7\chromedriver.exe")
# driver_chrome = webdriver.Chrome(service=service)
# driver_chrome.get("https://advantageonlineshopping.com/#/")
# driver_chrome.implicitly_wait(30)
# driver_chrome.maximize_window()
# toolbar= Advantage_ToolBar(driver_chrome)
# sign_in_page = Advantage_SignInPopUp(driver_chrome)
# shopping_cart_pag = Advantage_ShoppingCart(driver_chrome)
#
# toolbar.click_user()
# sign_in_page.sign_in("test0001", "Aabc12")
# toolbar.click_cart()
# sleep(1)
# print(shopping_cart_pag.total_price())
# sleep(5)

