from selenium.webdriver.common.by import By

from browser import Browser


class BasePage(Browser):
    # 1.URL
    URL = "https://the-internet.herokuapp.com/login"
    # 2.Selectorii pentru campuri / butoane
    USERNAME_LOC = (By.ID, "username")
    PASSWORD_LOC = (By.ID, "password")
    BUTTON_LOC = (By.CSS_SELECTOR, "button[class='radius']")

    # 3.Altii selectori

    # 4.Metodele
    # Navigarea catre URL
    def navigate_to_login(self):
        self.browser.get(self.URL)

    # Introdicem Username
    def input_username(self):
        self.browser.find_element(*self.USERNAME_LOC).send_keys("tomsmith")

    # Introducem password
    def input_password(self):
        self.browser.find_element(*self.PASSWORD_LOC).send_keys("SuperSecretPassword!")

    # Click pe login
    def click_login(self):
        self.browser.find_element(*self.BUTTON_LOC).click()
