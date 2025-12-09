
#upload a file
'''
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)
file_path = r"C:\Users\anagh\PycharmProjects\selenium_project"
driver.find_element('xpath','//input[@id="singleFileInput"]').send_keys(file_path)

#######'''###########################################################

# upload multiple files
'''
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)
file1 ="C:\\Users\\anagh\OneDrive\\Desktop\\seleniuym practice"
file2 ="C:\\Users\\anagh\\OneDrive\\Desktop\\RESUME"
file3 ="C:\\Users\\anagh\\OneDrive\\Desktop\\python qstns 1.txt"
driver.find_element('xpath','//input[@id="multipleFilesInput"]').send_keys(f'{file1}\n{file2}\n{file3}')

'''

###################################################
#download a file
'''

import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)'''
'''
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)
file_path = "C:\Users\anagh\PycharmProjects\selenium_project"
driver.find_element('xpath','//input[@id="singleFileInput"]').send_keys(file_path)
'''