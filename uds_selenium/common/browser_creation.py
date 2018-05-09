import unittest
from selenium import webdriver

# import os 
# import sys 
# lib_path = os.path.abspath('../') 
# sys.path.insert(0,lib_path)
# from testcases.login import Uds_login

class Browser_creation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.firefox_driver = webdriver.Firefox()
        cls.firefox_driver.get("https://172.30.36.110/login/")
        cls.firefox_driver.maximize_window()
        # s = self.firefox_driver.__getattribute__(' oVirt/RHEV Platform Provider')
        # print '^^^^^^^^^^^^^^^^^^',s

    @classmethod
    def tearDownClass(cls):
        cls.firefox_driver.quit()

# if __name__ == "__main__":
#     unittest.main()   
