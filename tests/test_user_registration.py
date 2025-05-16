from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import CommonLocators, RegistrationPageLocators
import time


def test_user_registration(driver):
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
