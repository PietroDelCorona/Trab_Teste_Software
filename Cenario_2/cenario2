
'''
Entrar no site alvo de avaliação do teste clicar no link de cadastro e tentar se cadastrar no site preenchendo os campos e clicar em "cadastrar". Testando todos os usuários disponíveis pelo site, assim como, as mudanças na senha fornecida.
'''

import time
import warnings
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def test_login(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com")
        print("URL:", driver.current_url)

        user = input("Usuário: ")
        password = input("Senha: ")

        username = driver.find_element(By.ID, "user-name")
        password_box = driver.find_element(By.ID, "password")

        username.send_keys(user)
        password_box.send_keys(password)

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        if "inventory" in driver.current_url:
            print("Login bem-sucedido!")
        else:
            print("Falha no login!")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
