from splinter.browser import Browser
from sys import stdin


def sortTitle(n):
	if (n[0]=='A') or (n[0]=='A'):
		return '2';
	if (n[0]=='C') or (n[0]=='D'):
		return '3';
	if (n[0]=='E') or (n[0]=='F'):
		return '4';
	if (n[0]=='G') or (n[0]=='H'):
		return '5';
	if (n[0]=='I') or (n[0]=='J') or (n[0]=='K'):
		return '6';
	if (n[0]=='L') or (n[0]=='M') or (n[0]=='N'):
		return '7';
	if (n[0]=='O') or (n[0]=='P') or (n[0]=='Q'):
		return '8';
	if (n[0]=='R') or (n[0]=='S') or (n[0]=='T'):
		return '9';
	if (n[0]=='U') or (n[0]=='V') or (n[0]=='W'):
		return '10';
	if (n[0]=='X') or (n[0]=='Y') or (n[0]=='Z'):
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
