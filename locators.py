from selenium.webdriver.common.by import By


class CommonLocators:
    LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    PLACE_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
    USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")
    USER_NAME = (By.XPATH, "//*[contains(text(), 'User.')]")


class RegistrationPageLocators:
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    EMAIL_ERROR_MESSAGE = (By.CSS_SELECTOR, ".input_span__yWPqB")
    INPUT_ERROR_CONTAINER_EMAIL = (By.XPATH, "//input[@name='email']/parent::div")
    INPUT_ERROR_CONTAINER_PASSWORD = (By.XPATH, "//input[@name='password']/parent::div")
    INPUT_ERROR_CONTAINER_SUBMIT_PASSWORD = (By.XPATH, "//input[@name='submitPassword']/parent::div")


class UserInProfileLocators:
    USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")
    USER_NAME = (By.XPATH, "//*[contains(text(), 'User')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
    PROFILE_BUTTON = (By.CSS_SELECTOR, "button.circleSmall")
    MY_ADS_HEADER = (By.XPATH, "//h1[text()='Мои объявления']")
    MY_AD_H2 = (By.CSS_SELECTOR, "h2.h2")


class AuthRequiredLocators:
    AUTH_REQUIRED_HEADER = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")


class AdCreationLocators:
    NAME_OF_GOOD_INPUT = (By.NAME, "name")
    DESCRIPTION_TEXTAREA = (By.XPATH, "//textarea[@name='description' and @placeholder='Описание товара']")
    PRICE_INPUT = (By.NAME, "price")
    ARROW_BUTTON_DROPDOWN_CATEGORY = (By.CLASS_NAME, "dropDownMenu_arrowDown__pfGL1")
    HOBBY_BUTTON = (By.XPATH, "//button[.//span[text()='Хобби']]")
    ARROW_BUTTON_DROPDOWN_CITY = (By.CSS_SELECTOR, "button.dropDownMenu_arrowDown__pfGL1")
    CONDITION_RADIOBUTTON = (By.XPATH, "//div[contains(@class, 'radioUnput_inputRegular__')]")
    PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")
