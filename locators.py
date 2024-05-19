from selenium.webdriver.common.by import By

class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, ".//label[text() = 'Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")
# Кнопка "Зарегистрироваться" на экране входа
    REGISTRATION_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj")
# Заголовок "Вход" на экране входа
    ENTER_HEADING = (By.XPATH, "//div/main/div/h2")
# Кнопка "Войти" на экране входа
    ENTER_BUTTON = (By.XPATH, "//div/form/button")
# Уведомление о некорректном пароле
    INCORRECT_PASSWORD_NOTIFICATION = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")


class LoginPageLocators:
# Кнопка войти в аккаунт на главной
    ENTER_BUTTON_ON_MAIN = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_large__G21Vg')]")
# Заголовок "Вход" на экране входа
    ENTER_HEADING = (By.XPATH, "//div/main/div/h2")
# Поле ввода имейла
    EMAIL_INPUT = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input")
# Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")
# Кнопка "Войти" на экране входа
    SUBMIT_BUTTON = (By.XPATH, "//div/form/button")
# Кнопка "Личный кабинет" на главной
    PERSONAL_AREA_BUTTON = (By.LINK_TEXT, "Личный Кабинет")
# Кнопка "Зарегистрироваться" на экране входа
    REGISTRATION_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj")
# Кнопка "Войти" на экране восстановления пароля
    ENTER_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj")
# Кнопка "Оформить заказ"
    MAKE_CHECKOUT_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
# Текст в профиле
    DESCRIPTION_TEXT_ON_PERSONAL_AREA = (By.XPATH,"//div/nav/p")
# Кнопка конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and contains(@class, 'ml-2')]")
# Заголовок Соберите бургер
    MAKE_BURGER_HEADING = (By.XPATH, "//h1[contains(@class, 'text') and contains(@class, 'text_type_main-large') and contains(@class, 'mb-5') and contains(@class, 'mt-10')]")
# Лого
    LOGO = (By.XPATH, "//header/nav/div")



class LogoutPageLocators:
# Поле ввода имейла
    EMAIL_INPUT = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input")
# Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")
# Кнопка "Войти" на экране входа
    SUBMIT_BUTTON = (By.XPATH, "//div/form/button")
# Кнопка "Личный кабинет" на главной
    PERSONAL_AREA_BUTTON = (By.LINK_TEXT, "Личный Кабинет")
# Кнопка "Выйти" в личном кабинете
    EXIT_BUTTON_ON_PERSONAL_AREA = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and contains(@class, 'text') and contains(@class, 'text_type_main-medium text_color_inactive') and contains(@class, 'text_color_inactive')]")
# Кнопка "Оформить заказ"
    MAKE_CHECKOUT_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
# Кнопка "Профиль" в личном кабинете
    PROFILE_BUTTON = (By.XPATH, "//a[contains(text(), 'Профиль')]")
# Заголовок "Вход" на экране входа
    ENTER_TITLE = (By.XPATH, "//div/main/div/h2")

class ChangeSection:

# Кнопка переключения на раздел "Соусы"
    SAUCES_SECTION = (By.XPATH, "//span[contains(text(), 'Соусы')]")
# Кнопка переключения на раздел "Начинки"
    FILLINGS_SECTION = (By.XPATH, "//span[contains(text(), 'Начинки')]")
# Кнопка переключения на раздел "Булки"
    BUNS_SECTION = (By.XPATH, "//span[contains(text(), 'Булки')]")
# Локатор признака активности выбранного раздела
    ACTIVATED_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]")
    IN_ACTIV = (By.XPATH, ".//*")