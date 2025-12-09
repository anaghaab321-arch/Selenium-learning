# dependent independant xpath . check box
'''
eg : 1
# 1. identify the dependant and independant element
# 2. write xpath of independant element
# eg:- //td[text()='ruby']
#
# 3. traverse back(from the independant element we are going to
#  find the common parent for ind and dep element) until we get the match
#  for that - xpath of ind element/..  check the ind nd dep element is highlited.
#  do/.. until it is highlited.
#  eg:-//td[text()='ruby']/..
#
#  4. continue writing the xpath of dependant elment
#  eg:-//td[text()='ruby']/..//input[@name='download']

'''
import time

'''
if we have both the element as independant 
'''
'''
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://in.tradingview.com/')
time.sleep(2)

driver.find_element('xpath','//span[text()="Search"]').click()
time.sleep(2)
driver.find_element('xpath','//input[@name="query"]').send_keys('Hal')
time.sleep(2)
driver.find_element('xpath','(//button[@aria-label="Search"])[3]').click()
time.sleep(2)
hal_price = driver.find_element('xpath','//span[text()="HAL"]/../../..//span[@class="priceWrapper')
#it is a variable web element
'''

#write the sell price and
#the value of dependant var is dynamically changing so we only considering parenrrt tag


from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://www.iforex.in/')
time.sleep(2)
driver.find_element('xpath','(//div[@id="ai-chat-bubble-close"])[2]').click()
time.sleep(4)
gold_sell_price = driver.find_element('xpath','(//div[text()="Gold"]/../..//span)[2]')
gold_buy_price = driver.find_element('xpath','(//div[text()="Gold"]/../..//span)[3]')
print({gold_sell_price.text})
print({gold_buy_price.text})



























