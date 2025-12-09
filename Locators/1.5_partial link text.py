#partial link text
from selenium import webdriver
# from time import sleep (1)
import time #(2)
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver=webdriver.Chrome(opts)
'''
driver.get("file:///C:/Users/anagh/OneDrive/Desktop/partial%20link%20text.html")
time.sleep(2)
driver.find_element("partial link text","python").click()
'''
driver.get("https://www.selenium.dev/")
time.sleep(3)
driver.find_element("link text","Downloads").click()
time.sleep(2)
driver.find_element("partial link text","languages ").click()
time.sleep(2)