from selenium import webdriver
import time
import os
import os.path
def get_screenshot(self,funct):
	test_dir='./'
	screenshot_path=test_dir+'screenshot/'
	nowTime=time.strftime("%Y-%m-%d %H_%M_%S")
	self.get_screenshot_as_file(screenshot_path+"%s_%s.png"%(nowTime,funct))