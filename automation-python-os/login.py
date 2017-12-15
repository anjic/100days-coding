
class Login_xio(object):
	"""docstring for Login_xio"""
	def __init__(self):
		#super(Login_xio, self).__init__()
		
		
	def user_login(self):
		#self.user = username
		#self.pwd = password
		driver = webdriver.Firefox()
		driver.maximize_window()
		driver.get("http://localhost:4200")
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
		




