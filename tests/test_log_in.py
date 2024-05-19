import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from conftest import login_user
from locators import LoginPageLocators
from data import URL
from data import URL, name, new_email, email, password, incorrect_password

class TestLogIn:

    def test_enter_through_button_on_main(self, driver, login_user):
        driver.get(URL)
        driver.find_element(*LoginPageLocators.ENTER_BUTTON_ON_MAIN).click()
        login_user(email, password)
        assert 'Оформить заказ' in driver.find_element(*LoginPageLocators.MAKE_CHECKOUT_ORDER_BUTTON).text

    def test_enter_through_personal_area_button(self, driver, login_user):
        driver.get(URL)
        driver.find_element(*LoginPageLocators.PERSONAL_AREA_BUTTON).click()
        login_user(email, password)
        assert 'Оформить заказ' in driver.find_element(*LoginPageLocators.MAKE_CHECKOUT_ORDER_BUTTON).text

    def test_enter_through_button_on_registration_form(self, driver, login_user):
        driver.get(URL + "/register")
        driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
        login_user(email, password)
        assert 'Оформить заказ' in driver.find_element(*LoginPageLocators.MAKE_CHECKOUT_ORDER_BUTTON).text

    def test_enter_through_button_on_password_recovery_form(self, driver, login_user):
        driver.get(URL + "/forgot-password")
        driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
        login_user(email, password)
        assert 'Оформить заказ' in driver.find_element(*LoginPageLocators.MAKE_CHECKOUT_ORDER_BUTTON).text