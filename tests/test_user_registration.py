import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import helpers
from locators import CommonLocators, RegistrationPageLocators, UserInProfileLocators


class TestUserRegistration:

    def test_user_registration(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(CommonLocators.LOGIN_REGISTER_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)
        ).click()

        email = f"user_{int(time.time())}@test.com"
        password = "StrongPassword123!"

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_INPUT)
        ).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)

        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(CommonLocators.PLACE_AD_BUTTON)
        )

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(CommonLocators.USER_AVATAR)
        )
        assert driver.find_element(*CommonLocators.USER_NAME).is_displayed()

    def test_register_existing_email(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(CommonLocators.LOGIN_REGISTER_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)
        ).click()

        email_user_1 = helpers.Helpers.generate_random_email()
        password_user_1 = "Password123!"

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_INPUT)
        ).send_keys(email_user_1)

        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password_user_1)
        driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(password_user_1)

        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(UserInProfileLocators.LOGOUT_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(CommonLocators.LOGIN_REGISTER_BUTTON)

        )

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(CommonLocators.LOGIN_REGISTER_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_INPUT)
        ).send_keys(email_user_1)

        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password_user_1)
        driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(password_user_1)

        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        error_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_ERROR_MESSAGE)
        )
        assert "Ошибка" in error_msg.text

        email_container = driver.find_element(*RegistrationPageLocators.INPUT_ERROR_CONTAINER_EMAIL)
        assert "input_inputerror" in email_container.get_attribute("class").lower()

    def test_invalid_email_registration(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(CommonLocators.LOGIN_REGISTER_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)
        ).click()

        invalid_email = "invalid-email"
        password = "SomePassword123!"

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_INPUT)
        ).send_keys(invalid_email)

        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)

        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        email_error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_ERROR_MESSAGE)
        )
        assert "Ошибка" in email_error.text

        email_error_container = driver.find_element(*RegistrationPageLocators.INPUT_ERROR_CONTAINER_EMAIL)
        password_error_container = driver.find_element(*RegistrationPageLocators.INPUT_ERROR_CONTAINER_PASSWORD)
        confirm_error_container = driver.find_element(*RegistrationPageLocators.INPUT_ERROR_CONTAINER_SUBMIT_PASSWORD)

        assert "input_inputerror" in email_error_container.get_attribute("class").lower()
        assert "input_inputerror" in password_error_container.get_attribute("class").lower()
        assert "input_inputerror" in confirm_error_container.get_attribute("class").lower()