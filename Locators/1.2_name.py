import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True) #prevent the browser from automatically closing
driver = webdriver.Chrome(opts)
driver.get('https://www.instagram.com/accounts/login/?hl=en')
time.sleep(2)

'''
if we dont have id attribute we can use other attributes like name
 value name - if we have space then they are seperate attributes
value- default value of value is '' if we give value then it will be updated

 name - it will have a 'name'
 '''
driver.find_element('name','username').send_keys('anaghaab')
time.sleep(2)
driver.find_element('name','password').send_keys('anagh@321')
time.sleep(2)

# driver = webdriver.Chrome(opts)
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
'''here we have both id and name so we wil get the 
most appropriate one that suits
'''
# driver.find_element('name','firstname').send_keys('anaghaab')
# time.sleep(2)
# driver.find_element('name','reg_email__').send_keys('anagh32@gmail.com')
# time.sleep(2)
# driver.find_element('name','reg_passwd__').send_keys('anaghaa@3b')
# time.sleep(2)