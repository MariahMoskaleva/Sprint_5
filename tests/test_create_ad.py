from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import helpers
import urls

from locators import (
    CommonLocators,
    RegistrationPageLocators,
    AdCreationLocators,
    UserInProfileLocators,
)


def test_create_ad_authorized_user(driver):
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
