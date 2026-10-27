from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = '#user-name'
    PASSWORD_INPUT = '#password'
    LOGIN_BUTTON = '#login-button'
    ERROR_MESSAGE = '[data-test="error"]'
    PRODUCT_TITLE = '.title'

    def __init__(self, page):
        super().__init__(page, 'https://www.saucedemo.com/')

    def enter_username(self, username):
        self.page.locator(self.USERNAME_INPUT).fill(username)

    def enter_password(self, password):
        self.page.locator(self.PASSWORD_INPUT).fill(password)

    def click_login(self):
        self.page.locator(self.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def login_as_standard_user(self):
        self.login('standard_user', 'secret_sauce')

    def get_error_message(self):
        return self.page.locator(self.ERROR_MESSAGE).text_content()

    def is_error_visible(self):
        return self.page.locator(self.ERROR_MESSAGE).is_visible()

    def is_logged_in(self):
        if not self.page.url.endswith('/inventory.html'):
            return False

        try:
            self.page.locator(self.PRODUCT_TITLE).wait_for(state='visible', timeout=10000)
            return True
        except Exception:
            return False
