
import unittest
from cenario4 import CheckSite
from cenario4 import WebDriverManager  

class TestCheckSite(unittest.TestCase):
    def test_login_successful(self):
        driver_manager = WebDriverManager() 
        check_site = CheckSite(driver_manager)  
        check_site.test_login()
        self.assertTrue(check_site.login_successful)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestCheckSite('test_login_successful'))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("Login bem-sucedido")
    else:
        print("Falha no login")


