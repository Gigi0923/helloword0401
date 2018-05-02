from selenium import webdriver
import unittest
import os
class MyTest(unittest.TestCase):
	def setUp(self):
		chrome_driver=os.path.abspath(r"C:\\Gigi\\baiduyunTest\\driver\\chromedriver.exe")
		os.environ["webdriver.chrome.driver"]=chrome_driver
		ie_dirver=os.path.abspath(r"C:\\Gigi\\baiduyunTest\\driver\\IEDriverServer.exe")
		os.environ["webdriver.ie.driver"]=ie_dirver
		self.driver=webdriver.Chrome(chrome_driver)
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()
		self.login_url="https://login.bce.baidu.com/"
		self.username="15900443703"
		self.password="zhuqiuge23@"
		self.login_url="https://login.bce.baidu.com/"
		self.newprovidename="gr4"
		self.newcontactname="Gi8"
		self.newcontactphone="15900443703"
		self.admin_username=""

	def tearDown(self):
		self.driver.quit()
