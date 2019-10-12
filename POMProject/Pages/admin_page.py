class AdminPage:

    def __init__(self, driver):
        self.driver = driver
        self.admin_contextualmenu_xpath = "//a[@id='menu_admin_viewAdminModule']/b[.='Admin']"
        self.ap_username_textbox_id = "searchSystemUser_userName"
        self.ap_UserRole_dropdownmenu_id = "searchSystemUser_userType"
        self.ap_EmployeeName_textbox_id = "searchSystemUser_employeeName_empName"
        self.ap_status_dropdownmenu_id = "searchSystemUser_status"
        self.ap_search_button_id = "searchBtn"
        self.ap_reset_button_id = "resetBtn"
        self.ap_add_button_id = "btnAdd"
        self.ap_delete_button_id = "btnDelete"
        self.adduser_empname_textbox_id = "systemUser_employeeName_empName"
        self.adduser_username_textbox_id = "systemUser_userName"
        self.adduser_password_textbox_id = "systemUser_password"
        self.adduser_confirmpassword_textbox_id = "systemUser_confirmPassword"
        self.adduser_save_buttton_id = "btnSave"
        self.adduser_cancel_button_id = "btnCancel"
        self.ap_selectall_checkbox_xpath = "/html//input[@id='ohrmList_chkSelectAll']"
        self.modal_ok_button_id = "dialogDeleteBtn"
        self.ap_norecord_text_xpath = "/html//table[@id='resultTable']//td[.='No Records Found']"

    def ap_admin_page_navigation(self):
        self.driver.find_element_by_xpath(self.admin_contextualmenu_xpath).click()

    def ap_search_user(self, username, employee_name):
        self.driver.find_element_by_xpath(self.admin_contextualmenu_xpath).click()
        self.driver.find_element_by_id(self.ap_username_textbox_id).send_keys(username)
        # self.driver.find_element_by_id(self.ap_UserRole_dropdownmenu_id).is_selected(user_role)
        self.driver.find_element_by_id(self.ap_EmployeeName_textbox_id).send_keys(employee_name)
        # self.driver.find_element_by_id(self.ap_status_dropdownmenu_id).is_selected(status)
        if
        self.driver.find_element_by_id(self.ap_search_button_id).click()

    def ap_add_user(self, empname, username, password, confirm_password):
        self.driver.find_element_by_id(self.ap_add_button_id).click()
        self.driver.find_element_by_id(self.adduser_empname_textbox_id).send_keys(empname)
        self.driver.find_element_by_id(self.adduser_username_textbox_id).send_keys(username)
        self.driver.find_element_by_id(self.adduser_password_textbox_id).send_keys(password)
        self.driver.find_element_by_id(self.adduser_confirmpassword_textbox_id).send_keys(confirm_password)
        self.driver.find_element_by_id(self.adduser_save_buttton_id).click()

    def ap_add_user_cancel(self, empname, username, password, confirm_password):
        self.driver.find_element_by_id(self.ap_add_button_id).click()
        self.driver.find_element_by_id(self.adduser_empname_textbox_id).send_keys(empname)
        self.driver.find_element_by_id(self.adduser_username_textbox_id).send_keys(username)
        self.driver.find_element_by_id(self.adduser_password_textbox_id).send_keys(password)
        self.driver.find_element_by_id(self.adduser_confirmpassword_textbox_id).send_keys(confirm_password)
        self.driver.find_element_by_id(self.adduser_cancel_button_id).click()

    def ap_delete_user(self):
        self.driver.find_element_by_xpath(self.ap_selectall_checkbox_xpath).click()
        self.driver.find_element_by_id(self.ap_delete_button_id).click()
        self.driver.find_element_by_id(self.modal_ok_button_id).click()





