from config import URL, name, new_email, email, password, incorrect_password
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
        login_for_change_section()
        driver.find_element(*ChangeSection.SAUCES_SECTION).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH,"//div[2][contains(@class, 'tab_tab_type_current__2BEPc')]")))

    def test_change_on_fillings(self, driver, login_for_change_section):
        driver.get(URL+"/login")
        login_for_change_section()
        driver.find_element(*ChangeSection.FILLINGS_SECTION).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH,"//div[3][contains(@class, 'tab_tab_type_current__2BEPc')]")))

    def test_change_on_buns(self, driver, login_for_change_section): #тут надо учесть чт омы по умолчанию находимя в этомр азделе и надо сходит ьв другой сначала
        driver.get(URL + "/login")
        login_for_change_section()
        # переключаем на соусы т.к. по умолчанию будут булки
        driver.find_element(*ChangeSection.SAUCES_SECTION).click()
        # переключаем на булки
        driver.find_element(*ChangeSection.BUNS_SECTION).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[1][contains(@class, 'tab_tab_type_current__2BEPc')]")))





