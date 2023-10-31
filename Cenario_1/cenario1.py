import time
import warnings

import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class SearchNameGoogle(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        
    def test_search_in_google(self):
        driver = self.driver
        driver.get("https://www.google.com")
        print("URL:", driver.current_url)
        self.assertIn("Google", driver.title)
               
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("saucedemo")
        
        search_box.send_keys(Keys.RETURN)
        
        time.sleep(5)
        
        self.assertIn("https://www.saucedemo.com/", driver.page_source)
    
    def tearDown(self):
        self.driver.close()       


if __name__ == "__main__":
    unittest.main()