# Product page methods in Advantage site
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Advantage_ProductPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 30)

    # Back from a tablet product page to 'Tablets' category page
    def tablets_category_element(self):
        return self.driver.find_element(By.LINK_TEXT, 'TABLETS')

    def back_to_tablets_category(self):
        self.driver.find_element(By.LINK_TEXT, 'TABLETS').click()

    # Get product name
    def product_name_element(self):
        name = self.driver.find_element(By.CSS_SELECTOR, '#Description>h1').text
        # if the name above 27 letterers include spaces return name with only 27 letters
        # because in the cart menu popup the name of product can be included only 27 letters
        if len(name) > 27:
            new_name = name[:27]
            return new_name
        return name

    # Get product price
    def get_price(self):
        price_non_space = self.driver.find_element(By.CSS_SELECTOR, '#Description>h2').text.replace(" ", "")
        price_str = price_non_space[1:].replace(",", "")
        price = float(price_str)
        return price

    # A method that selects the quantity of the product
    def quantity_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="quantity"]')

    # change quantity in product page
    def select_quantity(self, num: int):
        # wait until the plus button in product page clickable
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="plus"]')))
        if num == 1:
            pass
        else:
            for i in range(num-1):
                self.actions.move_to_element(self.driver.find_element(By.CSS_SELECTOR, '[class="plus"]'))
                self.actions.click(self.driver.find_element(By.CSS_SELECTOR, '[class="plus"]'))
                self.actions.perform()

    def add_to_cart_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="save_to_cart"]')

    # A method that add product to the cart
    def add_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '[name="save_to_cart"]').click()

    # A method that select the first color in product page
    def choose_first_color(self):
        # get the Description table of product
        table = self.driver.find_element(By.CSS_SELECTOR, "#Description>div#productProperties")
        # get the list of div tags in the table
        div_list = table.find_elements(By.TAG_NAME, "div")
        # get the row of colors
        color_row = div_list[0]
        # get the list of divs tage in the row of colors
        list_div_in_color_row = color_row.find_elements(By.TAG_NAME, "div")
        # get the list of colors
        list_colors = list_div_in_color_row[0].find_elements(By.TAG_NAME, "span")
        # get the color in index 0
        color = list_colors[0].get_attribute("title")
        return color
