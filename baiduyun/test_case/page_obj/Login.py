# coding=utf-8
'''
created on 2018-3-
@author: Gigi
project: base class
'''
from selenium.webdriver.common.by import By

from page import BasePage

class LoginPage(BasePage):
	"""docstring for LoginPage"""
	# find element
	#userinfologin_loc=(By.ID, "TANGRAM__PSP_4__footerULoginBtn")
	baiduaccountlogin_form_loc=(By.CSS_SELECTOR, "div>a.passport-account")
	username_loc=(By.NAME, "userName")
	userpassword_loc=(By.NAME, "password")
	#rememberpass_loc=(By.ID, "TANGRAM__PSP_4__memberPass")
	submit_loc=(By.ID, "TANGRAM__PSP_4__submit")
	span_loc=(By.ID, "TANGRAM__PSP_4__error")
#	rebindGuideCancel_loc=(By.ID,"TANGRAM__PSP_29__rebindGuideCancel")
#	rebindGuideForward_loc=(By.ID, "TANGRAM__PSP_29__rebindGuideRebind")
#	MemberCenter_loc=(By.LINK_TEXT, "会员中心")
	region_loc=(By.CSS_SELECTOR, ".region-text region-global")
	userinfo_loc=(By.XPATH, "//div[@class='header-select user-info']/a")

	baiduaccountlogin_error_hint_loc=(By.ID, "TANGRAM__PSP_4__error")


    #百度账号登录Action
	def switch_to_baidulogin_form(self):
		self.find_element(*self.baiduaccountlogin_form_loc).click()
	def input_username(self, username):
		#self.find_element(*self.username_loc).clear()
		self.find_element(*self.username_loc).send_keys(username)
	def input_password(self, password):
		self.find_element(*self.userpassword_loc).send_keys(password)
	def submit(self):
		self.find_element(*self.submit_loc).click()
	def show_userinfo(self):
		return self.find_element(*self.userinfo_loc).title


	#百度账号登录错误提示
	def baiduaccountlogin_error_hint(self):
		return self.find_element(*self.baiduaccountlogin_error_hint_loc).text


	#云账号登录

	uclogin_form_loc=(By.ID, "choose-uc-login")
	uc_username_loc=(By.ID, "uc-common-account")
	uc_password_loc=(By.ID, "ucsl-password-edit")
	uc_token_loc=(By.ID, "uc-common-token")
	uc_submit_loc=(By.ID, "submit-form")

	uc_username_error_hint_loc=(By.ID, "account-error")
	uc_password_error_hint_loc=(By.ID, "password-error")
	uc_token_error_hint_loc=(By.ID, "token-error")

	#云账号登录action
	def switch_to_uclogin_form(self):
		self.find_element(*self.uclogin_form_loc).click()

	def input_uclogin_username(self, username):
		self.find_element(*self.uc_username_loc).send_keys(username)

	def input_uclogin_password(self,password):
		self.find_element(*self.uc_password_loc).send_keys(password)

	def input_uclogin_token(self,token):
		self.find_element(*self.uc_token_loc).send_keys(token)

	def uclogin_submit(self):
		self.find_element(*self.uc_submit_loc).click()

	def uclogin_username_error_hint(self):
		return self.find_element(*self.uc_username_error_hint_loc).text

	def uclogin_password_error_hint(self):
		return self.find_element(*self.uc_password_error_hint_loc).text

	def uclogin_token_error_hint(self):
		return self.find_element(*self.uc_token_error_hint_loc).text



'''
	def Cancel_rebind(self, rebindGuideCancel_loc):
		self.find_element(*self.rebindGuideCancel_loc).click()
	def forward_rebind(self, rebindGuideForward_loc):
		self.find_element(*self.rebindGuideForward_loc).click()

'''

