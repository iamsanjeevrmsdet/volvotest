import pytest
from pages.facebook_login_page import FacebookLoginPage
from pages.facebook_friends_page import FacebookFriendsPage
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.usefixtures("setup")
class TestFacebookFriendsPage:
    
    def test_login_with_different_users(self, get_test_data):
        login_page = FacebookLoginPage(self.driver)
        friends_page = FacebookFriendsPage(self.driver)
        
        for data in get_test_data:
            try:
                # Perform login using data from the fixture
                login_page.enter_username(data["username"])
                login_page.enter_password(data["password"])
                login_page.click_login()

                # Check if login was successful by looking for an element unique to the logged-in state
                if login_page.is_login_successful():
                    # Navigate to Friends Page
                    friends_page.navigate_to_friends_page()

                    # Validate that the Friends page is loaded
                    assert friends_page.is_friends_page_loaded(), f"Failed to navigate to Friends page for user {data['username']}"
                else:
                    print(f"Login failed for user {data['username']}. Continuing with next credentials.")
            
            except NoSuchElementException as e:
                # Log the exception and continue with the next data set
                print(f"Error encountered for user {data['username']}: {str(e)}. Continuing with next credentials.")
            
            finally:
                # Optionally log out after each iteration to ensure the next login is fresh
                if login_page.is_login_successful():
                    login_page.logout()