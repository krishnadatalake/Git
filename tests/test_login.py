from pages.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login_as_standard_user()

    assert login_page.is_logged_in() is True
    assert page.locator(login_page.PRODUCT_TITLE).text_content().strip() == 'Products'

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login('standard_user', 'wrong_password')

    assert login_page.is_error_visible() is True
    assert 'Username and password do not match any user in this service' in login_page.get_error_message()

def test_locked_out_user(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login('locked_out_user', 'secret_sauce')

    assert login_page.is_error_visible() is True
    assert 'Sorry, this user has been locked out.' in login_page.get_error_message()
