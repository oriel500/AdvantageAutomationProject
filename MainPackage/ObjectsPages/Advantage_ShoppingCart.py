# Shopping cart methods in advantage site
from selenium import webdriver
from selenium.webdriver.common.by import By


class Advantage_ShoppingCart:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    # A method that checks if you are in the cart page
    def shopping_cart_check(self):
        return self.driver.find_element(By.LINK_TEXT, "SHOPPING CART")

    def shopping_cart_empty(self):
        return self.driver.find_element(By.LINK_TEXT, "Your shopping cart is empty")