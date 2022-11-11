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
# delete in done
from time import sleep


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

    def test2_products_cart_popup(self):
        category_list = ['Speakers', 'Tablets', 'Mice']
        product_index_list = [0, 1, 2]
        qty_list = [3, 2, 1]

        for i in range(3):
            # enter to product
            self.main_page.select_category(category_list[i])
            self.category_page.select_product(product_index_list[i])

            # get details from product page
            name_product_page = self.product_page.product_name_element()
            color_product_page = self.product_page.choose_first_color()
            qty_product_page = qty_list[i]
            price_product_page = self.product_page.get_price()*qty_list[i]

            # add to cart
            self.product_page.select_quantity(qty_product_page)
            self.product_page.add_to_cart()
            self.toolbar.click_logo()

            # get details of product from cart popup window
            name_toolbar = self.toolbar.get_name_product_by_index(0)
            color_toolbar = self.toolbar.get_color_product_by_index(0)
            qty_toolbar = self.toolbar.get_qty_product_by_index(0)
            price_toolbar = self.toolbar.get_price_product_by_index(0)

            # check if the details from product equal to details from cart popup window
            self.assertEqual(name_product_page, name_toolbar)
            self.assertEqual(color_product_page, color_toolbar)
            self.assertEqual(qty_product_page, qty_toolbar)
            self.assertEqual(price_product_page, price_toolbar)

    def test7_check_navigate_backward(self):
        # enter to product
        self.main_page.select_category('Tablets')
        self.category_page.select_product(0)

        # click in navigation line on tablets
        self.product_page.back_to_tablets_category()

        title_category = self.category_page.category_title()
        self.assertEqual(title_category, "TABLETS")

        # click in navigation line on home
        self.category_page.back_to_main_page()

        # check if the function success to locate mice element
        self.assertTrue(self.main_page.mice_element())

    def test8_order_by_safepay_with_new_user(self):
        # create new user and logout
        username = "test0002"
        password = "Aabc12"
        email = "a@gmail.com"
        self.toolbar.click_user()
        self.signin_page.click_create_account()
        self.create_account_page.register(username, email, password)
        self.toolbar.click_user()
        self.account_menu.logout()

        # lists for data to pick a products
        category_list = ['Speakers', 'Mice']
        product_index_list = [1, -1]
        qty_list = [5, 2]

        # add to cart products
        for i in range(len(product_index_list)):
            # enter to product
            self.main_page.select_category(category_list[i])
            self.category_page.select_product(product_index_list[i])

            # add to cart
            self.product_page.select_quantity(qty_list[i])
            self.product_page.add_to_cart()
            self.toolbar.click_logo()

        # navigate to checkout
        self.toolbar.click_cart_checkout_popup()

        # login to new user
        self.order_actions.login_from_order_payment(username, password)

        # pay by safepay
        self.order_actions.click_next()
        self.order_actions.pay_now_by_safepay(username, password)
        # check if the function success to locate order number element
        self.assertTrue(self.order_actions.order_number_from_thankYou_page())
        # save the order number from thank you page
        order_id_from_thank_you_page = self.order_actions.order_number_from_thankYou_page()

        # check if the cart empty
        self.toolbar.click_cart()
        self.assertTrue(self.cart_page.is_empty())

        # navigate to my orders page
        self.toolbar.click_user()
        self.account_menu.click_my_orders()
        # save the order number from my orders page
        order_id_from_orders_page = self.order_actions.get_id_last_order()

        # check if the order number from thank you page equal to order number from my orders page
        self.assertEqual(order_id_from_thank_you_page, order_id_from_orders_page)

        # delete new user
        self.toolbar.click_user()
        self.account_menu.delete_account()

    def test9_order_by_master_with_exist_user(self):
        pass

    def test10_login_logout(self):
        username = "test0001"
        password = "Aabc12"

        self.toolbar.click_user()
        self.signin_page.sign_in(username, password)
        self.assertEqual(self.toolbar.get_name_user_icon(), username)

        self.toolbar.click_user()
        self.account_menu.logout()
        self.assertEqual(self.toolbar.get_name_user_icon(), '')
