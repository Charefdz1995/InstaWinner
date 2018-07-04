import time
from selenium import webdriver
from InstaWinner.settings import STATICFILES_DIRS
import yaml
from random import randint
from math import ceil
def login(driver,username,password):
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(2)
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    elements = driver.find_elements_by_xpath("//*[contains(text(), 'Log in')]")
    element  = elements[0]
    element.click()
    time.sleep(2)
    return driver

def get_profile(driver):
	time.sleep(2)
	code_url = str(STATICFILES_DIRS[0])+"/security.yaml"
	try :
		driver.find_element_by_link_text('Profile')
	except :
		driver.find_element_by_xpath("//button[text()='Send Security Code']").click()
		while True :
			if (security_code(code_url)!= None):
				time.sleep(2)
				driver.find_element_by_id('security_code').send_keys(security_code(code_url))
				time.sleep(2)
				reset(code_url)
				driver.find_element_by_xpath("//button[text()='Submit']").click()
				time.sleep(2)
				driver.find_element_by_link_text('Profile').click()
				break 
	return driver

def security_code(path):
	code  = None 
	try :
		with open(path,'r') as file : 
			data = yaml.load(file)
			code = data.get('code')
	except :
		code = None  
		print('waiting for security code')
	
	return code

def reset(path):
	data = dict(code = None)
	def quoted_presenter(dumper, data):
		return dumper.represent_scalar('tag:yaml.org,2002:str', data, style="'")
	yaml.add_representer(str, quoted_presenter)

	with open(path,'w') as file :
		yaml.dump(data,file,default_flow_style=False)

def get_followers(driver):
	driver.find_element_by_link_text('Profile').click()
	time.sleep(5)
	driver.find_element_by_partial_link_text(" followers").click()
	time.sleep(2)
	xpath = ("//a[@style='width: 30px; height: 30px;']")
	x = 0
	y = 500
	followers_num_element  = driver.find_elements_by_xpath('//span[@class ="g47SY "]')
	followers_num = int(followers_num_element[1].get_attribute('title').replace(',',''))
	print(followers_num)
	scrolls = ceil(followers_num/12)+1 # +1 just to make sure that we are going to scrap all content 
	print('this is the number of scrolls'+str(scrolls))
	for i in range(scrolls):
		print(str(i)+"scroll")
		driver.execute_script("document.querySelector('div[role=dialog] ul').parentNode.scrollTo({}, {})".format(str(x),str(y)))
		time.sleep(1)
		x += 1000
		y+= 1000
	print('We get :')
	print (len(driver.find_elements_by_xpath("//a[@style='width: 30px; height: 30px;']/following-sibling::div/div[1]/a")))

	return driver,driver.find_elements_by_xpath("//a[@style='width: 30px; height: 30px;']/following-sibling::div/div[1]/a")

def get_likers(driver,post_url):
	driver.get(post_url)
	time.sleep(2)
	driver.find_element_by_partial_link_text(' likes').click()
	time.sleep(2)
	element = driver.find_element_by_xpath('//a[@class = "zV_Nj"]/span')
	xpath = ("//a[@style='width: 30px; height: 30px;']")
	likes_num = int((element.text).replace(',',''))
	print("likers number {}".format(likes_num))
	scrolls = ceil(likes_num/12)+1 # +1 just to make sure that we are going to scrap all content 
	print('this is the number of scrolls'+str(scrolls))
	x,y = 0 , 500
	for i in range(scrolls):
		print(str(i)+"scroll")
		driver.execute_script("document.querySelector('div[role=dialog] ul').parentNode.scrollTo({}, {})".format(str(x),str(y)))
		time.sleep(1)
		x += 1000
		y+= 1000
	print('We get :')
	print (len(driver.find_elements_by_xpath("//a[@style='width: 30px; height: 30px;']/following-sibling::div/div[1]/a")))


	return driver,driver.find_elements_by_xpath("//a[@style='width: 30px; height: 30px;']/following-sibling::div/div[1]/a")


def select_winner(driver,post_url,followers):
	driver.get(post_url)
	time.sleep(5)
	driver.find_element_by_partial_link_text(' likes').click()
	time.sleep(5)
	element = driver.find_element_by_xpath('//a[@class = "zV_Nj"]/span')
	xpath = ("//a[@style='width: 30px; height: 30px;']")
	cmp  = len(driver.find_elements_by_xpath(xpath))
	likes_num = int((element.text).replace(',',''))
	x,y = 0 , 500
	winner = randint(0,likes_num-1)
	print('this is the winner '+str(winner))
	scrolls = ceil(winner/12)+1
	for i in range(scrolls):
		print(str(i)+"scroll")
		driver.execute_script("document.querySelector('div[role=dialog] ul').parentNode.scrollTo({}, {})".format(str(x),str(y)))
		time.sleep(1)
		x += 1000
		y+= 1000
	while True : 
		people=driver.find_elements_by_xpath("//a[@style='width: 30px; height: 30px;']/following-sibling::div/div[1]/a")		
		winner_id = people[winner-1]
		winner_username = str(winner_id.text)
		if winner_username in followers : 
			break
		else : 
			winner = randint(0,winner)
	driver.get('https://www.instagram.com/'+str(winner_username))
	return driver
def get_items(driver):

	people=driver.find_elements_by_xpath("//a[@style='width: 30px; height: 30px;']/following-sibling::div/div[1]/a")		
	return driver, people
