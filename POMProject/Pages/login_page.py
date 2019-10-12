class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"
        self.invalid_credential_message_xpath = "//span[@id='spanMessage']"
        self.NoUsername_message_xpath = "//span[@id='spanMessage']"
        self.NoPassword_message_xpath = "//span[@id='spanMessage']"
        # self.forgot_password_link_xpath = "/div[@id='forgotPasswordLink"
        self.forgot_password_link_xpath = " //a[contains(text(),'?')]"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def invalid_credential_message(self):
        msg = self.driver.find_element_by_xpath(self.invalid_credential_message_xpath).text
        return msg

    def no_username_message(self):
        msg = self.driver.find_element_by_xpath(self.NoUsername_message_xpath).text
        return msg

    def no_password_message(self):
        msg = self.driver.find_element_by_xpath(self.NoPassword_message_xpath).text
        return msg

    def forgot_password(self):
        self.driver.find_element_by_xpath(self.forgot_password_link_xpath).click()



