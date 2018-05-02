from selenium import webdriver
import time
from time import sleep
import sys
sys.path.append("./page_obj")
sys.path.append("./models")
from models import myunit
import unittest
from page_obj.mulituseraccess import useradminstration
from page_obj.overview_page import Overviewpage
from page_obj.user_login import test_user_login

class test_useradmin(myunit.MyTest):
	''
	def test_gotouseradminpage(self):
		test_user_login(self.driver, self.login_url, self.username, self.password)
		overviewpage=Overviewpage(self.driver,u"Baidu",u"Baidu Cloud")
		overviewpage.above_mouse(self.driver)
		useradminstrationpage=useradminstration(self.driver,u"Baidu",u"Baidu Cloud")
		useradminstrationpage.goto_useradminpage()
		self.assertEqual(useradminstrationpage.multiluseraccess_title_hint(), u"Mulit User Access")
		useradminstrationpage.goto_IAMUserLogin(self.driver)
		self.assertEqual(useradminstrationpage.IAMuser_title_hint(), u"IAM用户登录")
	'''
	def test_addnewuser1(self):
		test_user_login(self.driver, self.login_url, self.username, self.password)
		sleep(3)
		overviewpage=Overviewpage(self.driver,u"Baidu",u"Baidu Cloud")
		overviewpage.above_mouse(self.driver)
		useradminstrationpage=useradminstration(self.driver,u"Baidu",u"Baidu Cloud")
		useradminstrationpage.goto_useradminpage()
		useradminstrationpage.add_newuser()
		sleep(2)
		useradminstrationpage.input_addnewusername(self.admin_username)
		useradminstrationpage.confirm_addnewuser()
		self.assertEqual(useradminstrationpage.addnewuser_dialog_username_hint(), u"请填写用户名")
	'''

if __name__ == '__main__':
	unittest.main()
