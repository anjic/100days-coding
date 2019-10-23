import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#browser = webdriver.Firefox()
driver = webdriver.Chrome('c:/Users/canjaneyulu/Downloads/chromedriver_win32/chromedriver.exe') 
driver.maximize_window()
driver.get('http://seleniumhq.org/')
assert "Web Browser Automation" in driver.title
time.sleep(1)
elm_projects= driver.find_element(By.XPATH, '//a[@title="Selenium Projects"]')
elm_projects.click()
time.sleep(1)
elm_webdiver= driver.find_element(By.XPATH,'//img[@src="/images/selenium-logo.png"]')
elm_webdiver.click()
time.sleep(1)
elm_download= driver.find_element(By.XPATH,'//div[@class="downloadBox"]')
elm_download.click()
time.sleep(1)
ele_download_version= driver.find_element_by_link_text('3.141.59')
ele_download_version.click()
time.sleep(2)
driver.close()