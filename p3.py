# This application will be used to access all the printers web-based portals. 
# In doing so, it will allow Benteler to submit user information for all printers from a single CLI application.
# All browser interaction will be directed by the splinter API, built on top of the selenium project.
# WebDriver still needs to be downloaded for Firefox due to an error loading a custom profile 
# on launch of a new Browser object. 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import ChromeOptions
from sys import stdin

titleDict = dict({'A':2,'B':2,'C':3,'D':3,'E':4,'F':4,'G':5,'H':5,'I':6,'J':6,'K':6,'L':7,'M':7,
	'N':7,'O':8,'P':8,'Q':8,'R':9,'S':9,'T':9,'U':10,'V':10,'W':10,'X':11,'Y':11,'Z':11})
printers = []
employees = []
login = []

def sortTitle(n):
	return titleDict.get(n[0],1);

def inputUserInfo(count=0):
	print 'Employees entered so far: ',count
	userInput = raw_input('Would you like to enter an employee? Y/N: ').strip('n').startswith('Y')
	if(userInput):
		print('Enter the following information')
		name = raw_input('Name (Last, First ): ').strip()
		key = name[:16]
		email = raw_input('Email: ').strip()
		title = '1'
		title = sortTitle(name)
		employees.append(dict([('name',name), ('key',key), ('email',email), ('title',title)]))
		print(employees[count]['name'])
		print(employees[count]['key'])
		print(employees[count]['email'])
		print(employees[count]['title'])
		count += 1
		return inputUserInfo(count);
	return len(employees);

with open('printer.list') as f:
    for line in f.readlines():
    	printers.append(line.rstrip())

numEntries = inputUserInfo()

print 'There was a total of ', numEntries, ' entered'

printer = printers[0] 

####################################################
##########SELENIUM BROWSER INTERACTION##############
####################################################

# switched driver to selenium base driver for firefox

# load default profile manually
options = ChromeOptions()
options.addArguments('user-data-dir=C:\Users\Carrio\AppData\Local\Google\Chrome\User Data\Default')

# driver = webdriver.Firefox() # trying out chrome
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe', 0, options)

# for printer in printers #for future use with all printers
url = "http://" + printer + "/web/guest/en/websys/webArch/authForm.cgi"
driver.get(url)

# locate login and password forms
loginform = driver.find_element_by_id('userid_work')
passwordform = driver.driver.find_element_by_id('password_work')

# type in user credentials
loginform.send_keys(login[0])
passwordform.send_keys(login[1])

# log in using given credential
loginbutton = driver.find_element_by_link_text('Login')
loginbutton.click() 

# go to Address Book
addrbook = driver.find_element_by_link_text('Address Book')
addrbook.click()

# go to detail input
detailinput = driver.find_element_by_link_text('Detail Input')
detailinput.click()

# go to add user
adduser = driver.find_element_by_link_text('Add User')
adduser.click()

# begin filling forms 
name = driver.find_element_by_id('entryNameIn')
name.click()
name.send_keys( employees[0]['name'])

displayName = driver.find_element_by_id('entryDisplayNameIn')
displayName.click()
displayName.send_keys(employees[0]['key'])

title = driver.find_element_by_id('entryTagInfoIn')
title.click()
title.send_keys(employees[0]['title'])

mailAddr = driver.find_element_by_id('mailAddressIn')
mailAddr.click()
mailAddr.send_keys(employees[0]['email'])

confirmbutton = driver.find_element_by_link_text('OK')
confirmbutton.click()
