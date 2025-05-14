import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import CommonLocators, AuthRequiredLocators  # Убедись, что импорт локаторов правильный


def test_create_ad_unauthorized_user(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    place_ad_button = wait.until(EC.element_to_be_clickable(CommonLocators.PLACE_AD_BUTTON))
    place_ad_button.click()

    auth_modal_header = wait.until(EC.visibility_of_element_located(AuthRequiredLocators.AUTH_REQUIRED_HEADER))
    assert auth_modal_header.is_displayed()
    assert "авторизуйтесь" in auth_modal_header.text.lower()
