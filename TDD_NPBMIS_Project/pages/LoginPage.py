from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    page_header_xpath = "//div/p"
    email_field_id = "basic_email"
    password_field_id = "basic_password"
    login_button_css = "button.ant-btn"
    wrong_credentials_warning_message_xpath = "//div[contains(@class,'ant-message-error')]/span[2]"
    email_field_empty_warning_xpath = "//div[@id='basic_email_help']/div[1]"
    password_field_empty_warning_xpath = "//div[@id='basic_password_help']/div[1]"
    forgot_password_css = "a.whitespace-nowrap"

    def enter_email_address(self, email_address_text):
        self.type_into_element(email_address_text, "email_address_id", self.email_field_id)

    def enter_password(self, password_text):
        self.type_into_element(password_text, "password_field_id", self.password_field_id)

    def click_on_login_button(self):
        self.element_click("login_button_css", self.login_button_css)

    def login_to_application(self, email_address_text, password_text):
        self.enter_email_address(email_address_text)
        self.enter_password(password_text)
        return self.click_on_login_button()

    def get_page_title(self):
        page_title = self.retrieve_element_text("page_header_xpath", self.page_header_xpath)
        return page_title


    def wrong_credentials_warning_message(self):
        warning_message = self.retrieve_element_text("wrong_credentials_xpath",
                                                     self.wrong_credentials_warning_message_xpath)
        return warning_message

    def email_password_empty_warning_message(self):
        email_field_warning_text = self.retrieve_element_text("email_field_empty_xpath",
                                                              self.email_field_empty_warning_xpath)
        password_field_warning_text = self.retrieve_element_text("password_field_empty_xpath",
                                                                 self.password_field_empty_warning_xpath)
        warnings = [email_field_warning_text, password_field_warning_text]

        return warnings
