from page import BasePage
from selenium.webdriver.common.by import By

class useradminstration(BasePage):
	multiluseraccess_menu_loc=(By.XPATH, "//ul/li[@title='Mulit User Access']/a")
	multiuseraccess_title_loc=(By.CSS_SELECTOR, "div>ul>li>span.normal-title")
	adduser_button_loc=(By.CSS_SELECTOR, "span.ui-button-label")
	adduserdialog_title_loc=(By.CSS_SELECTOR, "div.ui-dialog-title>span")
	adduserdialog_username_loc=(By.ID, "ctrl-n-name-input")
	adduserdialog_username_hint_loc=(By.ID, "ctrl-n-name-validity")
	adduserdialog_confirmbutton_loc=(By.XPATH, "//div[@class='ui-dialog-foot ui-dialog-foot-panel']/div/div")
	adduserdialog_checkbox_loc=(By.ID, "ctrl-n-roles-box-0")
	IAMuser_link_loc=(By.XPATH, "//div/span/a[@href='http://d46b97862b454f01bc82ffcbcaed86c5.login.bce.baidu.com']")
	IAMuser_title_hint_loc=(By.XPATH, "//div/a/span")


	def goto_useradminpage(self):
		self.find_element(*self.multiluseraccess_menu_loc).click()

	def multiluseraccess_title_hint(self):
		return self.find_element(*self.multiuseraccess_title_loc).text

	def add_newuser(self):
		self.find_element(*self.adduser_button_loc).click()

	def addnewuser_dialog_title_hint(self):
		return self.find_element(*self.adduserdialog_title_loc).text

	def addnewuser_dialog_username_hint(self):
		return self.find_element(*self.adduserdialog_username_hint_loc).text

	def input_addnewusername(self, admin_username):
		self.find_element(*self.adduserdialog_username_loc).send_keys(admin_username)

	def input_addnewuserrole(self):
		self.find_element(*self.adduserdialog_checkbox_loc).click()

	def confirm_addnewuser(self):
		self.find_element(*self.adduserdialog_confirmbutton_loc).click()

	def goto_IAMUserLogin(self, driver):
		self.find_element(*self.IAMuser_link_loc).click()

		window1=driver.current_window_handle
		#print(window1)
		windows=driver.window_handles
		for current_window in windows:
			if current_window!=window1:
				driver.switch_to.window(current_window)
				#print(current_window)

	def IAMuser_title_hint(self):
		return self.find_element(*self.IAMuser_title_hint_loc).text

	def driver_back(self, driver):
		self.driver.back()

	def driver_forward(self, driver):
		self.driver.forward()
	










