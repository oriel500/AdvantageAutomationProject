# Toolbar in Advantage site
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Advantage_ToolBar:
    def __init__(self, _driver: webdriver.Chrome):
        self.driver = _driver
        self.wait = WebDriverWait(self.driver, 30)
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
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo>a")))
        self.logo_element().click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "our_products")))

    # hovering with the mouse on cart icon
    def hover_cart(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "menuCart")))
        self.actions.move_to_element(self.cart_element())
        self.actions.perform()

    # click on the cart icon and navigate to cart page
    def click_cart(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "menuCart")))
        self.cart_element().click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "shoppingCart")))


# === Check if the class work ===
# Setup
# service = Service(r"C:\seleniumQA7\chromedriver.exe")
# driver_chrome = webdriver.Chrome(service=service)
# driver_chrome.get("https://advantageonlineshopping.com/#/")
# driver_chrome.implicitly_wait(30)
# driver_chrome.maximize_window()
# page = Advantage_ToolBar(driver_chrome)
#
# page.click_cart()
# sleep(2)
# page.click_logo()
# sleep(5)
# page.hover_cart()
# sleep(10)
