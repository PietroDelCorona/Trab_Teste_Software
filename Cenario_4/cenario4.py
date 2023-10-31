
'''
Visitar o site completo, buscando os diferentes produtos do portfólio do site e encher o carrinho com as quantidades variadas.
'''
import time
import warnings

import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class WebDriverManager:
    def __init__(self):
        self.driver = None

    def setup_driver(self):
        self.driver = webdriver.Chrome()

    def teardown_driver(self):
        if self.driver:
            self.driver.quit()

class CheckSite(unittest.TestCase):
    def __init__(self, driver_manager):
        super().__init__()
        self.driver_manager = driver_manager
        self.login_successful = False

    def test_login(self):
        if self.driver_manager.driver is None:
            self.driver_manager.setup_driver()

        driver = self.driver_manager.driver
        driver.get("https://www.saucedemo.com")
        print("URL:", driver.current_url)
        self.assertIn("Swag Labs", driver.title)
        
        driver.maximize_window()
        
        username_box = driver.find_element(By.NAME, "user-name")
        username_box.send_keys("standard_user")
        
        time.sleep(2)
        
        password_box = driver.find_element(By.NAME, "password")
        password_box.send_keys("secret_sauce")
        
        password_box.send_keys(Keys.RETURN)
        
        time.sleep(5)
        
        self.assertIn("inventory", driver.page_source)
    
        
        primeiro_produto = driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack")
        primeiro_produto.click()
        
        time.sleep(3)
        
        segundo_produto = driver.find_element(By.NAME, "add-to-cart-sauce-labs-bike-light")
        segundo_produto.click()
        
        time.sleep(3)
        
        driver.execute_script("window.scrollTo(0, 300);")
        
        terceiro_produto = driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
        terceiro_produto.click()    
           
        time.sleep(3)
        
        quarto_produto = driver.find_element(By.NAME, "add-to-cart-sauce-labs-fleece-jacket")
        quarto_produto.click()       
        
        time.sleep(3)
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        quinto_produto = driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie")
        quinto_produto.click()   
            
        time.sleep(3)
        
        sexto_produto = driver.find_element(By.NAME, "add-to-cart-test.allthethings()-t-shirt-(red)")
        sexto_produto.click()       
        
        time.sleep(3)
        
        driver.execute_script("window.scrollTo(0,0)")
        
        time.sleep(3)
        
        icone_carrinho = driver.find_element(By.ID, "shopping_cart_container")
        icone_carrinho.click()
        
        self.assertIn("cart", driver.page_source)
        
        time.sleep(3)
        
        if "cart" in driver.current_url:
            print("Carrinho completo!")
        else:
            print("Carrinho insponível!")
        
        if "cart" in driver.current_url:
            self.login_successful = True
        
    def tearDown(self):
        self.driver.close()
        

if __name__ == "__main__":
    driver_manager = WebDriverManager()
    check_site = CheckSite(driver_manager)
    check_site.test_login()
    
    # Certifique-se de chamar teardown_driver no final do teste
    driver_manager.teardown_driver()
