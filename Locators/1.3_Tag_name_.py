from selenium import webdriver
# from time import sleep (1)
import time #(2)
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)


'''
# Tag name:
"""
driver = webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element("tag name","a").click()
"""
"""
driver = webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/register")
time.sleep(3)
driver.find_element("tag name","input").send_keys("Selenium")
"""
# find_elements():

driver = webdriver.Chrome(opts)
driver.get()
time.sleep(3)
driver.find_element("id","First")


