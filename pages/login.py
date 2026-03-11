from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.username_input = "//input[@id='username']"
        self.password_input = "//input[@id='password']"
        self.login_button = "//button[@id='submit']"
        self.verify_message = "//h1[normalize-space()='Logged In Successfully']"

        

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def verify_login_successful(self):
        assert self.page.is_visible(self.verify_message), "Login was not successful"
        