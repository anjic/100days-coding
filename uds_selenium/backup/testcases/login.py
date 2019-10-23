import unittest 
# from selenium import webdriver
import time
import os 
import sys 
lib_path = os.path.abspath('../') 
sys.path.insert(0,lib_path)
from common.browser_creation import Browser_creation
from selenium.webdriver.support.select import Select
# from dashboard import Dashboard_Uds

class Uds_login(Browser_creation):
  
    def test_1(self):
        # super(Uds_login,self).setUp()
        # assert "Welcome" in driver.title
        self.firefox_driver.find_element_by_id("id_user").send_keys("admin")
        self.firefox_driver.find_element_by_id("id_password").send_keys("udsmam0")
        self.firefox_driver.find_element_by_xpath("//button[@type='submit']").click()
        self.firefox_driver.find_element_by_xpath("//*[@class='dropdown'][2]").click()
        # self.firefox_driver.find_element_by_xpath("//*[@class='dropdown'][2]")
        self.firefox_driver.find_element_by_xpath("//*[@href='/adm/']").click()
        # self.firefox_driver.implicitly_wait(20)
        time.sleep(5)
        

    def test_2(self):
        # print 'test dash'
        # super(Dashboard_Uds, self).test_login() 
        # Uds_login().test_login()
        assert "UDS Dashboard" in self.firefox_driver.title 
        self.firefox_driver.find_element_by_class_name("close").click()
        # self.firefox_driver.find_element_by_xpath("//div[@class='side-nav']/ul/li[2]/a[@class='lnk-service_providers']").click()
        # assert "UDS Dashboard" in self.firefox_driver.title 
        print("###################################")
        # self.firefox_driver.find_element_by_class_name("close").click()
        self.firefox_driver.find_element_by_xpath("//div[@class='col-lg-3'][2]/div/a/div/div/div[@class='col-xs-10']").click()
        time.sleep(1)
        self.firefox_driver.find_element_by_class_name("close").click()
        self.firefox_driver.find_element_by_xpath("//*[@class='label-tbl-button' and text()='New']").click()
        time.sleep(1)
        self.firefox_driver.find_element_by_xpath("//a[@data-type='oVirtPlatform']").click()
        # self.firefox_driver.find_element_by_xpath("//li[2]/*[@class='lnk-service_providers']").click()
        time.sleep(2)


        # To close UDS enterprise popup
        # assert "UDS Dashboard" in self.firefox_driver.title 
        # print("###################################")
        # self.firefox_driver.find_element_by_class_name("close").click()
        # self.firefox_driver.find_element_by_xpath("//div[@class='col-lg-3'][2]/div/a/div/div/div[@class='col-xs-10']").click()
        # time.sleep(1)
        # self.firefox_driver.find_element_by_class_name("close").click()
        # self.firefox_driver.find_element_by_xpath("//*[@class='label-tbl-button' and text()='New']").click()
        # time.sleep(1)
        # self.firefox_driver.find_element_by_xpath("//a[@data-type='oVirtPlatform']").click()
        # select_ovirt.select_by_visible_text(" oVirt/RHEV Platform Provider")
        # self.firefox_driver.find_element_by_xpath("//li[2]/*[@class='lnk-service_providers']").click()
        # time.sleep(2)
        # s.click()

    
if __name__ == "__main__":
    unittest.main()

