from Login import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time

def test_cloudaccount_login(driver, login_url, username, password, token):
	login_page=LoginPage(driver, login_url, u"百度云-登录")
	login_page._open(login_url, u"百度云-登录")
	login_page.switch_to_uclogin_form()
	login_page.input_uclogin_username(username)
	login_page.input_uclogin_password(password)
	#get_screenshot(driver, "login_page")
	login_page.input_uclogin_token(token)
	login_page.uclogin_submit()

def test_user_login(driver, login_url, username, password):
	login_page=LoginPage(driver, login_url, u"百度云-登录")
	login_page._open(login_url, u"百度云-登录")
	'''
	js="window.scrollTo(100, 450);"
	driver.execute_script(js)
	sleep(3)
	js="var q=document.getElementById(\"TANGRAM__PSP_4__userName\");q.style.border=\"1px solid red\";"
	driver.execute_script(js)
	sleep(3)
	'''
	login_page.input_username(username)
	login_page.input_password(password)
	#get_screenshot(driver, "login_page")
	login_page.submit()
	#get_screen1shot(driver)

