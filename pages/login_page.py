from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    MESAGE_LOC = (By.ID, "flash")

    def return_mesage(self):
        e_mesage = self.browser.find_element(*self.MESAGE_LOC)
        # t_mesage = e_mesage.get_attribute("text")
        t_mesage = e_mesage.text
        # print(f"login:page{t_mesage}")
        return t_mesage

    def return_current_url(self):
        return self.browser.current_url

    def input_username_param(self, username):
        self.browser.find_element(*self.USERNAME_LOC).send_keys(username)

    def input_password_param(self, password):
        self.browser.find_element(*self.PASSWORD_LOC).send_keys(password)
