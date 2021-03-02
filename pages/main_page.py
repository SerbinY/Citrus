from .base_page import BasePage
from .locators import MainPageLocators
import time


class MainPage(BasePage):
    def user_should_see_welcome_text_after_login(self):
        self.browser.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        self.browser.find_element(*MainPageLocators.EMAIL_LOGIN_BUTTON).click()
        self.browser.find_element(*MainPageLocators.INPUT_USER_EMAIl).send_keys('yevgenserbin@gmail.com')
        self.browser.find_element(*MainPageLocators.EMAIL_NEXT_BUTTON).click()
        self.browser.find_element(*MainPageLocators.INPUT_USER_PASSWORD).send_keys('123456')
        self.browser.find_element(*MainPageLocators.PASSWORD_NEXT_BUTTON).click()
        time.sleep(5)
        wellcome_text = self.browser.find_element(*MainPageLocators.WELLCOME_TEXT).text
        assert 'Женя Сербин' in wellcome_text, 'Wellcome text is not displaed'





#        self.browser.find_element(*LoginPageLocators.INPUT_USER_NAME).send_keys('Serbin')
 #       self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys('123456')
  #      wellcome_text = self.browser.find_element(*LoginPageLocators.WELLCOME_TEXT).text
   #     assert 'Hello, Serbin' in wellcome_text, 'Wellcome text is not displaed'




