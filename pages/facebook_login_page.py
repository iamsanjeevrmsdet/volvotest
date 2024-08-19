from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class FacebookLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "email")
        self.password_field = (By.ID, "pass")
        self.login_button = (By.NAME, "login")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def is_login_successful(self):
        # Check for an element unique to a successful login
        try:
            self.driver.find_element(By.ID, "profile_icon")  # Example element
            return True
        except NoSuchElementException:
            return False

    def logout(self):
        # Implement logout logic to reset the session
        try:
            self.driver.find_element(By.ID, "logout_button").click()  # Example element
        except NoSuchElementException:
            print("Logout button not found.")
