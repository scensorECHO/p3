# This application will be used to access all the printers web-based portals. 
# In doing so, it will allow Benteler to submit user information for all printers from a single CLI application.
# All browser interaction will be directed by the splinter API, built on top of the selenium project.
# WebDriver still needs to be downloaded for Firefox due to an error loading a custom profile 
# on launch of a new Browser object. 

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from sys import stdin

title = dict({'A':2,'B':2,'C':3,'D':3,'E':4,'F':4,'G':5,'H':5,'I':6,'J':6,'K':6,'L':7,'M':7,
	'N':7,'O':8,'P':8,'Q':8,'R':9,'S':9,'T':9,'U':10,'V':10,'W':10,'X':11,'Y':11,'Z':11})
printers = []
employees = []
login = []

def sortTitle(n):
	return title.get(n[0],1);

def inputUserInfo():
	print('Would you like to enter an employee? Y/N')
	if(stdin.readline().strip('n').startswith('Y'))
		print('Enter the following information')
		name = input('Name (Last, First ): ').strip()
		key = name[:16]
		email = input('Email: ').strip()
		title = '1'
		title = sortTitle(name)

		employees.append(dict([('name',name), ('key',key), ('email',email), ('title',title)]))

		print(employees[0]['name'])
		print(employees[0]['key'])
		print(employees[0]['email'])
		print(employees[0]['title'])
		inputUserInfo()
	return 0;

with open('printer.list') as f:
    for line in f.readlines():
    	printers.append(line.rstrip())

printer = printers[0] 

inputUserInfo()

# commenting out all selenium functionality until recursive user prompt fixed

# # switched driver to selenium base driver for firefox
# driver = webdriver.Firefox()

# # for printer in printers #for future use with all printers
# url = "http://" + printer + "/web/guest/en/websys/webArch/authForm.cgi"
# driver.get(url)

# # locate login and password forms
# loginform = driver.find_element_by_id('userid_work')
# passwordform = driver.driver.find_element_by_id('password_work')

# # type in user credentials
# loginform.send_keys(login[0])
# passwordform.send_keys(login[1])

# # log in using given credential
# loginbutton = driver.find_element_by_link_text('Login')
# loginbutton.click() 

# # go to Address Book
# addrbook = driver.find_element_by_link_text('Address Book')
# addrbook.click()

# # go to detail input
# detailinput = driver.find_element_by_link_text('Detail Input')
# detailinput.click()

# # go to add user
# adduser = driver.find_element_by_link_text('Add User')
# adduser.click()

# # begin filling forms 
# name = driver.find_element_by_id('entryNameIn')
# name.click()
# name.send_keys( employees[0]['name'])

# displayName = driver.find_element_by_id('entryDisplayNameIn')
# displayName.click()
# displayName.send_keys(employees[0]['key'])

# title = driver.find_element_by_id('entryTagInfoIn')
# title.click()
# title.send_keys(employees[0]['title'])

# mailAddr = driver.find_element_by_id('mailAddressIn')
# mailAddr.click()
# mailAddr.send_keys(employees[0]['email'])

# # driver.screenshot('test.png') #old splinter code

# confirmbutton = driver.find_element_by_link_text('OK')
# confirmbutton.click()
