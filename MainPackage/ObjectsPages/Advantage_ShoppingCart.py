# Shopping cart methods in advantage site
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Advantage_ShoppingCart:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    # return the title
    def shopping_cart_title_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".sp>h3")

    # A method that returns the shopping cart list
    def products_table(self):
        # wait until the title of shopping cart appear
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sp>h3")))
        return self.driver.find_element(By.CSS_SELECTOR, '#shoppingCart>table>tbody')

    # get the list of products in shopping cart
    def products_list(self):
        return self.products_table().find_elements(By.TAG_NAME, 'tr')

    # get row in list of products by the index of the row
    def get_row_by_index(self, index):
        return self.products_list()[index]

    # get the columns from row by the index of the row
    def get_columns_by_rowIndex(self, index):
        row = self.get_row_by_index(index)
        cols = row.find_elements(By.TAG_NAME, "td")
        return cols

    # get the name of product by the index of the row
    def product_name_by_rowIndex(self, index):
        cols = self.get_columns_by_rowIndex(index)
        name = cols[1].find_element(By.TAG_NAME, "label").text
        # if the name above 27 letterers include spaces return name with only 27 letters
        # because in the cart menu popup the name of product can be included only 27 letters
        if len(name) > 27:
            new_name = name[:27]
            return new_name
        return name

    # get the color of product by the index of the row
    def product_color_by_rowIndex(self, index):
        cols = self.get_columns_by_rowIndex(index)
        return cols[-3].find_element(By.TAG_NAME, "span").get_attribute("title")

    # get the quantity of product by the index of the row
    def product_qty_by_rowIndex(self, index):
        cols = self.get_columns_by_rowIndex(index)
        label_list = cols[-2].find_elements(By.TAG_NAME, "label")
        return int(label_list[1].text)

    # get the price of product by the index of the row
    def product_price_by_rowIndex(self, index):
        cols = self.get_columns_by_rowIndex(index)
        price_non_space = cols[-1].find_element(By.TAG_NAME, "p").text.replace(" ", "")
        price = float(price_non_space[1:].replace(",", ""))
        return price

    # click edit from product by the index of the row
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
