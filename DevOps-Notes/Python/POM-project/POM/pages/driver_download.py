class Login():
	"""docstring for Login"""
	def __init__(self, browser):
		#super(Login, self).__init__()
		self.browser = browser
		self.elm_projects_xpath= '//a[@title="Selenium Projects"]'
		self.elm_webdiver_xpath = '//img[@src="/images/selenium-logo.png'
		self.elm_download_xpath = '//div[@class="downloadBox"]'
		self.ele_download_version_link_text= '3.141.59'

	def download_selenium_driver(self):
		self.browser.find_element(By.XPATH,self.elm_projects_xpath).click()
		self.browser.find_element(By.XPATH,self.elm_webdiver_xpath).click()
		