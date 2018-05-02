from Login import LoginPage
from usercenter import useraccountcenter
from usercenter import newgroup
from overview_page import Overviewpage
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
from selenium.webdriver.common.action_chains import ActionChains

def add_new_contact(driver, newcontactname, newcontactphone, newprovidename):
	usercenter_page=useraccountcenter(driver,newcontactname, newcontactphone)
	usercenter_page.switch_to_contactlist()
	#get_screenshot(driver,"switch_to_contactlist")
	sleep(5)
	usercenter_page.delete_specifycontact(newcontactname)
	#get_screenshot(driver, "delete_specifycontact")
	sleep(3)
	usercenter_page.newcontactDialog()	
	usercenter_page.input_newcontactname(driver, newcontactname)
	usercenter_page.input_newcontactphone(newcontactphone)
	usercenter_page.selectgroup(newprovidename)
	#get_screenshot(driver, "selectgroup")
	usercenter_page.confirm_newcontact()
	sleep(5)
	usercenter_page.verify_contactexisting(newcontactname)

def add_new_group(driver, newprovidename):
 	new_group_page=newgroup(driver, newprovidename, u"Baidu Cloud")
 	new_group_page.switch_to_group()
 	#status=new_group_page.verify_deletegroupbuttonstatus()
 	#print(status)
 	'''
 	if status=="true":
 		new_group_page.delete_allgroup()
 	else:
 		new_group_page.delete_allgroup()
 	'''
 	new_group_page.verify_newgroupdialog_displayed()
 	new_group_page.input_providename(newprovidename)
 	new_group_page.confirm_newgroup()
 	#new_group_page.verify_newgroup(newprovidename)

def delete_all_group(driver):
 	new_group_page=newgroup(driver,u"baidu", u"Baidu Cloud")
 	new_group_page.switch_to_group()
 	new_group_page.delete_allgroup()

def delete_all_contacts(driver):
	usercenter_page=useraccountcenter(driver,u"baidu", u"Baidu Cloud")
	usercenter_page.switch_to_contactlist()
	usercenter_page.delete_allcontacts()

def goto_usercenter(driver):
	overviewpage=Overviewpage(driver,u"Baidu",u"Baidu Cloud")
	overviewpage.Verify_onoverviewpage()

	#overviewpage.goto_usercenterpage()
	overviewpage.goto_usercenterpage()


