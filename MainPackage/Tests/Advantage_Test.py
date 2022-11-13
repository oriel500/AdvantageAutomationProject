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


class AdvantageTest(TestCase):
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

    def test1_quantity_in_popup_cart(self):
        # After select at least 2 products with different quantities >>
        # >> The test will check that the correct quantity appear in the pop-up cart.

        # List of category names that the test will go into
        cat_list = ['Headphones', 'Mice']
        product_index = 0                                        # Index of the product in the category page
        qty = 2                                                  # Qty of the selected product

        # Add two different products with different qty
        for i in cat_list:
            self.main_page.select_category(i)                    # Select category by name (cat_list)
            self.category_page.select_product(product_index)     # Select product by product index (product_index)
            self.product_page.select_quantity(qty)               # Select quantity of product (qty)
            self.product_page.add_to_cart()                      # Add product to cart
            self.toolbar.click_logo()                            # Click Advantage logo to return to main page
            product_index += 1
            qty += 1

        # Number of products in the pop-up cart (by list)
        list_of_products_cart = self.toolbar.list_products()
        sum_qty = 0

        # Check the number of the qty in the list (pop-up cart)
        for i in range(len(list_of_products_cart)):
            product_qty = self.toolbar.get_qty_product_by_index(i)
            sum_qty += product_qty

        print(sum_qty)
        self.assertEqual(sum_qty, 5)

    # check if the details from product equal to details from cart popup window
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

    def test3_remove_product_in_popup(self):
        # After select at least 2 products with different quantities >>
        # >> Remove one product with the pop-up cart and test if it's disappeared

        # List of category names that the test will go into
        cat_list = ['Laptops', 'Mice', 'Headphones']

        # Add different products to cart
        for i in cat_list:
            self.main_page.select_category(i)                   # Select category by name (cat_list)
            self.category_page.select_product(0)                # Select product by product index (product_index)
            self.product_page.select_quantity(1)                # Quantity of the product
            self.product_page.add_to_cart()                     # Add product to cart
            self.toolbar.click_logo()                           # Click Advantage logo to return to main page

        # Check that there is 3 products in the list
        self.assertEqual(len(self.toolbar.list_products()), 3)
        print(f'Number of products in cart is: {len(self.toolbar.list_products())}')

        # Remove one product from pop-up list
        self.toolbar.remove_product_by_index(0)

        # List of the new cart list
        print(f'Number of products in cart after remove is: {len(self.toolbar.list_products())}')

        # Check that there is 2 products in the list
        self.assertEqual(len(self.toolbar.list_products()), 2)

    def test4_shopping_cart_page(self):
        # After select one product and enter the shopping cart page >>
        # The test will check if you are in the shopping cart page.

        self.main_page.select_category('Laptops')                        # Select category by name
        self.category_page.select_product(0)                             # Select product by index
        self.product_page.select_quantity(3)                             # Quantity of the product
        self.product_page.add_to_cart()                                  # Add product to cart
        self.toolbar.click_cart()                                        # Go to shopping cart page

        self.assertEqual(self.cart_page.shopping_cart_title_element().text, 'SHOPPING CART')

    def test5_products_prices_sum(self):
        # After select 3 products with different quantities and enter the shopping cart page >>
        # The test will check if the total price equal to the price while selecting the products.

        # List of category names that the test will go into
        cat_list = ['Laptops', 'Speakers', 'Headphones']
        product_index = 0                                                 # Index of the product in the category page
        qty = 1                                                           # Qty of the selected product

        # List of prices of the products (*qty)
        prices_list = []

        # Add different products with different qty to cart
        for i in cat_list:
            self.main_page.select_category(i)                            # Select category by name
            self.category_page.select_product(product_index)             # Select product by index
            self.product_page.select_quantity(qty)                       # Quantity of the product
            self.product_page.add_to_cart()                              # Add product to cart

            # Print details of the selected product
            print(f'''
            Product Name: {self.product_page.product_name_element()}
            Quantity: {qty}
            Total Product Price: {self.product_page.get_price()*qty}''')

            # Add product price (when choosing) to relevant list
            prices_list.append(self.product_page.get_price()*qty)
            qty += 1
            product_index += 1
            self.toolbar.click_logo()                                    # Back to main page

        self.toolbar.click_cart()                                        # Go to shopping cart page
        self.assertEqual(sum(prices_list), self.cart_page.total_price())

    def test6_edit_qty_of_products(self):
        # After select at least 2 products, enter the shopping cart page and edit the quantities >>
        # The test will check if the changes appear in the shopping cart page.

        # List of category names that the test will go into
        cat_list = ['Laptops', 'Mice']

        # Add different products to cart
        for i in cat_list:
            self.main_page.select_category(i)                            # Select category by name
            self.category_page.select_product(0)                         # Select product by index
            self.product_page.select_quantity(1)                         # Quantity of the product
            self.product_page.add_to_cart()                              # Add product to cart
            self.toolbar.click_logo()                                    # Back to main page

        self.toolbar.click_cart()                                        # Go to shopping cart page

        index = 0
        for z in range(2):
            self.cart_page.edit_product_by_rowIndex(index)
            self.product_page.select_quantity(2)
            self.product_page.add_to_cart()
            self.toolbar.click_cart()
            index += 1

        self.toolbar.click_cart()                                        # Go to shopping cart page
        self.assertEqual((self.cart_page.product_qty_by_rowIndex(0)+self.cart_page.product_qty_by_rowIndex(1)), 4)

        # There is a bug!

    # check if the text "tables" on the navigation line navigate backward to tablets category and after this
    # navigate to main page with the text "home" on the navigation line
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

    # check if I can pay with new user by safepay method
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
            # enter to category
            self.main_page.select_category(category_list[i])
            # enter to product
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

    # check if I can pay with new user by master credit method
    def test9_order_by_master_with_new_user(self):
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
        category_list = ['Laptops', 'Headphones']
        product_index_list = [3, 0]
        qty_list = [1, 2]

        # add to cart products
        for i in range(len(product_index_list)):
            # enter to category
            self.main_page.select_category(category_list[i])
            # enter to product
            self.category_page.select_product(product_index_list[i])

            # add to cart
            self.product_page.select_quantity(qty_list[i])
            self.product_page.add_to_cart()
            self.toolbar.click_logo()

        # navigate to checkout
        self.toolbar.click_cart_checkout_popup()

        # login to new user
        self.order_actions.login_from_order_payment(username, password)

        # pay by master card
        self.order_actions.click_next()
        self.order_actions.pay_now_by_master_credit("123412341234", "123", "Oriel", "02", "2023")
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

    # check if I can log in to user and logout
    def test10_login_logout(self):
        username = "test0001"
        password = "Aabc12"

        self.toolbar.click_user()
        self.signin_page.sign_in(username, password)
        # check if the username equal to text next to user icon
        self.assertEqual(self.toolbar.get_name_user_icon(), username)

        self.toolbar.click_user()
        self.account_menu.logout()
        # check if the text next to user icon is empty
        self.assertEqual(self.toolbar.get_name_user_icon(), '')
