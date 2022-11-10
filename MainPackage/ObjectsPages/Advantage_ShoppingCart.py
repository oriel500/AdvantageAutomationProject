# Shopping cart methods in advantage site
from selenium import webdriver
from selenium.webdriver.common.by import By


class Advantage_ShoppingCart:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    # A method that checks if you are in the cart page
    def shopping_cart_check(self):
        return self.driver.find_element(By.LINK_TEXT, "SHOPPING CART")

    # A method that returns the shopping cart list
    def products_table(self):
        return self.driver.find_elements(By.CSS_SELECTOR, 'tr[class="ng-scope"]')

    def products_list(self):
        list1 = self.driver.find_elements(By.CSS_SELECTOR, 'tr[class="ng-scope"]')
        return list1

    # A method that checks if that shopping cart is empty
    def shopping_cart_empty(self):
        if len(self.products_list()) == 0:
            return True
        else:
            return False

    # A method that sum the shopping cart price as the price and quantity of the products while choosing
    def total_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'span[class="roboto-medium ng-binding"]')

    # A method that checkout the shopping cart
    def check_out_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[role="button"]')

    def checkout_shopping_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '[role="button"]').click()
