from selenium.webdriver.common.by import By
from page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest
import sys
sys.path.append("..")
import models.logger
from models.logger import Logger
from screenshot import get_screenshot
import os
logger='Overviewpage'
mylogger = Logger(logger).getlog()

def goto_customnavigition(driver):
	overviewpage=Overviewpage(driver,u"Baidu",u"Baidu Cloud")
	overviewpage.Verify_onoverviewpage()
	overviewpage.customNavigation(driver)


class Overviewpage(BasePage):
	"""docstring for ClassName"""
	useraccount_loc=(By.ID, "username")
	#ticket_loc=(By.CSS_SELECTOR, ".iconfont icon-ticket")
	#ticket_loc=(By.CSS_SELECTOR, "div.ticket-nav>i.iconfont icon-ticket")
	ticket_loc=(By.CLASS_NAME, "ticket-nav")
	createticket_loc=(By.XPATH, "//div[@id='ticketList']/p/a[@data-action='create']")
	ticketlist_loc=(By.XPATH, "//div[@id='ticketList']/p/a[@data-action='more']")
	ticketlisttext_loc=(By.CSS_SELECTOR, ".list-content")
	createtickettext_loc=(By.CSS_SELECTOR, ".main-card-title")
	tickettype_loc=(By.CSS_SELECTOR, "span#ctrl-t-questionType-text")
	tickettypecontent_loc=(By.CSS_SELECTOR, "ol.ui-selectex-list")
	introjstooltip_loc=(By.CSS_SELECTOR, ".introjs-tooltip header-intro")
	introjstooltipclosebutton_loc=(By.CSS_SELECTOR, "div>a.introjs-button introjs-skipbutton")
	introjstooltiptext_loc=(By.CSS_SELECTOR, ".introjs-tooltiptext")
	introjsnextbutton_loc=(By.XPATH, "//div/a[@class='introjs-button introjs-nextbutton']")
	overviewbar_loc=(By.CSS_SELECTOR, "i.iconfont icon-overview")
	billingnav_loc=(By.CSS_SELECTOR, "div.billing-nav")
	customNav_loc=(By.CSS_SELECTOR, ".custom-nav")
	customNavtitle_loc=(By.CSS_SELECTOR, ".ui-dialog-title")
	checkboxes_loc=(By.CSS_SELECTOR, "input[type=checkbox]")
	customNavconfirm_loc=(By.ID, "ctrl-default-btnFootOk")


	def above_mouse(self, driver):
		introjstooltip_status=self.find_element(*self.introjsnextbutton_loc).is_displayed()
		if introjstooltip_status:
			self.find_element(*self.introjsnextbutton_loc).click()
			self.find_element(*self.introjsnextbutton_loc).click()
			self.find_element(*self.introjsnextbutton_loc).click()
			sleep(3)
		user_above=self.find_element(*self.useraccount_loc)
		ActionChains(self.driver).move_to_element(user_above).perform()

	def customNavigation(self,driver):
		introjstooltip_status=self.find_element(*self.introjsnextbutton_loc).is_displayed()
		if introjstooltip_status:
			self.find_element(*self.introjsnextbutton_loc).click()
			self.find_element(*self.introjsnextbutton_loc).click()
			self.find_element(*self.introjsnextbutton_loc).click()
			sleep(3)
		self.find_element(*self.customNav_loc).click()
		#customNavigationstatus=self.find_element(*self.customNavtitle_loc).is_displayed()
		checkboxes=self.driver.find_elements_by_css_selector("input[type=checkbox]")
		for checkbox in checkboxes:
			checkbox.click()
			sleep(1)
		self.find_element(*self.customNavconfirm_loc).click()




	def goto_usercenterpage2(self):
		#js=document.getElementByClassName("introjs-tooltip header-intro").click()
		#self.driver.execute_script(js)
		self.find_element(*self.billingnav_loc).click()
		#self.find_element(*self.overviewbar_loc).click()
		sleep(2)
		#self.find_element(*self.overviewbar_loc).click()
		self.find_element(*self.useraccount_loc).click()
		'''
		introjstooltip_status=self.find_element(*self.introjstooltip_loc).is_displayed()

		if introjstooltip_status:
			self.find_element(*self.introjstooltipclosebutton_loc).click()
			self.find_element(*self.useraccount_loc).click()
		else:
			self.find_element(*self.useraccount_loc).click()
		'''
	def goto_usercenterpage(self):
		introjstooltip_status=self.find_element(*self.introjsnextbutton_loc).is_displayed()
		if introjstooltip_status:
			self.find_element(*self.introjsnextbutton_loc).click()
			self.find_element(*self.introjsnextbutton_loc).click()
			self.find_element(*self.introjsnextbutton_loc).click()
			sleep(3)
		self.find_element(*self.useraccount_loc).click()


	def Verify_onoverviewpage(self):
		useraccount_text=self.find_element(*self.useraccount_loc).text
		assert useraccount_text=="可", "user is not on overview page"


	def goto_ticketlistpage(self,driver):
		#self.find_element(*self.ticket_loc).click()
		above=self.find_element(*self.ticket_loc)
		ActionChains(driver).move_to_element(above).perform()
		get_screenshot(driver,"ticket")
		self.find_element(*self.ticketlist_loc).click()
		sleep(3)
		
		window_1=driver.current_window_handle
		windows=driver.window_handles
		for current_window in windows:
			if current_window!=window_1:
				driver.switch_to.window(current_window)
		sleep(3)
		get_screenshot(driver, "allticketlist")
		try:
			ticketlist_status=self.find_element(*self.ticketlisttext_loc).is_displayed()
			self.assertTrue(ticketlist_status, "'tiket list' text not existed")

		except:
			pass

		


	def goto_createticketpage(self,driver):
		#self.find_element(*self.ticket_loc).click()
		above=self.find_element(*self.ticket_loc)
		ActionChains(driver).move_to_element(above).perform()
		get_screenshot(driver,"ticket")
		self.find_element(*self.createticket_loc).click()
		sleep(3)
		get_screenshot(driver, "createticket")
		window_1=driver.current_window_handle
		windows=driver.window_handles
		for current_window in windows:
			if current_window!=window_1:
				driver.switch_to.window(current_window)
		sleep(3)

		ticketlist_status=self.find_element(*self.createtickettext_loc).is_displayed()
		mylogger.info("%s"%ticketlist_status)
		self.createticket(driver)
	
	def createticket(self, driver):
		tickettyperow=len(self.driver.find_elements_by_xpath("//span[@id='ctrl-t-questionType-text']"))
		self.driver.find_element_by_id("ctrl-t-questionType").click()
		self.driver.find_element_by_xpath("//div/ol/li[@data-index='3']").click()
		self.driver.find_element_by_xpath("//ul/li[@data-index='3.0']").click()
		self.driver.find_element_by_css_selector("#ctrl-t-typeFeatureId-text").click()
		self.driver.find_element_by_xpath("//ol[@id='ctrl-t-typeFeatureId-layer']/li[@data-index='1']").click()
		self.driver.find_element_by_id("ctrl-t-questionTitle-input").send_keys("test")
		xf=self.driver.find_element_by_xpath("//div[@id='edui3_body']/div/iframe")
		self.driver.switch_to.frame(xf)
		self.driver.find_element_by_xpath("//div/form/input[@name='undefined']").send_keys("C:\\Users\\zhuq\\Desktop\\0509\\Capture.PNG")
		self.driver.switch_to.parent_frame()
		self.driver.find_element_by_id("use-default-phone").click()
		self.driver.find_element_by_id("use-default-email").click()
		self.driver.find_element_by_class_name("webuploader-element-invisible").send_keys("C:\\Users\\zhuq\\Desktop\\1122\\Capture.PNG")
		sleep(2)
		self.driver.find_element_by_id("ticketSubmit").click()




		#tickettyperow1=len(self.driver.find_elements_by_xpath("//div/ol[class='ui-selectex-list']"))
		#tickettyperow2=len(self.driver.find_elements_by_xpath("//div/ol[class='ui-selectex-list']/li"))
		#mylogger.info("ticket type row %s"%tickettyperow)
		#mylogger.info("ticket type row1 %s"%tickettyperow1)
		#mylogger.info("ticket type row2 %s"%tickettyperow2)


