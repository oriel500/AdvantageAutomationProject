from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from MainPackage.ObjectsPages.Advantage_ToolBar import Advantage_ToolBar
from MainPackage.ObjectsPages.Advantage_MainPage import Advantage_MainPage
from MainPackage.ObjectsPages.Advantage_ProductPage import Advantage_ProductPage
from MainPackage.ObjectsPages.Advantage_OrderPayment_Actions import Advantage_OrderPayment_Actions
from MainPackage.ObjectsPages.Advantage_CreateAccountPage import Advantage_CreateAccountPage
from MainPackage.ObjectsPages.Advantage_AccountOperationsMenu import Advantage_AccountOperationsMenu
from MainPackage.ObjectsPages.Advantage_ShoppingCart import Advantage_ShoppingCart
from MainPackage.ObjectsPages.Advantage_CategoryPage import Advantage_CategoryPage
from MainPackage.ObjectsPages.Advantage_SignInPopUp import Advantage_SignInPopUp
from time import sleep


class TestAdvantage(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\Selenium1\chromedriver.exe")

        # Open browser (create a driver object)
        self.driver = webdriver.Chrome(service=service_chrome)

        # Go to the required URL
        self.driver.get('https://www.advantageonlineshopping.com/#/')

        self.driver.maximize_window()
        self.driver.implicitly_wait(60)

        self.toolbar = Advantage_ToolBar(self.driver)
        self.main = Advantage_MainPage(self.driver)
        self.product = Advantage_ProductPage(self.driver)
        self.account_op = Advantage_AccountOperationsMenu(self.driver)
        self.category = Advantage_CategoryPage(self.driver)
        self.cre_account = Advantage_CreateAccountPage(self.driver)
        self.order = Advantage_OrderPayment_Actions(self.driver)
        self.cart = Advantage_ShoppingCart(self.driver)
        self.signin = Advantage_SignInPopUp(self.driver)

    def test1_quantity_in_popup_cart(self):
        # List of category names
        cat_list = ['Headphones', 'Mice']

        product_index = 0
        qty = 2

        # Add two different products with different qty
        for i in cat_list:
            self.main.select_category(i)                            # Select category by name (cat_list)
            self.category.select_product(product_index)             # Select product by product index (product_index)
            self.product.select_quantity(qty)                       # Select quantity of product (qty)
            self.product.add_to_cart()                              # Add product to cart
            self.toolbar.click_logo()                               # Click Advantage logo to return to main page
            product_index += 1
            qty += 1

        # Number of products in the pop-up cart (by list)
        list_of_products_cart = self.toolbar.list_products()
        sum_qty = 0
        for i in range(len(list_of_products_cart)):
            product_qty = self.toolbar.get_qty_product_by_index(i)
            sum_qty += product_qty

        print(sum_qty)
        self.assertEqual(sum_qty, 5)

    def test3_remove_product_in_popup(self):
        cat_list = ['Laptops', 'Mice', 'Headphones']
        qty = 1

        # Add different products to cart
        for i in cat_list:
            self.main.select_category(i)
            self.category.select_product(0)
            self.product.select_quantity(qty)
            self.product.add_to_cart()
            self.toolbar.click_logo()
            qty += 1

        print(f'Number of products in cart is: {len(self.toolbar.list_products())}')
        # Delete a product from pop-up
        self.toolbar.remove_product_by_index(0)

        # List of new cart list
        self.assertNotEqual(len(self.toolbar.list_products()), 3)
        print(f'Number of products in cart after remove is: {len(self.toolbar.list_products())}')

    def test4_shopping_cart_page(self):
        self.main.select_category('Laptops')
        self.category.select_product(0)
        self.product.select_quantity(3)
        self.product.add_to_cart()

        self.toolbar.click_cart()           # Go to shopping cart page

        self.assertEqual(self.cart.shopping_cart_title_element().text, 'SHOPPING CART')

    def test5_products_prices_sum(self):
        # List of prices of the products (*qty)
        prices_list = []

        # List of names of the products
        product_names = []

        # List of qty
        qty_list = []

        cat_list = ['Laptops', 'Speakers', 'Headphones']
        qty = 1
        product_index = 0

        # Add different products with different qty to cart
        for i in cat_list:
            self.main.select_category(i)
            self.category.select_product(product_index)
            self.product.select_quantity(qty)
            self.product.add_to_cart()
            qty_list.append(qty)
            prices_list.append(self.product.get_price()*qty)
            product_names.append(self.category.select_product(product_index).text)
            qty += 1
            product_index += 1
            self.toolbar.click_logo()

        self.toolbar.click_cart()               # Go to shopping cart page
        print(f'Name: {product_names[0]}, Qty: {qty_list[0]}, Price: {prices_list[0]}')
        print("----------")
        print(f'Name: {product_names[1]}, Qty: {qty_list[1]}, Price: {prices_list[1]}')
        print("----------")
        print(f'Name: {product_names[2]}, Qty: {qty_list[2]}, Price: {prices_list[2]}')
        print("----------")
        print(f'Total price is: {sum(prices_list)}')
        self.assertEqual(sum(prices_list), self.cart.total_price())

    def test6_edit_qty_of_products(self):
        cat_list = ['Laptops', 'Mice', 'Headphones']
        # Add different products to cart
        for i in cat_list:
            self.main.select_category(i)
            self.category.select_product(0)
            self.product.select_quantity(1)
            self.product.add_to_cart()

        # self.toolbar.click_cart()
        # edit
        # self.product.select_quantity(qty+)
        # AssertEqual Quantity of products to qty