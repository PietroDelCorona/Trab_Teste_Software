'''
Buscar a finalização do processo de compra preenchendo os campos de endereço de entrega e esperar a resposta final do site
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class TestCheckout:
    def setup_class(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()

    def test_checkout(self):
        driver.get('https://www.saucedemo.com/')

        time.sleep(2)

        field_login = driver.find_element(By.ID, 'user-name')
        field_login.send_keys('standard_user')

        field_password = driver.find_element(By.ID, 'password')
        field_password.send_keys('secret_sauce')

        field_password.send_keys(Keys.RETURN)

        time.sleep(2)

        #acessando o carrinho
        carrinho = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        carrinho.click()

        time.sleep(2)

        checkout_button = driver.find_element(By.ID, 'checkout')
        checkout_button.click()

        time.sleep(1.7)

        continue_button = driver.find_element(By.ID, 'continue')
        continue_button.click()

        time.sleep(2)

        #todos sem preencher
        label_result_todos_sem_preencher = driver.find_element(By.CSS_SELECTOR, '.error-message-container error, h3')

        print('sem preencher nenhum input:')
        print(label_result_todos_sem_preencher.text)
        print('--------------------')
        driver.save_screenshot('screen_erro_checkout_fields_vazios.png')

        assert 'Error: First Name is required' in label_result_todos_sem_preencher.text
 
        #######################

        field_first_name = driver.find_element(By.ID, 'first-name')
        field_first_name.send_keys('ALO')

        field_last_name = driver.find_element(By.ID, 'last-name')
        field_last_name.send_keys('ALO')

        field_cep = driver.find_element(By.ID, 'postal-code')
        field_cep.send_keys('10')

        time.sleep(1.5)

        information_continue_button = driver.find_element(By.ID,'continue')
        information_continue_button.click()

        time.sleep(1.7)

        finish_button = driver.find_element(By.ID, 'finish')
        finish_button.click()

        time.sleep(2)

        message_finish = driver.find_element(By.CLASS_NAME, 'complete-text')
        print('compra concluída:')
        print(message_finish.text)

        driver.save_screenshot('compra_concluida.png')

        time.sleep(2)





    def teardown_class(self):
        driver.close()