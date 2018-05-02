from selenium.webdriver.common.by import By
from page import BasePage
import sys
sys.path.append("..")
import models.logger
from models.logger import Logger
from screenshot import get_screenshot
logger='usercenter'
mylogger = Logger(logger).getlog()

class useraccountcenter(BasePage):
	usercenter_loc=(By.ID, "username")
	newcontactdialog_loc=(By.ID,"ctrl-e-esui8785972-title")
	createcontactbutton_loc=(By.XPATH,"//div/div/button[@id='ctrl-e-addContact']")


	newcontactname_loc=(By.ID,"ctrl-e-1-name-input")
	newcontactphone_loc=(By.ID, "ctrl-e-1-phone-input")
	newcontactconfirm_loc=(By.ID, "ctrl-e-btnFootOk")
	contactlist_loc=(By.XPATH, "//a[contains(@href,'#/contact/list')]")
	contactlisttab_loc=(By.XPATH, "//div[@class='detail-content']/ul/li[1]")
	grouplist_loc=(By.ID,"ctrl-e-1-groupId")
	contacttable_loc=(By.ID,"ctrl-e-table-body")
	selectallcontactbox_loc=(By.ID, "ctrl-e-table-select-all")
	deletecontactbutton_loc=(By.ID, "ctrl-e-deleteContacts")
	confrim_deletecontactbutton_loc=(By.ID, "ctrl-e-btnFootOk")
	cancel_deletecontactbutton_loc=(By.ID, "ctrl-e-btnFootCancel")
	contactpage_nodata_loc=(By.CLASS_NAME, "ui-table-body-nodata")

	def switch_to_contactlist(self):
		self.find_element(*self.contactlisttab_loc).click()

	def input_newcontactname(self, driver, newcontactname):
		self.find_element(*self.newcontactname_loc).send_keys(newcontactname)
		mylogger.info("input contact name")
		get_screenshot(driver,"input_newcontactname")

	def input_newcontactphone(self,newcontactphone):
		self.find_element(*self.newcontactphone_loc).send_keys(newcontactphone)
		mylogger.info("input contact phone")

	def newcontactDialog(self):
		self.find_element(*self.createcontactbutton_loc).click()
		mylogger.info("click 'create contact' button")

	def confirm_newcontact(self):
		self.find_element(*self.newcontactconfirm_loc).click()


	def delete_allcontacts(self):
		self.find_element(*self.selectallcontactbox_loc).click()
		buttonstatus=self.find_element(*self.deletecontactbutton_loc).get_attribute("disabled")
		
		if buttonstatus:
			mylogger.info("Button 'delete contact' is disabled")
			nodata_result=self.driver.find_element(*self.contactpage_nodata_loc).is_displayed()
			nodata_text=self.driver.find_element(*self.contactpage_nodata_loc).text
			if nodata_result:
				mylogger.info("%s displayed in contact table"%nodata_text)
			else:
				mylogger.info("%s is not displayed in contact table"%nodata_text)

		else:
			self.find_element(*self.deletecontactbutton_loc).click()
			self.find_element(*self.confrim_deletecontactbutton_loc).click()
			nodata_result=self.driver.find_element(*self.contactpage_nodata_loc).is_displayed()
			nodata_text=self.driver.find_element(*self.contactpage_nodata_loc).text
			if nodata_result:
				mylogger.info("%s displayed in contact table"%nodata_text)
			else:
				mylogger.info("%s is not displayed in contact table"%nodata_text)



	def delete_specifycontact(self, newcontactname):
		contact_table=self.find_element(*self.contacttable_loc)
		contact_table_row=contact_table.find_elements_by_tag_name("tr")
		mylogger.info("contact list table row number: %s"%len(contact_table_row))

		

		for i in range(0,len(contact_table_row)):
			contact_table_col=contact_table_row[0].find_elements_by_tag_name("td")
			mylogger.info("contact list table column number:%s"%len(contact_table_col))
			contact_text=contact_table_row[i].find_elements_by_tag_name("td")[1].text
			if contact_text==newcontactname:
				mylogger.info("contact %s existed in contact list"%newcontactname)
				contact_table_row[i].find_element_by_xpath("//td/div/span/input[@data-index=%s]"%i).click()
				self.find_element(*self.deletecontactbutton_loc).click()
				self.find_element(*self.confrim_deletecontactbutton_loc).click()
				break
		else:
			mylogger.info("%s not existing"%newcontactname)
			


	def selectgroup(self, groupprovidename):
		
		self.find_element(*self.grouplist_loc).click()
		grouplist=self.driver.find_elements_by_xpath("//li[@class='ui-select-item']")
		mylogger.info("%s group can be selected"%len(grouplist))
		row_valuelist=[]

		for i in range(0,len(grouplist)):
			groupprovide_name=grouplist[i].text
			if groupprovide_name==groupprovidename:
				grouplist[i].click()
				#print(groupprovide_name)
				break
		else:
			mylogger.warning("%s group name not found in list"%groupprovidename)

	def verify_contactexisting(self, newcontactname):
		contact_table=self.find_element(*self.contacttable_loc)
		contact_table_row=contact_table.find_elements_by_tag_name("tr")
		mylogger.info("contact list table row number: %s"%len(contact_table_row))

		for i in range(0,len(contact_table_row)):
			contact_table_col=contact_table_row[0].find_elements_by_tag_name("td")
			mylogger.info("contact list table column number:%s"%len(contact_table_col))
			contact_text=contact_table_row[i].find_elements_by_tag_name("td")[1].text
			if contact_text==newcontactname:
				mylogger.info("contact %s added successfuly"%newcontactname)
				break
		else:
			mylogger.info("%s not existing"%newcontactname)

		





class newgroup(BasePage):
	"""docstring for ClassName"""
	contactgroup_loc=(By.XPATH, "//a[contains(@href,'#/contact/group')]")
	contactgrouptab_loc=(By.XPATH, "//div[@class='detail-content']/ul/li[2]")
	newcontactgroupbutton_loc=(By.ID, "ctrl-e-addGroup")
	groupprovidename_loc=(By.ID, "ctrl-e-1-name-input")
	newgroupconfirm_loc=(By.ID,"ctrl-e-btnFootOk")
	table_loc=(By.ID, "ctrl-e-table")
	#nogroupdata_loc=(By.CSS_SELECTOR, ".ui-table-body-nodata")
	selectallitembox_loc=(By.ID,"ctrl-e-selectAllItems-box")
	deletegroupbutton_loc=(By.ID, "ctrl-e-deleteGroups")
	confirm_deletegroup_loc=(By.ID,"ctrl-e-btnFootOk")
	groupexistingtip_loc=(By.ID, "ctrl-e-1-name-validity")
	cancelnewgroupbutton_loc=(By.ID, "ctrl-e-btnFootCancel")
	newgroupdialogtitle_loc=(By.CLASS_NAME, "ui-dialog-title")
	grouppage_nodata_loc=(By.CLASS_NAME,"ui-table-body-nodata")



	def verify_deletegroupbuttonstatus(self):
		self.find_element(*self.selectallitembox_loc).click()
		return self.find_element(*self.deletegroupbutton_loc).get_attribute("data-ui-disabled")
	def switch_to_group(self):
		#self.find_element(*self.contactgroup_loc).click()
		contactgrouptab_status=self.find_element(*self.contactgrouptab_loc).get_attribute("class")
		if contactgrouptab_status=="ui-tab-item ui-tab-item-":
			self.find_element(*self.contactgrouptab_loc).click()

	def verify_newgroupdialog_displayed(self):
		self.find_element(*self.newcontactgroupbutton_loc).click()
		'''
		newgroupdialog_result=self.find_element(*self.newgroupdialogtitle_loc).is_displayed()
		if newgroupdialog_result:
			self.switch_to_a
			mylogger.info("new group dialog displayed")
		'''
		

	def input_providename(self, groupprovidename):
		self.find_element(*self.groupprovidename_loc).send_keys(groupprovidename)

	def confirm_newgroup(self):
		self.find_element(*self.newgroupconfirm_loc).click()

	def delete_allgroup(self):
		self.find_element(*self.selectallitembox_loc).click()
		buttonstatus=self.find_element(*self.deletegroupbutton_loc).get_attribute("disabled")

		if buttonstatus:
			nodata_result=self.driver.find_element(*self.grouppage_nodata_loc).is_displayed()
			nodata_text=self.driver.find_element(*self.grouppage_nodata_loc).text
			mylogger.info("Button 'delete group' is disabled")
			if nodata_result:
				mylogger.info("%s displayed in group table"%nodata_text)
			else:
				mylogger.info("%s is not displayed in group table"%nodata_text)
		else:
			self.find_element(*self.deletegroupbutton_loc).click()
			self.find_element(*self.confirm_deletegroup_loc).click()
			nodata_result=self.driver.find_element(*self.grouppage_nodata_loc).is_displayed()
			nodata_text=self.driver.find_element(*self.grouppage_nodata_loc).text
			if nodata_result:
				mylogger.info("%s displayed in group table, group has been deleted"%nodata_text)
			else:
				mylogger.info("%s is not displayed in group table"%nodata_text)



	def verify_newgroup(self,groupprovidename):

		table=self.find_element(*self.table_loc)
		table_rows=table.find_elements_by_tag_name('tr')
		mylogger.info("group list total rows:%s"%len(table_rows))

		talbe_cols=table_rows[0].find_elements_by_tag_name('td')
		mylogger.info("group list table total column:%s"%len(talbe_cols))


		for i in range(0,len(table_rows)):
			table_col2=table_rows[i].find_elements_by_tag_name('td')[1].text
			if table_col2==groupprovidename:
				mylogger.info("group %s added successfuly"%table_col2)
				break
		else:
			mylogger.info("group %s not existing"%table_col2)
			
	def Add_existinggroup(self,groupprovidename):
		#input_providename(groupprovidename)
		#confirm_newgroup()
		self.find_element(*self.groupprovidename_loc).send_keys(groupprovidename)
		self.find_element(*self.newgroupconfirm_loc).click()
		groupexistingtip_result=self.find_element(*self.groupexistingtip_loc).is_displayed()
		if groupexistingtip_result==True:
			return groupexistingtip_result
			groupexistingtip_text=self.find_element(*self.groupexistingtip_loc).text
			mylogger.info("tooltips when added the group existed: %s"%groupexistingtip_text)






'''
		for tr in table_tr_list:
			table_td_list=tr.find_elements(By.TAG_NAME, 'td')
			row_list=[]
			print(table_td_list)
			for td in table_td_list:
				row_list.append(td.text)
			table_list.append(row_list)


		for i in range(len(table_list)):
			for j in range(len(table_list[i])):
				if groupprovidename==table_list[i][j]:
					print("success add group %s"%groupprovidename)

'''	
	
			#row_valuelist.append(row_value)
		#print(row_valuelist)
		


