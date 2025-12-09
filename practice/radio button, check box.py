import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True) #prevent the browser from automatically closing
driver = webdriver.Chrome(opts)
driver.get('https://demo.automationtesting.in/Register.html')
time.sleep(2)
#radio button
driver.find_element('xpath','//input[@value="Male"]').click()
time.sleep(2)

#check box

#find elements will give multiple web elements
#find element will give single web element
#here we have 3 check box and when we give //input[@type="checkbox"] it give 3 outputs
#so we are  creating a list of elements here
li = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for s in li:
    val = s.get_attribute('value')
    print(val)

