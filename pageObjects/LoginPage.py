from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//button[@class='button-1 login-button']"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        # Clear the textbox from previous data
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        # Insert username
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        #Clear the textbox from previous data
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        # Insert password
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        # Click the login button
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        # Click the logout link text
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()





