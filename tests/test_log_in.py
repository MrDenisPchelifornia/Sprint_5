import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from conftest import login_user
from locators import LoginPageLocators
from config import URL

class TestLogIn:

    def test_enter_through_button_on_main(self, driver, login_user):
        driver.get(URL)
        driver.find_element(*LoginPageLocators.ENTER_BUTTON_ON_MAIN).click()
# Ниже ждем кнопку "Вход"
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/form/button")))
        login_user()

    def test_enter_through_personal_area_button(self, driver, login_user):
        driver.get(URL)
        driver.find_element(*LoginPageLocators.PERSONAL_AREA_BUTTON).click()
# Ниже ждем заголовок "Вход"
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//main/div/h2"), "Вход"))
        login_user()

    def test_enter_through_button_on_registration_form(self, driver, login_user):
        driver.get(URL + "/register")
        driver.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
# Ниже ждем кнопку "Зарегистрироваться"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/form/button")))
        login_user()

    def test_enter_through_button_on_password_recovery_form(self, driver, login_user):
        driver.get(URL + "/forgot-password")
        driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
# Ниже ждем кнопку "Войти" на экране восстановления пароля
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//main/div/h2"), "Вход"))
        login_user()