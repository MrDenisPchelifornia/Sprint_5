from selenium.webdriver.common.by import By

class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//fieldset[1]/div/div/input") # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, "//fieldset[2]/div/div/input") # Поле ввода имейла
    PASSWORD_INPUT = (By.XPATH, "//fieldset[3]/div/div/input") # Поле ввода пароля
    SUBMIT_BUTTON = (By.XPATH, "//div/form/button") #Кнопка "Зарегистрироваться"

class LoginPageLocators:
    ENTER_BUTTON_ON_MAIN = (By.XPATH, "//section[2]/div/button") # Кнопка войти в аккаунт на главной
    ENTER_HEADING = (By.XPATH, "/html/body/div/div/main/div/h2")  # Заголовок "Вход" на экране входа
    EMAIL_INPUT = (By.XPATH, "//fieldset[1]/div/div/input") # Поле ввода имейла
    PASSWORD_INPUT = (By.XPATH, "//fieldset[2]/div/div/input") # Поле ввода пароля
    SUBMIT_BUTTON = (By.XPATH, "//div/form/button") # Кнопка "Войти" на экране входа
    PERSONAL_AREA_BUTTON = (By.XPATH, "/html/body/div/div/header/nav/a/p") # Кнопка "Личный кабинет" на главной
    REGISTRATION_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj") # Кнопка "Зарегистрироваться" на экране входа
    ENTER_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj")  # Кнопка "Войти" на экране восстановления пароля

class LogoutPageLocators:

    EMAIL_INPUT = (By.XPATH, "//fieldset[1]/div/div/input") # Поле ввода имейла
    PASSWORD_INPUT = (By.XPATH, "//fieldset[2]/div/div/input") #  Поле ввода пароля
    SUBMIT_BUTTON = (By.XPATH, "//div/form/button")  # Кнопка "Войти" на экране входа
    PERSONAL_AREA_BUTTON = (By.LINK_TEXT, "Личный Кабинет") # Кнопка "Личный кабинет" на главной
    EXIT_BUTTON_ON_PERSONAL_AREA = (By.XPATH, "//nav/ul/li[3]/button") # Кнопка

class ChangeSection:

    SAUCES_SECTION = (By.XPATH, "//section[1]/div[1]/div[2]/span")
    FILLINGS_SECTION = (By.XPATH, "//section[1]/div[1]/div[3]/span")
    BUNS_SECTION = (By.XPATH, "//section[1]/div[1]/div[1]/span")
