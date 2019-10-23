import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Selenium_Drivers(unittest.TestCase):
	def setUp(self):
		#print "Hello"
		# create a new Firefox session
		self.browser = webdriver.Chrome('c:/Users/canjaneyulu/Downloads/chromedriver_win32/chromedriver.exe')
		#self.browser.implicitly_wait(30)
		self.browser.maximize_window()
		# navigate to the application home page
		self.browser.get('http://seleniumhq.org/')
	def test_download_selenium(self):
		self.elm_projects= self.browser.find_element(By.XPATH, '//a[@title="Selenium Projects"]')
		self.elm_projects.click()
		#time.sleep(1)
		self.elm_webdiver= self.browser.find_element(By.XPATH,'//img[@src="/images/selenium-logo.png"]')
		self.elm_webdiver.click()
		#time.sleep(1)
		self.elm_download= self.browser.find_element(By.XPATH,'//div[@class="downloadBox"]')
		self.elm_download.click()
		time.sleep(1)
		self.ele_download_version= self.browser.find_element_by_link_text('3.141.59')
		self.ele_download_version.click()
		time.sleep(2)
	def test_selenium_documentation(self):
		self.document=self.browser.find_element_by_link_text('Documentation')
		self.document.click()
		self.python =self.browser.find_element(By.XPATH,'//input[@value="python"]')
		self.python.click()
		self.note = self.browser.find_element(By.XPATH,'//a[@href="00_Note_to-the-reader.jsp"]')
		self.note.click()
		time.sleep(2)
	def test_selenium_Web_Applications(self):
		self.document=self.browser.find_element_by_link_text('Documentation')
		self.document.click()
		self.python =self.browser.find_element(By.XPATH,'//input[@value="python"]')
		self.python.click()
		self.web_App= self.browser.find_element_by_link_text("Test Automation for Web Applications")
		self.web_App.click()
		time.sleep(2)
# close the browser window
	def tearDown(self):
		self.browser.quit()
if __name__ == '__main__':
	unittest.main()