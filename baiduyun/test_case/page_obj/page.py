# coding=utf-8
'''
created on 2018-3-6
@author: Gigi
project: base class

'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append("..")
import models.logger
from models.logger import Logger
import time

logger='BasePage'
mylogger = Logger(logger).getlog()

class BasePage(object):
	"""docstring for BasePage"""
	#
	def __init__(self, selenium_webdriver, base_url,pagetitle):
		self.driver = selenium_webdriver
		self.base_url=base_url
		self.pagetitle=pagetitle
		self.timeout=30

	def onpage(self, pagetitle):
		return pagetitle in self.driver.title
	#
	def _open(self, url, pagetitle):
		url=self.base_url
		self.driver.get(url)
		assert self.onpage(pagetitle), u"open page %s Failed"%url

	#
	def find_element(self, *loc):
		try:
			WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc))
			return self.driver.find_element(*loc)
		except:
			#print(u"%s page not found %s element"%(self, loc))
			mylogger.error("%s page not found %s element"%(self, loc))
			#mylogger.error("exction error is: %s"%msg)
			#self.driver.get_screenshot(self,selenium_webdriver)



	def _close(self):
		self.driver.close()


	def testclick(self,loc):
		try:
			loc=getattr(self, "_%s"% loc)
			self.find_element(*loc).click()
		except AttributeError:
			mylogger.error("%s page not found %s element"%(self, loc))

	def send_keys(self, loc, value, clear_first=True, click_first=True):
		try:
			loc=getattr(self,"_%s"% loc)
			if click_first:
				self.find_element(*loc).click()
			if clear_first:
				self.find_element(*loc).clear()
				self.find_element(*loc).send_keys(value)
		except AttributeError:
			#print(u"%s page not found %s element"%(self,loc))
			mylogger.error("%s page not found %s element"%(self, loc))



	def switch_to_alert(self,loc):
		return self.driver.switch_to_alert(loc)

'''
	def find_elements(self, *locs):
		try:
			WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locs))
			return self.driver.find_elements(*locs)
		except:
			print(u"%s page not found %s element"%(self, locs))
'''