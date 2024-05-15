from config import URL, password, incorrect_password, name, new_email
from conftest import driver
from locators import RegisterPageLocators
from conftest import register_user
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestRegistration:

    def test_right_registration(self, driver, register_user):
        driver.get(URL+"/register")
        register_user(name, new_email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.ENTER_HEADING))
# проверить что кнопка содержиит текст "Вход"
        assert 'Войти' in driver.find_element(*RegisterPageLocators.ENTER_BUTTON).text

    def test_wrong_registration(self, driver, register_user):
        driver.get(URL+"/register")
        register_user(name, new_email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(incorrect_password)
        driver.find_element(*RegisterPageLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((RegisterPageLocators.INCORRECT_PASSWORD_NOTIFICATION)))
# здесь написать тест обводки там в классе добавлется эрорр или через цсс элементы
        assert 'Некорректный пароль' in driver.find_element(*RegisterPageLocators.INCORRECT_PASSWORD_NOTIFICATION).text
