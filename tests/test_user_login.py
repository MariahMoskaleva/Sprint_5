import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import CommonLocators, RegistrationPageLocators, UserInProfileLocators


class TestUserLogin:

    def test_register_and_login(self, driver):
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

        driver.find_element(*UserInProfileLocators.PROFILE_BUTTON).click()
        wait.until(EC.element_to_be_clickable(UserInProfileLocators.LOGOUT_BUTTON)).click()

        wait.until(EC.presence_of_element_located(CommonLocators.LOGIN_REGISTER_BUTTON))

        login_button = driver.find_element(*CommonLocators.LOGIN_REGISTER_BUTTON)
        wait.until(EC.element_to_be_clickable(CommonLocators.LOGIN_REGISTER_BUTTON))
        login_button.click()

        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)

        login_button = driver.find_element(*CommonLocators.LOGIN_BUTTON)
        wait.until(EC.element_to_be_clickable(CommonLocators.LOGIN_BUTTON))
        login_button.click()

        avatar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(CommonLocators.USER_AVATAR)
        )
        assert avatar.is_displayed()
