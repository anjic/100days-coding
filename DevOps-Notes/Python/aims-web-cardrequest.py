import time
#import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import odooselenium

#browser = webdriver.Firefox()
user = 'inrbae315'
password= 'password'
chrome_driver = webdriver.Chrome('c:/Users/canjaneyulu/Downloads/chromedriver_win32/chromedriver.exe') 
#chrome_driver.maximize_window()
ui=odooselenium.OdooUI(chrome_driver,base_url=u'http://aims.dev4srcm.org')

# Log in, ui.login('myusername', 'mypassword', 'mydatabase')
ui.login(user.upper(), password, 'aims')
#print ui.list_modules()
ui.go_to_module('AIMS')
ui.go_to_view('Web Card Request')
#print dir(ui)
# print type(ui.list_modules)
#print dir(ui)
with ui.wait_for_ajax_load():
	create_btn= chrome_driver.find_elements(By.XPATH,'//button[contains(text(), "Create")]')
	for btn in create_btn:
		btn.click()
		time.sleep(1)
	select_date = chrome_driver.find_elements(By.XPATH,'//img[@title="Select date"]')
	for date in select_date:
		date.click()
		time.sleep(1)
	now_btn= chrome_driver.find_elements(By.XPATH,'//button[contains(text(), "Now")]')
	for btn in now_btn:
		btn.click()
		time.sleep(1)
	center_input= chrome_driver.find_element_by_class_name('ui-autocomplete-input')
	center_input.send_keys('HYDERABAD')
	time.sleep(1)
	# center_select= chrome_driver.find_elements(By.XPATH,'//span[contains(text(),"HYDERABAD")]')
	# center_select.click()
	# time.sleep(3)
	name_on_card = chrome_driver.find_elements(By.XPATH,'//input[@id="oe-field-input-28"]')
	name_on_card.send_keys('INACAE124')
	time.sleep(1)

	# select_date.click()
# Toggle list view.
# assert ui.get_url_fragments()['view_type'] == u'kanban'
# list_view_button = webdriver.find_element(
#     By.CSS_SELECTOR,
#     ".oe_vm_switch_list")
# with ui.wait_for_ajax_load():
#     list_view_button.click()

# chrome_driver.get('http://aims.dev4srcm.org')
#title = "hello"
#assert title == chrome_driver.title
#time.sleep(1)
# elm_user= chrome_driver.find_element_by_id('login')
# elm_user.send_keys(user.upper())
# time.sleep(1)
# elm_password= chrome_driver.find_element_by_id('password')
# elm_password.send_keys(password)
# time.sleep(1)
# elm_login= chrome_driver.find_element(By.XPATH,"//button")
# elm_login.click()
# time.sleep(1)
chrome_driver.quit()
