from re import T
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep



driver = webdriver.Chrome('/home/silent/Downloads/chromedriver')
driver.get('https://instagram.com')



#username
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(input('username:'))
sleep(10)


#password
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('W13722012h')
sleep(10)
#login btn
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
sleep(10)


# save info
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
sleep(10)


#searche user and enter keys
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(input('target_name: '))
sleep(10)


driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/a/div').click()
sleep(10)


# click options btn
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/button').click()
sleep(10)


# click to report option
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/button[3]').click()
sleep(10)


#click to 'report account'
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div/div[1]').click()
sleep(10)


# click its content that ......
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div/div[1]').click()
sleep(10)


# its spam
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div/div[1]').click()
sleep(10)


#close btn
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div/div/div[4]/button').click()
sleep(10)
