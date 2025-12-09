#5.link text:
#     It is used to find the location of an element by using text.
#     It will work only for anchor Tag [It will work for span tag also but not all the time]
#     The text value is case sensitive

# Sample Html code:
# <a href="https://www.amazon.in">Amazon</a>
# <span>...</span>

# Sample code:
"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/A1_html/sample.html")
time.sleep(3)
driver.find_element("link text","Amazon").click()
"""

# was to click on minutes on flipkart.com
"""
driver = webdriver.Chrome(opts)
driver.get("https://www.flipkart.com/")
time.sleep(3)
driver.find_element("link text","Minutes").click()

"""
"""
driver = webdriver.Chrome(opts)
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.find_element("tag name","input").send_keys("Password")
#ElementNotInteractableException
"""
"""
click on mac in https://www.apple.com/in/
Do signup in udemy
"""
from selenium import webdriver
# from time import sleep (1)
import time #(2)
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
'''
driver=webdriver.Chrome(opts)
driver.get("https://www.apple.com/in/")
driver.find_element("link text","Mac").click()
'''
#udemy
driver = webdriver.Chrome(opts)
driver.get("https://www.udemy.com/?srsltid=AfmBOoo4hmoNb6Wh5YORtxfUokZWS5Ey9-BzMF4T4xB4IKtxnPsFrA_F")
time.sleep(3)
driver.find_element("link text","Sign up").click()
time.sleep(3)
driver.find_element("name","full-name").send_keys("Pookie")
time.sleep(3)
driver.find_element("name","email").send_keys("mailto:Pookie@gmail.com")
time.sleep(3)
driver.find_element("class name","ud-icon.ud-icon-xsmall.ud-fake-toggle-input.ud-fake-toggle-checkbox").click()
time.sleep(3)
driver.find_element("class name","ud-btn.ud-btn-large.ud-btn-brand.ud-btn-text-md.passwordless-auth-mx-code-generation-form--submit-button--2vOvZ").click()
