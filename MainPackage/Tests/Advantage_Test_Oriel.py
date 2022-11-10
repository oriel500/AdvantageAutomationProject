from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# ObjectsPages
from MainPackage.ObjectsPages.Advantage_AccountOperationsMenu import Advantage_AccountOperationsMenu
from MainPackage.ObjectsPages.Advantage_CategoryPage import Advantage_CategoryPage
from MainPackage.ObjectsPages.Advantage_CreateAccountPage import Advantage_CreateAccountPage
from MainPackage.ObjectsPages.Advantage_MainPage import Advantage_MainPage
from MainPackage.ObjectsPages.Advantage_OrderPayment_Actions import Advantage_OrderPayment_Actions
from MainPackage.ObjectsPages.Advantage_ProductPage import Advantage_ProductPage
from MainPackage.ObjectsPages.Advantage_ShoppingCart import Advantage_ShoppingCart
from MainPackage.ObjectsPages.Advantage_SignInPopUp import Advantage_SignInPopUp
from MainPackage.ObjectsPages.Advantage_ToolBar import Advantage_ToolBar

class TestCalcPage(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\selenium1\chromedriver.exe")

        # Open browser (create a driver object)
        self.driver = webdriver.Chrome(service=service_chrome)

        # Go to the required URL
        self.driver.get("https://advantageonlineshopping.com/#/")

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # Create an object for the Pages
        self.account_menu = Advantage_AccountOperationsMenu(self.driver)
        self.category_page = Advantage_CategoryPage(self.driver)
        self.product_page = Advantage_ProductPage(self.driver)
        self.main_page = Advantage_MainPage(self.driver)
        self.create_account_page = Advantage_CreateAccountPage(self.driver)
        self.order_actions = Advantage_OrderPayment_Actions(self.driver)
        self.cart_page = Advantage_ShoppingCart(self.driver)
        self.signin_page = Advantage_SignInPopUp(self.driver)
        self.toolbar = Advantage_ToolBar(self.driver)

    def test(self):
        pass