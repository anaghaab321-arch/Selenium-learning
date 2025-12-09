from selenium import webdriver
import time
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver=webdriver.Chrome(opts)
driver.get("https://www.saucedemo.com/v1/")
time.sleep(2)
driver.find_element("id","user-name").send_keys("problem_user")