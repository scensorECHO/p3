from splinter.browser import Browser
from sys import stdin


def sortTitle(n):
	c = n[0]
	if (c=='A') or (c=='A'):
		return '2';
	if (c=='C') or (c=='D'):
		return '3';
	if (c=='E') or (c=='F'):
		return '4';
	if (c=='G') or (c=='H'):
		return '5';
	if (c=='I') or (c=='J') or (c=='K'):
		return '6';
	if (c=='L') or (c=='M') or (c=='N'):
		return '7';
	if (c=='O') or (c=='P') or (c=='Q'):
		return '8';
	if (c=='R') or (c=='S') or (c=='T'):
		return '9';
	if (c=='U') or (c=='V') or (c=='W'):
		return '10';
	if (c=='X') or (c=='Y') or (c=='Z'):
		return '11';
	else:
		return '1';


printers = open('printer.list','r').read().splitlines()
printer = printer[0]
login = open('login.info','r').read().splitlines()

employees = []

print('Would you like to enter an employee? Y/N')
while( stdin.readline().strip('n').startswith('Y')):
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

	print('Would you like to enter another employee? Y/N')

browser = Browser('firefox', profile='splinter')
url = "http://" + printer + "/web/guest/en/websys/webArch/authForm.cgi"
browser.visit(url)
browser.fill('userid_work',login[0])
browser.fill('password_work',login[1])
browser.find_link_by_text('Login').first.click()
browser.find_link_by_text('Address Book').first.click()
browser.find_link_by_text('Detail Input').first.click()
browser.find_link_by_text('Add User').first.click()
browser.fill('entryNameIn', employees[0]['name'])
browser.fill('entryDisplayNameIn',employees[0]['key'])
browser.select('entryTagInfoIn',employees[0]['title'])
browser.fill('mailAddressIn',employees[0]['email'])
browser.screenshot('test.png')
browser.find_link_by_text('OK').first.click()
