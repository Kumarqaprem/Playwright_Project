from pages.login import LoginPage


def test_login(page):
    login_page = LoginPage(page)

    login_page.login("student", "Password123")

