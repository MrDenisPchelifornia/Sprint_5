from config import URL, name, new_email, email, password, incorrect_password
from conftest import driver
from locators import RegisterPageLocators, LoginPageLocators
from conftest import register_user
from conftest import login_and_go_to_personal_area
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class TestTransition:

    def test_transition_in_personal_area_from_main_screen(self, driver, login_and_go_to_personal_area):
        driver.get(URL+"/login")
        login_and_go_to_personal_area(email, password)
        assert 'В этом разделе вы можете изменить свои персональные данные' in driver.find_element(*LoginPageLocators.DESCRIPTION_TEXT_ON_PERSONAL_AREA).text


    def test_transition_in_conctractor_from_personal_area(self, driver, login_and_go_to_personal_area):
        driver.get(URL+"/login")
        login_and_go_to_personal_area(email, password)
        driver.find_element(*LoginPageLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((LoginPageLocators.MAKE_CHECKOUT_ORDER_BUTTON)))
        assert 'Соберите бургер' in driver.find_element(*LoginPageLocators.MAKE_BURGER_HEADING).text

    def test_transition_in_conctractor_throught_logo(self, driver, login_and_go_to_personal_area):
        driver.get(URL+"/login")
        login_and_go_to_personal_area(email, password)
        driver.find_element(*LoginPageLocators.LOGO).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((LoginPageLocators.MAKE_CHECKOUT_ORDER_BUTTON)))
        assert 'Соберите бургер' in driver.find_element(*LoginPageLocators.MAKE_BURGER_HEADING).text
