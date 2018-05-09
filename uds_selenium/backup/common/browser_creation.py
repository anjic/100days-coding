import unittest
from selenium import webdriver

class Browser_creation(unittest.TestCase):

    def setUp(self):
        self.firefox_driver = webdriver.Firefox()
        self.firefox_driver.get("https://172.30.36.110/login/")
        self.firefox_driver.maximize_window()
        # s = self.firefox_driver.__getattribute__(' oVirt/RHEV Platform Provider')
        # print '^^^^^^^^^^^^^^^^^^',s

    def tearDown(self):
        self.firefox_driver.quit()

# if __name__ == "__main__":
#     unittest.main()   
