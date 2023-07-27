from features.pages.BasePage import BasePage
from features.pages.DashboardPage import DashboardPage
from selenium.webdriver.common.alert import Alert

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    email_address_field_id = "basic_email"
    password_field_id = "basic_password"
    login_button_css_selector = "button[type='submit']"

    def enter_email_address(self, email_text):
        self.type_into_element("email_address_field_id", self.email_address_field_id, email_text)

    def enter_password(self, password_text):
        self.type_into_element("password_field_id", self.password_field_id, password_text)

    def click_on_login_button(self):
        self.click_on_element("login_button_css_selector", self.login_button_css_selector,)
        return DashboardPage(self.driver)

    def display_status_of_warning_message(self, expected_warning_text):
        return self.verify_alert_message(expected_warning_text)