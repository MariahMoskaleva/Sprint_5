import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import helpers
import urls
from locators import (
    AdCreationLocators,
    AuthRequiredLocators,
    CommonLocators,
    RegistrationPageLocators,
    UserInProfileLocators,
)


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


class TestCreateAd:

    def test_create_ad_authorized_user(self, driver):
        wait = WebDriverWait(driver, 10)

        driver.get(urls.BASE_URL)

        wait.until(EC.element_to_be_clickable(CommonLocators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)).click()

        email = helpers.Helpers.generate_random_email()
        password = "Password123"

        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        for attempt in range(3):
            try:
                place_ad_button = wait.until(EC.element_to_be_clickable(CommonLocators.PLACE_AD_BUTTON))
                place_ad_button.click()
                break
            except StaleElementReferenceException:
                print(f"Попытка {attempt + 1} не удалась, повторный поиск элемента.")
        else:
            raise Exception("Не удалось кликнуть на кнопку 'Разместить объявление' после 3 попыток.")

        wait.until(EC.visibility_of_element_located(AdCreationLocators.NAME_OF_GOOD_INPUT)).send_keys("Гитара")

        desc_input = driver.find_element(*AdCreationLocators.DESCRIPTION_TEXTAREA)
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", desc_input)
        wait.until(EC.visibility_of(desc_input)).send_keys("Отличная гитара, почти новая")

        category_dropdown = wait.until(EC.element_to_be_clickable(AdCreationLocators.ARROW_BUTTON_DROPDOWN_CATEGORY))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", category_dropdown)
        category_dropdown.click()

        hobby_button = wait.until(EC.element_to_be_clickable(AdCreationLocators.HOBBY_BUTTON))
        hobby_button.click()

        price_input = driver.find_element(*AdCreationLocators.PRICE_INPUT)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", price_input)
        wait.until(EC.visibility_of(price_input)).send_keys("15000")

        city_dropdown = wait.until(EC.element_to_be_clickable(AdCreationLocators.ARROW_BUTTON_DROPDOWN_CITY))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", city_dropdown)
        city_dropdown.click()

        novosibirsk_button = wait.until(EC.element_to_be_clickable(AdCreationLocators.NOVOSIBIRSK_BUTTON))
        novosibirsk_button.click()

        condition_radio = driver.find_element(*AdCreationLocators.CONDITION_RADIOBUTTON)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", condition_radio)
        wait.until(EC.element_to_be_clickable(condition_radio)).click()

        publish_button = driver.find_element(*AdCreationLocators.PUBLISH_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", publish_button)
        wait.until(EC.element_to_be_clickable(publish_button)).click()

        try:
            profile_button = wait.until(EC.element_to_be_clickable(UserInProfileLocators.PROFILE_BUTTON))
            driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", profile_button)
            profile_button.click()
        except StaleElementReferenceException:
            profile_button = wait.until(EC.element_to_be_clickable(UserInProfileLocators.PROFILE_BUTTON))
            driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", profile_button)
            profile_button.click()

        wait.until(EC.visibility_of_element_located(UserInProfileLocators.MY_ADS_HEADER))
        ads_titles = wait.until(EC.presence_of_all_elements_located(UserInProfileLocators.MY_AD_H2))
        assert any("Гитара" in ad.text for ad in ads_titles), "Объявление не найдено в списке"

    def test_create_ad_unauthorized_user(self, driver):
        wait = WebDriverWait(driver, 10)

        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        place_ad_button = wait.until(EC.element_to_be_clickable(CommonLocators.PLACE_AD_BUTTON))
        place_ad_button.click()

        auth_modal_header = wait.until(EC.visibility_of_element_located(AuthRequiredLocators.AUTH_REQUIRED_HEADER))
        assert auth_modal_header.is_displayed()
        assert "авторизуйтесь" in auth_modal_header.text.lower()