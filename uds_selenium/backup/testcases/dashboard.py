import unittest
from selenium import webdriver
import time
import os 
import sys 
lib_path = os.path.abspath('../') 
sys.path.insert(0,lib_path)
from common.browser_creation import Browser_creation
# from testcases.login import Uds_login

class Dashboard_Uds(Browser_creation):

    def test_dashboard(self):
        print 'test dash'
        # # super(Dashboard_Uds, self).test_login() 
        # # Uds_login().test_login()
        # assert "UDS Dashboard" in self.firefox_driver.title 
        # self.firefox_driver.find_element_by_class_name("close").click()
        # # self.firefox_driver.find_element_by_xpath("//div[@class='side-nav']/ul/li[2]/a[@class='lnk-service_providers']").click()
        # # assert "UDS Dashboard" in self.firefox_driver.title 
        # print("###################################")
        # # self.firefox_driver.find_element_by_class_name("close").click()
        # self.firefox_driver.find_element_by_xpath("//div[@class='col-lg-3'][2]/div/a/div/div/div[@class='col-xs-10']").click()
        # time.sleep(1)
        # self.firefox_driver.find_element_by_class_name("close").click()
        # self.firefox_driver.find_element_by_xpath("//*[@class='label-tbl-button' and text()='New']").click()
        # time.sleep(1)
        # self.firefox_driver.find_element_by_xpath("//a[@data-type='oVirtPlatform']").click()
        # # self.firefox_driver.find_element_by_xpath("//li[2]/*[@class='lnk-service_providers']").click()
        # time.sleep(2)


if __name__ == "__main__":
    # dashborad = Dashboard_Uds()
    # dashborad.test_login()
    unittest.main()