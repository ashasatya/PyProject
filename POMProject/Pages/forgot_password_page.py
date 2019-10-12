
class ForgotPassword:

    def __init__(self,driver):

        self.driver = driver
        self.fp_username_textbox_id = "securityAuthentication_userName"
        self.fp_reset_button_id = "btnSearchValues"
        self.fp_cancel_button_id = "btnCancel"
        # LEARN These are Javascript tag, unable to select message and code.
        # self.fp_message1_text_xpath = "Please contact HR admin in order to reset the password"
        # self.fp_message2_text_xpath = "Could not find a user with given details"

    def reset_password(self, username):
            # self.driver.find_element_by_xpath(self.forgot_password_link_xpath).click()
        self.driver.find_element_by_id(self.fp_username_textbox_id).send_keys(username)
        self.driver.find_element_by_id(self.fp_reset_button_id).click()

    def cancel_password(self):
        self.driver.find_element_by_id(self.fp_cancel_button_id).click()
