# Main page elements in Advantage site
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Advantage_MainPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    # A methods that find a category element
    def speakers_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[id='speakersImg']")

    def tablets_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[id='tabletsImg']")

    def laptops_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[id='laptopsImg']")

    def mice_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[id='miceImg']")

    def headphones_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[id='headphonesImg']")

    # A method that selects a category and get into it
    def select_category(self, name: str):
        d1 = {'Speakers': 'speakersImg', 'Tablets': 'tabletsImg', 'Laptops': 'laptopsImg',
              'Mice': 'miceImg', 'Headphones': 'headphonesImg'}
        # wait to main page open
        self.wait.until(EC.visibility_of_element_located((By.ID, "our_products")))
        # click category
        self.driver.find_element(By.ID, d1[name]).click()
