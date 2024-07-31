from behave import *


@given('I am login page')
def step_impl(context):
    context.login_page.navigate_to_login()


@when('I introduce the valid username')
def step_impl(context):
    context.login_page.input_username()


@when('I introduce the valid password')
def step_impl(context):
    context.login_page.input_password()


@when('I clicked the login button')
def step_impl(context):
    context.login_page.click_login()


@then('I am in secure area')
def step_impl(context):
    current_text = context.login_page.return_mesage()
    expected_text = "You logged into a secure area!"
    # print(current_text)
    # print(expected_text)
    # Comparam egalitate exacta intre curent_text si expected_text
    # caractere, saptii , enter, toate trebuie sa fie exact la fel
    # assert current_text == expected_text
    # folosim cuvantul cheie in verificam existenta textului
    # expected in string returnat de curent_text
    assert expected_text in current_text


@then('I am on a new page')
def step_impl(context):
    current_url = context.login_page.return_current_url()
    expected_url = "https://the-internet.herokuapp.com/secure"
    assert current_url == expected_url


@when(u'I use an invalid "{username}" and "{password}"')
def step_impl(context, username, password):
    context.login_page.input_username_param(username)
    context.login_page.input_password_param(password)


@then(u'I should remain on the login page')
def step_impl(context):
    current_url = context.login_page.return_current_url()
    expected_url = "https://the-internet.herokuapp.com/login"
    assert current_url == expected_url

