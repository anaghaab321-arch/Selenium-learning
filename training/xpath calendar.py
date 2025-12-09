#sol 1
'''
import time
from sys import maxsize

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://www.makemytrip.com/')
time.sleep(2)
driver.maximize_window()
driver.find_element('xpath','//span[@class="commonModal__close"]').click()
time.sleep(2)
driver.find_element('xpath','//span[text()="Departure"]').click()
time.sleep(2)
def select_date(month,date):
    while True:
        try:
            driver.find_element('xpath', f'//div[text()="{month}"]/../..//p[text()="{date}"]').click()
            break
        except:
            driver.find_element('xpath', '//span[@class="DayPicker-NavButton DayPicker-NavButton--next"]').click()
select_date('May 2026',26)
'''
'''
#sol 2
import time
from sys import maxsize

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://www.makemytrip.com/')
time.sleep(2)
driver.maximize_window()
driver.find_element('xpath','//span[@class="commonModal__close"]').click()
time.sleep(2)
driver.find_element('xpath','//span[text()="Departure"]').click()
time.sleep(2)
while True:
    month = driver.find_element('xpath', '(//div[@class="DayPicker-Caption"])[1]')
    print(month.text)

    if month.text == 'July 2026':
        driver.find_element('xpath', '(//p[text()="20"])[1]').click()
        break
    else:
        driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()
    '''

#go to irctc and select a travel date
'''
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://www.irctc.co.in/nget/train-search')
time.sleep(1)
driver.maximize_window()
driver.find_element('xpath','//button[@class="btn btn-primary"]').click()
time.sleep(2)
driver.find_element('xpath','(//input[@autocomplete="off"])[3]').click()
time.sleep(2)
#if we dont use forward
# driver.find_element('xpath','//div[@class="ui-datepicker-title ng-tns-c69-9"]/../..//a[text()="19"]').click()
# time.sleep(2)
def select_date(month,year,date):
    while True:
        try:
            driver.find_element('xpath', f'//span[text()="{month}"]/..//span[text()="{year}"]/../..//a[text()="{date}"]').click()
            break
        except:
            driver.find_element('xpath','//span[@class="ui-datepicker-next-icon pi pi-chevron-right ng-tns-c69-9"]').click()
select_date('January','2025','2')
#not completed
'''
#go to https://www.redbus.in/, select the date of journey
#Go to https://www.booking.com/, select the check-in date
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://www.redbus.in)
time.sleep(1)
driver.maximize_window()
driver.find_element('xpath','//div[@class="dateInputWrapper___c8345a"]').click()
time.sleep(2)

            driver.find_element('xpath','//p[text()="December"]/..//p[text()="2025"]/../../..//span[text()="19"]').click())







































