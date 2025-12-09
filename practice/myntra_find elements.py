#go to myntra and fetch the popular search elements
'''
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://www.myntra.com/')
time.sleep(2)
driver.maximize_window()
popular_search = driver.find_elements('xpath','//div[@class="desktop-pSearchlinks"]//a')
for ele in popular_search:
    print(ele.text)
'''
############################################################################
'''
'''
#assignmnt 2 :_go to myntra and serch addidas  and list the colors
'''
2.  wap to print all the colors available for adidas original shoes in https://www.myntra.com/
3.  Go to https://www.zomato.com/Bengaluru/, search for pizza, select pizza-delivery, select any cafe/restraunt which serves pizza,
    wap to print the name and price of each food item in available
4.  Go to https://in.bookmyshow.com/, select the location. Print all the movie names available.
'''
#######################################2222222222222222222########################################
'''
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://www.myntra.com/')
time.sleep(2)
driver.maximize_window()
driver.find_element('xpath','//input[@class="desktop-searchBar"]').send_keys('adidas')
time.sleep(2)
driver.find_element('xpath','//li[text()="Adidas Shoes"]').click()
time.sleep(2)
driver.find_element('xpath','//span[text()=" more"]').click()
time.sleep(2)
color = driver.find_elements('xpath','//div[@class="vertical-filters-filters"]//li[@class="colour-listItem"]')
for colours in color:
    print(colours.text)

'''

####################################################################################
#3.  Go to https://www.zomato.com/Bengaluru/, search for pizza, select pizza-delivery, select any cafe/restraunt which serves pizza,
   # wap to print the name and price of each food item in available
'''
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://www.zomato.com/bangalore/restaurants')
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.find_element('xpath','//div[@class="sc-18n4g8v-0 gAhmYY sc-kMBllD LqMHQ"]//input').click()
time.sleep(2)
driver.find_element('xpath','//input[@placeholder="Search for restaurant, cuisine or a dish"]').send_keys('pizza')
time.sleep(2)
driver.find_element('xpath','//div[@class="sc-glUWqk GrjUP"]//p[text()="Pizza - Delivery"]').click()
time.sleep(2)
driver.find_element('xpath',"//div[@class='sc-evWYkj cRThYq']//h4[text()=\"Domino's Pizza\"]").click()
time.sleep(2)
foods = driver.find_elements('xpath','//div[@class="sc-dgEPJF nioNy"]//h4')
prices = driver.find_elements('xpath','//div[@class="sc-dgEPJF nioNy"]//span[@class="sc-17hyc2s-1 cCiQWA"]')
for f, p in zip(foods, prices):
    print(f.text, "-", p.text)

'''
####################################################################################################

# go to book my show .select location. click on see all. print all the movies names available
'''
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://in.bookmyshow.com/')
driver.maximize_window()
time.sleep(2)
driver.find_element('xpath','//p[text()="Kochi"]').click()
time.sleep(2)
driver.find_element('xpath','//div[text()="See All ›"]').click()
time.sleep(2)
movies = driver.find_elements('xpath','//div[@role="main"]//h3[contains(@class,"sc-133848s-16")]')
time.sleep(2)
for movie in movies:
    print(movie.text)
'''
#//div[@role="main"]//div[@class="sc-1ljcxl3-0 ldQqlW"]//div[@class="sc-7o7nez-0 elfplV"]

############################################################################
#go to the website and write the data
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
data = driver.get('file:///C:/Users/anagh/OneDrive/Desktop/seleniuym%20practice/demo.html')
driver.maximize_window()
time.sleep(2)
s=driver.find_elements('xpath','//input[@name="fname"]')
data_list=["u","are","strong","baby","i","love","you","so","much"]
time.sleep(2)
for text,data in zip(s,data_list):
    s.send_keys(data_list)

###############################'''#################################
# go to python.org and fetch all the link in it
'''
import time
from selenium.webdriver.edge.options import Options
from selenium import webdriver

opts = Options()
opts.add_argument("--start-maximized")
opts.add_experimental_option("detach", True)

driver = webdriver.Edge(options=opts)
driver.get('https://www.python.org/')
driver.maximize_window()
time.sleep(2)
all_links = driver.find_elements('tag name','a')
for link in all_links:
    print(link.get_attribute('href'))



'''


























