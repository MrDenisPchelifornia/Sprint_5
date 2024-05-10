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

        driver.find_element(*LogoutPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LogoutPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LogoutPageLocators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//section[2]/div/button")))

        driver.find_element(*LogoutPageLocators.PERSONAL_AREA_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//nav/ul/li[1]/a")))

        driver.find_element(*LogoutPageLocators.EXIT_BUTTON_ON_PERSONAL_AREA).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/form/button")))

        assert 'Вход' in driver.find_element(By.XPATH, "//div/main/div/h2").text
