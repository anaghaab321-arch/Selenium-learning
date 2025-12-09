#alerts

#simple alert
'''
import time
from _pyrepl.commands import accept

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
'''
'''
driver.find_element('xpath','//button[text()="Simple Alert"]').click()
alert_obj= driver.switch_to.alert
alert_obj.accept()

'''
#####################################################
#confirmation alert
'''
driver.find_element('xpath','//button[text()="Confirmation Alert "]').click()
alert_obj= driver.switch_to.alert
alert_obj.accept()
#alert_obj.dismiss()
'''
######################################################################
#prompt alert
'''
driver.find_element('xpath','//button[text()="Prompt Alert"]').click()

time.sleep(2)

alert_obj= driver.switch_to.alert
alert_obj.send_keys('leoooo')

time.sleep(2)
alert_obj.accept()


'''
#################################################################
#authetication pop up
'''
import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')


'''
#################################################################
#push notifications
'''
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
opts.add_argument('--disable-notifications')
driver = webdriver.Chrome(opts)


driver.get('https://www.irctc.co.in/nget/train-search')

'''

Disable push notifications in Firefox       '''
# from selenium import webdriver
#
# opts = webdriver.FirefoxOptions()
#
# opts.set_preference("dom.webnotifications.enabled", False)
# opts.set_preference("dom.push.enabled", False)
#
# driver = webdriver.Firefox(opts)
#
# driver.get('https://www.irctc.co.in/nget/train-search')
#
# ##-----------------------------------------------------------------------
#
'''     Disable push notifications in Edge       '''
# from selenium import webdriver
#
# opts = webdriver.EdgeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument("--disable-notifications")
#
# driver = webdriver.Edge(opts)
#
# driver.get('https://www.irctc.co.in/nget/train-search')

##-----------------------------------------------------------------------

'''     Allow push notifications in Chrome       '''
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

prefs = {
    "profile.default_content_setting_values.notifications":2            ## 2 --> disable, 1--> allow notifications , 0--> will give the pop-up
}

opts.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(opts)

driver.get('https://www.irctc.co.in/nget/train-search')

##-----------------------------------------------------------------------

'''     Allow push notifications in Firefox       '''

from selenium import webdriver

opts = webdriver.FirefoxOptions()

opts.set_preference("permissions.default.desktop-notification", 1)      ## 2 --> disable, 1--> allow notifications , 0--> will give the pop-up

driver = webdriver.Firefox(opts)
driver.get('https://www.irctc.co.in/nget/train-search')


































