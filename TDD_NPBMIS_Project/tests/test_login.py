import time

import pytest
from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest
from utilities import ReadConfigurations



@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin(BaseTest):


    email = ReadConfigurations.read_configuration("basic info", "email")
    password = ReadConfigurations.read_configuration("basic info", "password")
    emails = eval(ReadConfigurations.read_configuration("email info", "email_variants"), {}, {})



    def test_login_with_valid_credentials(self):
        self.dashboard_page = DashboardPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.login_page.login_to_application(self.email, self.password)
        assert self.dashboard_page.presence_of_user_icon_avatar, "dashbaord" in self.dashboard_page.get_current_url()


    def test_login_with_invalid_credentials(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_to_application(self.generate_email_with_time_stamp(), "wrongpassword")
        assert "User not found!" in self.login_page.wrong_credentials_warning_message()

    def test_login_with_valid_email_and_invalid_password(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_to_application(self.email, "wrongpassword")
        assert "Password doesn't match" in self.login_page.wrong_credentials_warning_message()

    def test_login_with_invalid_email_and_valid_password(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_to_application(self.generate_email_with_time_stamp(),self.password)
        assert "User not found!" in self.login_page.wrong_credentials_warning_message()

    def test_password_not_visible_to_pagesource(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.enter_password("passwordcheck")
        assert "passwordcheck" not in self.driver.page_source

    def test_login_with_empty_fields(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_to_application("", "")
        assert "login" in self.driver.current_url


    @pytest.mark.xfail
    @pytest.mark.parametrize("email_variant", emails)
    def test_EmailaddressfieldisnotCaseSensitive(self, email_variant):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_to_application(email_variant)
        assert self.dashboard_page.presence_of_user_icon_avatar()
        assert "dashboard" in self.driver.current_url

    def test_Verify_warning_messages(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_to_application("", "")
        warnings = self.login_page.email_password_empty_warning_message()
        assert "कृपया आफ्नो इमेल प्रविष्ट गर्नुहोस्।" in warnings[0]
        assert "कृपया आफ्नो पासवर्ड प्रविष्ट गर्नुहोस्।" in warnings[1]

    @pytest.mark.check
    def test_user_is_navigated_back_to_login_page_when_clicking_on_back_button(self):
        self.dashboard_page = DashboardPage(self.driver)
        self.login_page.login_to_application(self.email, self.password)
        self.dashboard_page.presence_of_user_icon_avatar()
        self.driver.back()
        assert "सूचना व्यवस्थापन प्रणाली" in self.login_page.get_page_title()

    def test_all_hyperlinks_are_working_properly(self):
        self.login_page = LoginPage(self)
        self.login_page.get_element()