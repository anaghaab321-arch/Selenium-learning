'''#print all elements in footer section of demo workshop
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)
driver.maximize_window()

#we cant fetch site link using text because we are printing the text sitelink
#<a href="/sitemap">Sitemap</a>
#we cant locate using text sitemap and also we cant never locate a
#attribute using href
#//div[@class="footer-menu-wrapper"]//a
#div is parent tag and a tag is child. we are first locating the whole footer
#then find elements which is a tag. //a is to find immediate child

# s= driver.find_element('xpath','//a[href="/sitemap"]').click()
# print(s.text)
# time.sleep(2)
# l=driver.find_element('xpath','//a[href="/shipping-returns"]').click()
# print(l.text)
# time.sleep(2)

footer_elements = driver.find_elements('xpath','//div[@class="footer-menu-wrapper"]//a')
print(footer_elements)

#find element will only locate one element. so we use find elments for 22 elements here

#output - [<selenium.webdriver.remote.webelement.WebElement (session="cd00f16327cd484660993105f097f08f",
#we will get elements with address   [webelement1, we2,we3,....]
#we have to extract  the text from this so go for looping

for ele in footer_elements:
    print(ele.text)

#output- Sitemap
# Shipping & Returns
# Privacy Notice
# Conditions of Use
# About us
#.......

'''
#################################################################

#eg 2
#go to myntra and fetch the popular search elements
####################################################################

import time

from selenium import webdriver

'''opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://www.myntra.com/')
time.sleep(2)
driver.maximize_window()
driver
'''
# ass 2 :_go to myntra and serch addidas  and list the colors
# go to zomato bengaluru search for pizza .select 1st option. click on 1st restaurant.
#print name and priceof each and every food item present
# go to book my show .select locatiooon. click on see all. print all the movies names available

###############################################################################
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

categories = driver.find_elements('xpath', '//div[@class="block block-category-navigation"]//a')
print(categories)       ## list of web-elements     ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7]

for ele in categories:
    print(ele.text)

