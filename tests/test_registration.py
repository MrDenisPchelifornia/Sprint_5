from config import URL, password, incorrect_password
from conftest import driver
from locators import RegisterPageLocators
from conftest import register_user
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestRegistration:

    def test_right_registration(self, driver, register_user):
        driver.get(URL+"/register")
        register_user()
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.SUBMIT_BUTTON).click()

        locator = (By.XPATH, "//main/div/h2")
        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element(locator, "Вход"))

        assert 'Вход' in driver.find_element(By.XPATH, "//main/div/h2").text

    def test_wrong_registration(self, driver, register_user):
        driver.get(URL+"/register")
        register_user()
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(incorrect_password)
        driver.find_element(*RegisterPageLocators.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//form/fieldset[3]/div/p")))

        assert 'Некорректный пароль' in driver.find_element(By.XPATH,"//form/fieldset[3]/div/p").text
