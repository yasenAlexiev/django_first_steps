from playwright.sync_api import Page
from allauth.account.models import EmailAddress

from tests.pages.auth import SignupPage
from app.models import UserProfile


def test_signup(page: Page, user_data: dict):
    page.goto("/")
    signup_page = SignupPage(page)
    signup_page.complete_signup_form(user_data["email"], user_data["password"])

    user = UserProfile.objects.get(email=user_data["email"])
    email_address = EmailAddress.objects.get(user=user, email=user_data["email"])
    assert email_address.verified
