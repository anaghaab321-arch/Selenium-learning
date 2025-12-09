import time

#from selenium import webdriver

#opts = webdriver.ChromeOptions()
#opts.add_experimental_option("detach", True) #prevent the browser from automatically closing

#driver = webdriver.Chrome(opts)

## launch the application
'''
driver.get('https://www.saucedemo.com/v1/')
time.sleep(2)
driver.find_element('id','user-name').send_keys('standard_user')
time.sleep(1)
driver.find_element('id','password').send_keys('secret_sauce')
time.sleep(2)
driver.find_element('id','login-button').click()
time.sleep(5)
driver.find_element('id','burger-menu-btn').click()
time.sleep(1)
driver.find_element('id','logout_sidebar_link').click()
time.sleep(1)
'''
'''
driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)
driver.find_element('id','name').send_keys('Anagha')
time.sleep(1)
driver.find_element('id','email').send_keys('anaghaab36@gmail.com')
time.sleep(2)
driver.find_element('id','phone').send_keys('8357986434')
time.sleep(1)
driver.find_element('id','textarea').send_keys('Hazel villa sellom')
time.sleep(1)
driver.find_element('id','female').click()
time.sleep(1)
driver.find_element('id','country').click()
time.sleep(1)
driver.find_element('id','country').click()
time.sleep(1)
driver.find_element('id','country').click()
time.sleep(1)

'''
'''
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True) #prevent the browser from automatically closing

driver = webdriver.Chrome(opts)

## launch the application
driver.get('file:///C:/Users/anagh/OneDrive/Desktop/Practice%20sign%20up.html')
time.sleep(2)
driver.find_element("id","f1").send_keys("lolapp")
time.sleep(1)
## 1.if we have the value matches wwith multile elements then the firstone will
## have the value. for eg: if username and password have id="a1" then a1 is for username
## 2.if we put an id which is not present it will give
## no such elment exemption
## 3.eg: driver.find_element("if","f1").send_keys("lolapp")
## if we enter if instead of id  it shows : 
## InvalidArgumentException
##. eg:diver.get("www.amazon.com")    -  here link is not clear
## it wil show InvalidArgument
'''
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True) #prevent the browser from automatically closing

driver = webdriver.Chrome(opts)

## launch the application
driver.get('https://www.facebook.com/login/')
time.sleep(2)
driver.find_element("id","email").send_keys("gandhara")
time.sleep(1)
driver.find_element("id","pass").send_keys("lovee")
time.sleep(1)
driver.find_element("id","loginbutton").click()
time.sleep(1)
##there are times the id locators o not work thats when we use name locator