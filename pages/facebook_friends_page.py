from selenium.webdriver.common.by import By

class FacebookFriendsPage:
    def __init__(self, driver):
        self.driver = driver
        self.friends_header = (By.XPATH, "//h2[text()='Friends']")

    def navigate_to_friends_page(self):
        self.driver.get("https://www.facebook.com/friends")

    def is_friends_page_loaded(self):
        return self.driver.find_element(*self.friends_header).is_displayed()
