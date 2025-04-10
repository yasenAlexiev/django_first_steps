from playwright.sync_api import Page


class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator('input[type="email"]')
        self.password_input = page.locator('input[type="password"]')
        self.signup_button = page.locator('button[type="submit"]')
    
    def complete_signup_form(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.signup_button.click()

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_field = page.get_by_placeholder("Email")
        self.password_field = page.get_by_placeholder("Password")
        self.signup_button = page.get_by_role("button", name="Sign in")


class ConfirmationPage:
    def __init__(self, page: Page):
        self.page = page
        self.confirm_button = page.get_by_role("button")
