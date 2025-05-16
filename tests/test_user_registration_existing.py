import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import CommonLocators, RegistrationPageLocators, UserInProfileLocators  # Убедитесь, что путь к файлу с локаторами верный


def test_register_logout_and_register_again(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(CommonLocators.LOGIN_REGISTER_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)
    ).click()

    email_user_1 = "user99896767689@example.com"  # Уникальный email для первого пользователя
    password_user_1 = "Password123!"  # Пароль для первого пользователя

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

    # Проверка, что поле email подсвечено ошибкой
    email_container = driver.find_element(*RegistrationPageLocators.INPUT_ERROR_CONTAINER_EMAIL)
    assert "input_inputerror" in email_container.get_attribute("class").lower()
