from overview_page import Overviewpage

def goto_ticketlist(driver):
	overviewpage=Overviewpage(driver,u"Baidu",u"Baidu Cloud")
	overviewpage.goto_ticketlistpage(driver)

def goto_createticket(driver):
	overviewpage=Overviewpage(driver,u"Baidu",u"Baidu Cloud")
	overviewpage.goto_createticketpage(driver)