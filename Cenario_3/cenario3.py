
'''
Visitar o site e tentar entrar com a conta cadastrada. Visualizar o carrinho de compras e remover os produtos já selecionados.
'''
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class CustomCheckSite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()

    def test_shopping_cart(self):
        self.assertIn("Swag Labs", self.driver.title)

        username_box = self.driver.find_element(By.NAME, "user-name")
        username_box.send_keys("standard_user")

        time.sleep(2)

        password_box = self.driver.find_element(By.NAME, "password")
        password_box.send_keys("secret_sauce")

        password_box.send_keys(Keys.RETURN)

        time.sleep(5)

        self.assertIn("inventory", self.driver.page_source)

        icone_carrinho = self.driver.find_element(By.ID, "shopping_cart_container")
        icone_carrinho.click()

        self.assertIn("cart", self.driver.page_source)

        produtos_no_carrinho = self.driver.find_elements(By.CLASS_NAME, "cart_item")

        if len(produtos_no_carrinho) == 0:
            print("O carrinho está vazio. Nada para remover.")
        else:
            for produto in produtos_no_carrinho:
                remove_button = produto.find_element(By.NAME, "remove-sauce-labs-backpack")
                produto_nome = produto.find_element(By.CLASS_NAME, "inventory_item_name").text
                remove_button.click()
                print(f"Produto '{produto_nome}' removido do carrinho.")

        time.sleep(3)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()



