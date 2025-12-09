import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://www.myntra.com/')
time.sleep(1)
'''
men = driver.find_element('xpath', '//a[@data-group="men"]]')
 print(men.text)
 '''

#text   : it is a property which will give the value of web element

#if we dnt use text here (print(men) only it will give only the address
#where it is stored.
#we use data grp here
##############################################################
# if we want to fetch the attribute value of web element
#eg:- i want to now value of class,href,id, etcc
'''
women = driver.find_element('xpath', '//a[@data-group="women"]][1]')
print(women.get_attribute('href'))
'''
#get dorm attribute

list1=["onion","tomato"]
print(list1)















































