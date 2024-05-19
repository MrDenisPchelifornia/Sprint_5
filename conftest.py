import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from locators import LoginPageLocators
from locators import RegisterPageLocators
from locators import LogoutPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from data import URL, name, new_email, email, password, incorrect_password

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture # Фикстура для проверки логина после перехода с разных разделов
def login_user(driver):
    def _login_user(email, password):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((LoginPageLocators.MAKE_CHECKOUT_ORDER_BUTTON)))
    return _login_user

@pytest.fixture # Фикстура для проверки регистрации, не учтен пароль так как он разный в разных проверках
def register_user(driver):
    def _register_user(name, new_email):
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(new_email)
    return _register_user

#тут на пару шагов меньше чем в фикстуре для логина поэтому решил сделать новую что бы не переписывать ту и другие тесты
#локаторы оставил те же
@pytest.fixture
def login_for_change_section(driver):
    def _login_for_change_section(email, password):
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((LoginPageLocators.MAKE_CHECKOUT_ORDER_BUTTON)))
    return _login_for_change_section

# фикстура для входа и перехода в личный кабинет, локаторы брал тоже из другого раздела
@pytest.fixture
def login_and_go_to_personal_area(driver):
    def _login_and_go_to_personal_area(email, password):
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        # ждем кнопку "оформить заказ" подтверждающую что мы вошли
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((LoginPageLocators.MAKE_CHECKOUT_ORDER_BUTTON)))
        # кликаем на кнопку личный кабинет и ждем появления кнопки "Профиль"
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((LogoutPageLocators.PROFILE_BUTTON)))
    return _login_and_go_to_personal_area
