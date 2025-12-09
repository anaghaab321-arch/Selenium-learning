#action chains

import time

from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
#to know elements in class click on ctrl nd click on class

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

ac_obj = ActionChains(driver)

'''
driver.get('https://www.kushals.com/')
driver.maximize_window()
time.sleep(2)

earring = driver.find_element('xpath','(//a[contains(text(), "Earrings")])[2])')
ac_obj.move_to_element(earring).perform()
time.sleep(2)

accessories = driver.find_element('xpath', '(//a[contains(text(), "Accessories")])[2]')
ac_obj.move_to_element(accessories).perform()
time.sleep(2)

-----------------------------------------------------------------------------------'''

'''
hover to all the elments present  in the navigation bar
'''

## Solution1
'''
driver.get('https://www.myntra.com/')
time.sleep(2)

navigation_elements = driver.find_elements('xpath', '//a[@class="desktop-main"]')    ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7]
for ele in navigation_elements[:-1]:
    ac_obj.move_to_element(ele).perform()
    time.sleep(2)
'''
##-------------------------------------------------------------------------------
## Solution2
'''
driver.get('https://www.myntra.com/')
time.sleep(2)

navigation_elements = driver.find_elements('xpath', '//a[@class="desktop-main"]')    ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7]
for ele in range(0, len(navigation_elements)-1):
    ac_obj.move_to_element(navigation_elements[ele]).perform()
    time.sleep(2)

################################################################'''

###########  double click  ####################
'''
driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)


copy_name= driver.find_element('xpath','//label[text()="Name:"]')
ac_obj.double_click(copy_name).perform()
'''

################### RIGHT CLICK ####################
'''
right_click_ele= driver.find_element('xpath', '//h2[text()="Dynamic Button"]')
ac_obj.context_click(right_click_ele).perform()

'''
# OR BY DEFAULT IT WILL RM RIGHT CLICK ON START OF APPLICATION
'''
ac_obj.context_click().perform()

'''

################## SCROLLING ####################
#scrolling to a specific spefic element

driver.get('https://www.myntra.com/')
time.sleep(2)
'''
elite_ele = driver.find_element('xpath','//strong[text()="Elite"]')
ac_obj.scroll_to_element(elite_ele).perform()
''' #or

elite_ele = driver.find_element('xpath','//strong[text()="Elite"]')
driver.execute_script("window.scrollInto(0,document.body.ScrollHeight);"







##########################################################

#scroll down till the end of application
#when we click on end button keyword manually the app will scroll to buttom.

#end
#home
#pgUp
#PgDn
#first import keybo
'''
#go to end of applctn
ac_obj.send_keys(Keys.END).perform()

#strt
ac_obj.send_keys(Keys.HOME).perform()

'''
#page up nd page down

'''
ac_obj.send_keys(Keys.PAGE_DOWN).perform()
ac_obj.send_keys(Keys.PAGE_DOWN).perform()
ac_obj.send_keys(Keys.PAGE_UP).perform()
ac_obj.send_keys(Keys.PAGE_UP).perform()

'''














































