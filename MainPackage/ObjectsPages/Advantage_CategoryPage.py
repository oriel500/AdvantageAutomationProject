# Category page in Advantage site
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Advantage_CategoryPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    # A method that returns the text of the category name
    def category_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.categoryTitle').text

    # get the link text "HOME" in navigation line
    def select_main_page(self):
        return self.driver.find_element(By.LINK_TEXT, 'HOME')

    # Back from to main page by navigation line
    def back_to_main_page(self):
        self.driver.find_element(By.LINK_TEXT, 'HOME').click()

    # click on product by index in the list of products in category page
    def select_product(self, num):
        # wait until locate category title
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.categoryTitle')))
        # get the table of products
        table = self.driver.find_element(By.CSS_SELECTOR, ".categoryRight>ul")
        # get the list of products
        list1 = table.find_elements(By.TAG_NAME, 'li')
        return list1[num].click()
