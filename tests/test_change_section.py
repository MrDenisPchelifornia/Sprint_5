from data import URL, name, new_email, email, password, incorrect_password
from conftest import driver
from locators import RegisterPageLocators
from locators import ChangeSection
from conftest import register_user
from conftest import login_for_change_section
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

class TestChangeSection:

    def test_change_on_sauces(self, driver, login_for_change_section):
        driver.get(URL+"/login")
        login_for_change_section(email, password) # Логин
        driver.find_element(*ChangeSection.SAUCES_SECTION).click()
        assert driver.find_element(*ChangeSection.SAUCES_SECTION) in (driver.find_element(*ChangeSection.ACTIVATED_SECTION)).find_elements(*ChangeSection.IN_ACTIV) # Проверяем что раздел "Соусы" активен

    def test_change_on_fillings(self, driver, login_for_change_section):
        driver.get(URL+"/login")
        login_for_change_section(email, password) # Логин
        driver.find_element(*ChangeSection.FILLINGS_SECTION).click()
        assert driver.find_element(*ChangeSection.FILLINGS_SECTION) in (driver.find_element(*ChangeSection.ACTIVATED_SECTION)).find_elements(*ChangeSection.IN_ACTIV) # Проверяем что раздел "Начинки" активен

    def test_change_on_buns(self, driver, login_for_change_section): #тут надо учесть что мы по умолчанию находимя в этом разделе и надо сходить в другой сначала
        driver.get(URL + "/login")
        login_for_change_section(email, password) # Логин
        # переключаем на соусы т.к. по умолчанию будут булки
        driver.find_element(*ChangeSection.SAUCES_SECTION).click()
        # переключаем на булки
        driver.find_element(*ChangeSection.BUNS_SECTION).click()
        assert driver.find_element(*ChangeSection.BUNS_SECTION) in (driver.find_element(*ChangeSection.ACTIVATED_SECTION)).find_elements(*ChangeSection.IN_ACTIV) # Проверяем что раздел "Булки" активен



