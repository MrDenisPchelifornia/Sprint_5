from config import URL, name, new_email, email, password, incorrect_password
from conftest import driver
from locators import RegisterPageLocators
from conftest import register_user
from conftest import login_and_go_to_personal_area
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class TestTransition:

    def test_transition_in_personal_area_from_main_screen(self, driver, login_and_go_to_personal_area):
        driver.get(URL+"/login")
        login_and_go_to_personal_area()
        assert 'В этом разделе вы можете изменить свои персональные данные' in driver.find_element(By.XPATH,"/html/body/div/div/main/div/nav/p").text

    def test_transition_in_conctractor_from_personal_area(self, driver, login_and_go_to_personal_area):
        driver.get(URL+"/login")
        login_and_go_to_personal_area()
        #Находим "Констурктор" и жмакаем по нему ждем заголовка "Соберите бургер"
        driver.find_element(By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a/p").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/section[1]/h1")))
        assert 'Соберите бургер' in driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/h1").text

    def test_transition_in_conctractor_throught_logo(self, driver, login_and_go_to_personal_area):
        driver.get(URL+"/login")
        login_and_go_to_personal_area()
        # ищем лого жмем и ждем появления заголовка "Соберите бургер"
        driver.find_element(By.XPATH, "/html/body/div/div/header/nav/div").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/section[1]/h1")))
        assert 'Соберите бургер' in driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/h1").text
