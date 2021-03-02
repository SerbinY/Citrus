from selenium.webdriver.common.by import By



class MainPageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.user-actions .link-to')
    EMAIL_LOGIN_BUTTON = (By.CSS_SELECTOR, '.custom-button.custom-button.custom-button--secondary.identity__switch')
    INPUT_USER_EMAIl = (By.CSS_SELECTOR, 'input[name="email"]')
    EMAIL_NEXT_BUTTON = (By.CSS_SELECTOR, '.custom-button.custom-button.custom-button--primary.identity__submit')
    INPUT_USER_PASSWORD = (By.CSS_SELECTOR, '[name="password"]')
    PASSWORD_NEXT_BUTTON = (By.CSS_SELECTOR, '.custom-button.custom-button--primary.email-login__submit')
    WELLCOME_TEXT = (By.CSS_SELECTOR, '.auth')

