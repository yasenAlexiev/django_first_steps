from playwright.sync_api import Page

class SignInPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.get_by_placeholder("Email address")
        self.password_input = page.get_by_placeholder("Password")
        self.sign_in_button = page.get_by_role("button", name="Create your account")


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.get_by_placeholder("Email address")
        self.password_input = page.get_by_placeholder("Password")
        self.sign_in_button = page.get_by_role("button", name="Sign in")


class ConfirmationPage:
    def __init__(self, page: Page):
        self.page = page
        self.confirmation_button = page.get_by_role("button")
