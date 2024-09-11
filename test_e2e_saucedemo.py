import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Драйвер Chrome создан
driver = webdriver.Chrome()

# Переход на сайт 'https://www.saucedemo.com/'
driver.get('https://www.saucedemo.com/')
logging.info('Открыта страница авторизации')

# Ввод логина и пароля
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
logging.info('Введены учетные данные')

# Нажатие кнопки 'Войти'
driver.find_element(By.ID, 'login-button').click()
logging.info('Нажата кнопка "Войти"')

# Ожидание загрузки страницы с товарами
WebDriverWait(driver, 10).until(expected_conditions.
                                presence_of_element_located(
                                    (By.ID, 'inventory_container')))
logging.info('Загружена страница с товарами')

# Добавление товара "Sauce Labs Backpack" в корзину
driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
logging.info('Добавлен товар "Sauce Labs Backpack" в корзину')

# Ожидание обновления корзины
WebDriverWait(driver, 10).until(expected_conditions.
                                presence_of_element_located(
                                    (By.CLASS_NAME, 'shopping_cart_link')))
logging.info('Корзина обновлена')

# Открытие корзины
driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
logging.info('Корзина открыта')

# Проверка наличия товара "Sauce Labs Backpack" в корзине
assert 'Sauce Labs Backpack' in driver.page_source
logging.info('Товар "Sauce Labs Backpack" присутствует в корзине')

# Переход к странице оформления заказа
driver.find_element(By.ID, 'checkout').click()
logging.info('Нажата кнопка "Перейти к оформлению"')

# Ожидание загрузки страницы оформления заказа
WebDriverWait(driver, 10).until(expected_conditions.
                                presence_of_element_located(
                                    (By.ID, 'checkout_info_container')))
logging.info('Загружена страница оформления заказа')

# Ввод данных для оформления заказа
driver.find_element(By.ID, 'first-name').send_keys('Test')
driver.find_element(By.ID, 'last-name').send_keys('User')
driver.find_element(By.ID, 'postal-code').send_keys('Secret1!')
logging.info('Введены данные для оформления заказа')

# Нажатие кнопки 'Продолжить'
driver.find_element(By.ID, 'continue').click()
logging.info('Нажата кнопка "Продолжить"')

# Проверка наличия товара на странице оформления заказа
assert "Sauce Labs Backpack" in driver.page_source
logging.info('Товар "Sauce Labs Backpack" '
             'присутствует на странице оформления заказа')

# Нажатие кнопки 'Finish'
driver.find_element(By.ID, 'finish').click()
logging.info('Нажата кнопка "Finish"')

# Проверка осуществления покупки
assert "Your order has been dispatched" in driver.page_source
logging.info('Покупка осуществленна успешно')

# Закрытие драйвера
driver.quit()
logging.info('Драйвер закрыт')
