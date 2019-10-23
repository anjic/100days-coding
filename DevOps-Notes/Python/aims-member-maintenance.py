import time
#import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import odooselenium

#browser = webdriver.Firefox()
user = 'inrbae315'
password= 'password'
chrome_driver = webdriver.Chrome('c:/Users/canjaneyulu/Downloads/chromedriver_win32/chromedriver.exe') 
chrome_driver.maximize_window()
ui=odooselenium.OdooUI(chrome_driver,base_url=u'http://aims.dev4srcm.org')

# Log in, ui.login('myusername', 'mypassword', 'mydatabase')
ui.login(user.upper(), password, 'aims')
#print ui.list_modules()
with ui.wait_for_ajax_load():
	ui.go_to_module('AIMS')
	ui.go_to_view('Member Maintenance')
	# time.sleep(6)
# with ui.wait_for_ajax_load():
	user_name= chrome_driver.find_element(By.XPATH,'//table/tbody/tr[9]')
	user_name.click()
	time.sleep(2)
	# edit_btn = chrome_driver.find_element_by_css_selector('button.oe_button.oe_form_button_edit')
	# edit_btn = chrome_driver.find_element(By.XPATH,'//span[@class="oe_form_buttons_view"]/div/button')
	edit_btn = chrome_driver.find_element(By.XPATH,'//button[contains(text(),"Edit")]')
	edit_btn.click()
	user_title= chrome_driver.find_element(By.XPATH,'//select/option[@value="21"]')
	user_title.click()
	time.sleep(1)
	user_prefix= chrome_driver.find_element(By.XPATH,'//input[@placeholder="Prefix.."]')
	user_prefix.clear()
	user_prefix.send_keys('jesus')
	time.sleep(1)
	user_midldle= chrome_driver.find_element(By.XPATH,'//input[@placeholder="Middle Name (if any).."]')
	user_midldle.clear()
	user_midldle.send_keys('kulan')
	time.sleep(1)
	# user_center= chrome_driver.find_element_by_class_name('ui-autocomplete-input')
	# user_center.send_keys('HYDERABAD')
	user_SRCM_learnt= chrome_driver.find_element(By.XPATH,'//td/span[@class="oe_form_field oe_form_field_char"]/input[@maxlength="64"]')
	user_SRCM_learnt.send_keys('from old abhyasis')
	time.sleep(1)
	user_title= chrome_driver.find_element(By.XPATH,'//button[@accesskey="S"]')
	user_title.click()
	time.sleep(1)
chrome_driver.close()