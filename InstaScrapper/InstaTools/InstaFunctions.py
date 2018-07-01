import time
from selenium import webdriver

def login(driver,username,password):
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(5)
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    elements = driver.find_elements_by_xpath("//*[contains(text(), 'Log in')]")
    element  = elements[0]
    element.click()
    time.sleep(10)
    return driver

def get_profile(driver):
	driver.find_element_by_link_text('Profile').click()
	return driver

def get_followers(driver):
	time.sleep(5)
	driver.find_element_by_partial_link_text(" followers").click()
	time.sleep(5)
	xpath = ("//a[@style='width: 30px; height: 30px;']")
	x = 0
	y = 500
	followers_num_element  = driver.find_elements_by_xpath('//span[@class ="g47SY "]')
	followers_num = int(followers_num_element[1].get_attribute('title'))
	while True :
		driver.execute_script("document.querySelector('div[role=dialog] ul').parentNode.scrollTo({}, {})".format(str(x),str(y)))
		count = len(driver.find_elements_by_xpath(xpath))
		x += 500
		y+= 500
		if followers_num == count:
			break

	return driver.find_elements_by_xpath("//a[@style='width: 30px; height: 30px;']/following-sibling::div/div[1]/a")

def get_likers(driver,post_url):
	driver.get(post_url)
	time.sleep(5)
	driver.find_element_by_partial_link_text(' likes').click()
	time.sleep(5)
	element = driver.find_element_by_xpath('//a[@class = "zV_Nj"]/span')
	xpath = ("//a[@style='width: 30px; height: 30px;']")
	likes_num = int((element.text).replace(',',''))
	print("likers number {}".format(likes_num))
	x = 0
	y = 500
	while True :
		driver.execute_script("document.querySelector('div[role=dialog] ul').parentNode.scrollTo({}, {})".format(str(x),str(y)))
		count = len(driver.find_elements_by_xpath(xpath))
		x += 500
		y+= 500
		if likes_num == count:
			break

	return driver.find_elements_by_xpath("//a[@style='width: 30px; height: 30px;']/following-sibling::div/div[1]/a")
