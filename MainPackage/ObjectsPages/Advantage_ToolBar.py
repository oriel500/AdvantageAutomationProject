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
        # wait until the logo clickable
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
    def list_products(self):
        self.hover_cart()
        # wait the cart menu popup appear
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div>table")))
        table = self.driver.find_element(By.CSS_SELECTOR, "div>table")
        tr_list = table.find_elements(By.CSS_SELECTOR, "tr#product")
        return tr_list

    # get list of td tags from the list of products in cart menu popup window
    def get_product_by_index(self, index):
        self.hover_cart()
        td_list = self.list_products()[index].find_elements(By.TAG_NAME, "td")
        return td_list

    # get the name of product in cart menu popup window by index
    def get_name_product_by_index(self, index):
        # choose td from product
        choose_td = self.get_product_by_index(index)[1]
        # get 'a' tag
        a_tag = choose_td.find_element(By.TAG_NAME, "a")
        # took from 'a' tag, h3 tag
        name = a_tag.find_element(By.TAG_NAME, "h3").text
        # if the name above 27 letterers include spaces return name with only 27 letters
        # because in the cart menu popup the name of product can be included only 27 letters
        if len(name) > 27:
            new_name = name[:27]
            return new_name
        return name

    # get the price of product in cart menu popup window by index
    def get_price_product_by_index(self, index):
        # choose td from product
        choose_td = self.get_product_by_index(index)[2]
        # get the price text
        price_str = choose_td.find_element(By.TAG_NAME, "p").text[1:]
        price_str = price_str.replace(",", "")
        # change price_str to float
        return float(price_str)

    # get the QTY of product in cart menu popup window by index
    def get_qty_product_by_index(self, index):
        # choose td from product
        choose_td = self.get_product_by_index(index)[1]
        # get 'a' tag
        a_tag = choose_td.find_element(By.TAG_NAME, "a")
        # get labels tags
        label_tags = a_tag.find_elements(By.TAG_NAME, "label")
        # return the price
        return int(label_tags[0].text.split()[1])

    # get the color of product in cart menu popup window by index
    def get_color_product_by_index(self, index):
        # choose td from product
        choose_td = self.get_product_by_index(index)[1]
        # get 'a' tag
        a_tag = choose_td.find_element(By.TAG_NAME, "a")
        # get labels tags
        label_tags = a_tag.find_elements(By.TAG_NAME, "label")
        # return the color
        return label_tags[1].find_element(By.TAG_NAME, "span").text

    # remove product from the cart menu popup with index of the row
    def remove_product_by_index(self, index):
        # choose td from product
        choose_td = self.get_product_by_index(index)[2]
        # get the price text
        x_button = choose_td.find_element(By.CSS_SELECTOR, ".closeDiv>div")
        x_button.click()

    # click on the user icon in toolbar
    def click_user(self):
        # wait for user icon clickable
        self.wait.until(EC.element_to_be_clickable((By.ID, "menuUser")))
        # click the user icon
        self.user_element().click()
        # wait for cart menu popup window not appear
        self.wait.until_not(EC.visibility_of_element_located((By.ID, "toolTipCart")))

    # return the name of user next to user icon
    def get_name_user_icon(self):
        # wait for sign button not appear
        self.wait.until_not(EC.visibility_of_element_located((By.ID, "sign_in_btnundefined")))
        # wait for the account operation menu not appear
        self.wait.until_not(EC.visibility_of_element_located((By.ID, "loginMiniTitle")))

        name = self.driver.find_element(By.CSS_SELECTOR, "#menuUserLink>span").text
        return name
