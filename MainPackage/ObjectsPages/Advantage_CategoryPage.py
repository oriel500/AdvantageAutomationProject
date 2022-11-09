# Main page in Advantage site
from selenium import webdriver
from selenium.webdriver.common.by import By


class Advantage_CategoryPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    # Back from 'Tablets' to main page
    def select_main_page(self):
        self.driver.find_element(By.LINK_TEXT, 'HOME')

    def back_to_main_page(self):
        self.driver.find_element(By.LINK_TEXT, 'HOME').click()

    def select_product(self, num):
        list1 = self.driver.find_elements(By.TAG_NAME, 'li')
        if num > len(list1):
            pass
            # print(f'Num is not in range. Expected: 0 <= {num} <= {len(list1)}')
        else:
            return list1[num].get_attribute('id')
