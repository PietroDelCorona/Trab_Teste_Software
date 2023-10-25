
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

class CheckSite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        
    def test_login(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com")
        print("URL:", driver.current_url)
        self.assertIn("Swag Labs", driver.title)
        
        username_box = driver.find_element(By.NAME, "user-name")
        username_box.send_keys("standard_user")
        
        password_box = driver.find_element(By.NAME, "password")
        password_box.send_keys("secret_sauce")
        
        password_box.send_keys(Keys.RETURN)
        
        time.sleep(5)
        
        self.assertIn("inventory", driver.page_source)
        
    def tearDown(self):
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main()
