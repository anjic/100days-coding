from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
from selenium import webdriver as driver


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://localhost:4200")
#driver.wait(4)
user = driver.find_element_by_xpath('//input[@placeholder="Username"]')
user.clear()
user.send_keys('Administrator')
print("username value passed.......")
pwd = driver.find_element_by_xpath('//input[@placeholder="Password"]')
pwd.clear()
pwd.send_keys('made4you')
print('Password value passed....')

submit=driver.find_element_by_xpath('//button[@type="submit"]')
submit.click()

#driver.wait(5)
driver.implicitly_wait(10)

driver.close()

#WebDriverWait wait = new WebDriverWait(driver, 30); wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("Username")));
#driver.get(By.xpath,'//button[@type="submit"]')
#driver.close()
