
from selenium import webdriver
import time
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver=webdriver.Chrome(opts)
driver.get("https://www.selenium.dev/")
time.sleep(2)

#browser commands
'''
driver.maximize_window()
driver.fullscreen_window()
driver.close()
driver.quit()
'''



