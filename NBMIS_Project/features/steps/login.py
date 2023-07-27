from behave import *
from features.pages.LoginPage import LoginPage
from utilities import EmailWithTimeStampGenerator


@given(u'I navigated to Login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    assert context.login_page.verify_page_url("login")

@when(u'I enter valid email as "{email}" and valid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'I click on Login button')
def step_impl(context):
    context.login_page.click_on_login_button()


@then(u'I should get logged in')
def step_impl(context):
    assert context.login_page.verify_page_url("dashboard")


@when(u'I enter invalid email and valid password say "{password}" into the fields')
def step_impl(context, password):
    invalid_email = EmailWithTimeStampGenerator.get_new_email_with_timestamp()
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password(password)


@then(u'I should get a proper warning message')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.display_status_of_warning_message("User not found!")



@when(u'I enter valid email say "{email}" and invalid password say "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'I enter invalid email and invalid password say "{password}" into the fields')
def step_impl(context, password):
    invalid_email = EmailWithTimeStampGenerator.get_new_email_with_timestamp()
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password(password)


@when(u'I dont enter anything into email and password fields')
def step_impl(context):
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")

