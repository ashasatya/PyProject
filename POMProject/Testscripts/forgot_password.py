from selenium import webdriver
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
# from POMProject.Pages.login_page import LoginPage

path = "/Users/AshaSatyakumar/Documents/Tools/WorkFolder/PyProject/POMProject/Utility/drivers/chromedriver"
driver = webdriver.Chrome(executable_path=path)

driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/index.php")
time.sleep(1)
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
time.sleep(2)
driver.find_element_by_xpath("//b[contains(text(),'Admin')").click()
driver.find_element_by_id("searchSystemUser_userName").send_keys("test123")
driver.find_element_by_id("searchSystemUser_userType").is_selected("ESS")
driver.find_element_by_id("searchSystemUser_employeeName_empName").send_keys("Apolo Sr")
driver.find_element_by_id("searchSystemUser_status").is_selected("Enabled")
driver.find_element_by_id("btnAdd").click()
time.sleep(5)
print("Test Complete")



