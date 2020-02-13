from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POMProject.Pages.login_page import LoginPage
from POMProject.Pages.home_page import HomePage
from POMProject.Pages.forgot_password_page import ForgotPassword
from POMProject.Pages.admin_page import AdminPage
import HtmlTestRunner


class LoginTest(unittest.TestCase):
    path = "/Users/AshaSatyakumar/Documents/Tools/WorkFolder/PyProject/POMProject/Utility/drivers/chromedriver"
    driver = webdriver.Chrome(executable_path=path)

    @classmethod  # class function is used, always provide the annotation classmethod.
    def setUpClass(cls):
        # cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")

    def test_01_login_invalid_password(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin1")
        login.click_login()
        login.invalid_credential_message()
        # message = login.invalid_credential_message()
        # self.assertEqual(message, "Invalid credentials")
        # self.driver.implicitly_wait(10)
        time.sleep(5)

    def test_02_login_invalid_username(self):
        driver = self.driver

        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()
        login.invalid_credential_message()
        # message = login.invalid_credential_message()
        # self.assertEqual(message, "Invalid credentials")
        # driver.implicitly_wait(10)
        time.sleep(5)

    def test_03_no_password(self):
        driver = self.driver

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("")
        login.click_login()
        login.no_password_message()
        # message = login.no_password_message()
        # self.assertEqual(message, "Password cannot be empty")
        time.sleep(5)

    def test_04_no_username(self):
        driver = self.driver

        login = LoginPage(driver)
        login.enter_username("")
        login.enter_password("admin")
        login.click_login()
        login.no_username_message()
        # message = login.no_username_message()
        # self.assertEqual(message, "Username cannot be empty")
        time.sleep(5)

    def test_05_forgot_password(self):
        driver = self.driver

        login = LoginPage(driver)
        login.forgot_password()
        time.sleep(5)

        forgot_password = ForgotPassword(driver)
        forgot_password.cancel_password()
    #
    def test_06_reset_password_valid(self):
        # message = "Please contact HR admin in order to reset the password" scenario,
        # yet to figure out how to write script to read the javascript message on browser
        driver = self.driver

        login = LoginPage(driver)
        login.forgot_password()
        time.sleep(5)

        forgot_password = ForgotPassword(driver)
        forgot_password.reset_password("Admin")
        time.sleep(5)
        forgot_password.cancel_password()

    def test_07_reset_password_invalid(self):
        # message "Could not find a user with given details" scenario,
        # yet to figure out how to write script to read the javascript message on browser
        driver = self.driver

        login = LoginPage(driver)
        login.forgot_password()
        time.sleep(5)

        forgot_password = ForgotPassword(driver)
        forgot_password.reset_password("")
        time.sleep(5)
        forgot_password.cancel_password()
    #
    # def test_08_login_valid(self):
    #     driver = self.driver
    #
    #     login = LoginPage(driver)
    #     login.enter_username("Admin")
    #     login.enter_password("admin123")
    #     login.click_login()
    #
    #     home = HomePage(driver)
    #     home.click_welcome()
    #     driver.implicitly_wait(10)
    #     home.click_logout()
    #     driver.implicitly_wait(10)
    #
    # # def test_09_admin_add_user_valid(self):
    # #     driver = self.driver
    # #
    # #     login = LoginPage(driver)
    # #     login.enter_username("Admin")
    # #     login.enter_password("admin123")
    # #     login.click_login()
    # #     time.sleep(3)
    # #     # Click on Admin Page
    # #     admin = AdminPage(driver)
    # #     admin.ap_admin_page_navigation()
    # #     time.sleep(2)
    # #     # Add new user
    # #     admin.ap_um_cancel_add_user("Fiona Yellow", "F15Grace", "Yellow123", "yellow123")
    # #     time.sleep(2)
    # #     print("User Added successfully")
    # #     time.sleep(5)
    #
    # # def test_10_admin_search_delete_user(self):
    # #     driver = self.driver
    # #
    # #     admin = AdminPage(driver)
    # #     time.sleep(2)
    # #     admin.ap_um_search_delete_user("F15Grace", "Fiona Yellow")
    # #     time.sleep(2)
    # #     # Need to add test scenario for no records found
    #
    # # def test_11_jobtitle_add(self):
    # #     driver = self.driver
    # #
    # #     # Click on Admin Page
    # #     admin = AdminPage(driver)
    # #     time.sleep(2)
    # #     admin.ap_jobtitle_cancel_add_jobtitle("test10")
    #     time.sleep(2)

    @classmethod  # class function is used, always provide the annotation classmethod.
    def tearDownClass(cls):
        print("Test Complete")
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    reports_path = "/Users/AshaSatyakumar/Documents/Tools/WorkFolder/PyProject/POMProject/Reports"
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=reports_path))
