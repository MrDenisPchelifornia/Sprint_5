from config import URL, name, new_email, email, password, incorrect_password
from conftest import driver
from locators import LogoutPageLocators
from conftest import register_user
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

class TestLogOut:

    def test_log_out_on_personal_area(self, driver):
        driver.get(URL+"/login")
        driver.find_element(*LogoutPageLocators.EMAIL_INPUT).send_keys(email) # Заполняем имейл
        driver.find_element(*LogoutPageLocators.PASSWORD_INPUT).send_keys(password) # Заполняем пароль
        driver.find_element(*LogoutPageLocators.SUBMIT_BUTTON).click() # Жмем "Войти"
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LogoutPageLocators.MAKE_CHECKOUT_ORDER_BUTTON)) # Проверяем что появилась кнопка "Оформить заказ"
        driver.find_element(*LogoutPageLocators.PERSONAL_AREA_BUTTON).click() # Жмем "Личный кабинет"
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LogoutPageLocators.PROFILE_BUTTON)) # Проверяем что есть "Кнопка профиль"
        driver.find_element(*LogoutPageLocators.EXIT_BUTTON_ON_PERSONAL_AREA).click() # Жмем "Выход"
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LogoutPageLocators.SUBMIT_BUTTON)) # Жмем кнопку "Войти"
        assert 'Вход' in driver.find_element(*LogoutPageLocators.ENTER_TITLE).text # Сравниваем что заголовком является словов "Вход"
