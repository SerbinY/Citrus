from pages.main_page import MainPage




def test_login_form(browser):
    link = "https://www.citrus.ua/"
    page = MainPage (browser,link)
    page.open()
    page.user_should_see_welcome_text_after_login()



