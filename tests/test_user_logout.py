import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import CommonLocators, RegistrationPageLocators, UserInProfileLocators


class TestUserLogout:

    def test_register_and_login_and_logout(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(CommonLocators.LOGIN_REGISTER_BUTTON)).click()

        wait.until(EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)).click()

        timestamp = str(int(time.time()))
        email = f"user_{timestamp}@example.com"
        password = "Password123!"

        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)

        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        wait.until(EC.visibility_of_element_located(UserInProfileLocators.USER_AVATAR))

        wait.until(EC.element_to_be_clickable(UserInProfileLocators.LOGOUT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(CommonLocators.LOGIN_REGISTER_BUTTON))

        assert driver.find_element(*CommonLocators.LOGIN_REGISTER_BUTTON).is_displayed()
