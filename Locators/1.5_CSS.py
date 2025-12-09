#CSS SELECTOR:
# What is Css?
#     --> Css stands for Cascading style Sheet
#     --> It is used to decorate a webpage like color,font size,Background etc.....

# What is css selector?
#     It is used to find the location of a web element by using css expression

# css expression:
"""
    syntax:
        tagname[attribute name='attribute value']
        Any attribute including id,name,class etcc....
"""

# Where we have to write css expression?
"""
Step 1 : Inspect the element
Step 2 : Press ctrl+f in your keyboard "find my string" search will get appear
Step 3 : type the css expression
"""

# Verify the css expression to check if the expression is valid or not:
"""
1.Element should get highlight
2.code should get highlight in yellow color
3.(1 of 1) Matching you have to get
"""

# Sample code:
import time

""" syntax:
         tagname[attribute name='attribute value']
Any attribute including id,name,class etc can be used
"""
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/l")
time.sleep(2)
driver.find_element("link text","Log in").click()
time.sleep(2)
driver.find_element("css selector","input[id='Email']").send_keys("hastafsfr@gmail.com")
time.sleep(2)

driver = http: // webdriver.Chrome(opts)
driver.get("https://www.selenium.dev/downloads/")
time.sleep(3)
driver.find_element("partial link text", "languages").click()
"""

# CSS SELECTOR:
# What is Css?
#     --> Css stands for Cascading style Sheet
#     --> It is used to decorate a webpage like color,font size,Background etc.....

# What is css selector?
#     It is used to find the location of a web element by using css expression

# css expression:
"""
syntax:
tagname[attribute
name = 'attribute value']
Any
attribute
including
id, name,


class etcc....


"""

# Where we have to write css expression?
"""
Step
1: Inspect
the
element
Step
2: Press
ctrl + f in your
keyboard
"find my string"
search
will
get
appear
Step
3: type
the
css
expression
"""

# Verify the css expression to check if the expression is valid or not:
"""
1.
Element
should
get
highlight
2.
code
should
get
highlight in yellow
color
3.(1
of
1) Matching
you
have
to
get
"""

# Sample code:
"""
driver = http: // webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/login")
time.sleep(3)
driver.find_element("css selector", "input[class='email']").send_keys("Amitabh mailto:bachhan@gmail.com")
"""


Oct 30 - 11:01 am
# xpath :
#     xpath is used to find the location of a webelement in a html tree structure or in DOM(Document object Model)

# xpath classified into two types:
# 1.Absolute xpath
# 2.Relative xpath

# 1.Absolute xpath
#     -->It will traverse from parent to its own child
#     -->It is Denoted as (/)
# Drawbacks of Absolute xpath
#     -->Absolute xpath is very lengthy comparing to relative xpath
#     --> Always it will traverse from parent to its own child
# 2.Relative xpath
#     -->It will traverse from parent to any of the child
#     -->It is Denoted as (//)

# Sample for Absolute xpath
"""
driver = http: // webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/A2_Selenium/xpath.html")
time.sleep(3)
driver.find_element("xpath", "html/body/div[1]/input[1]").send_keys("Username1")

"""
"""
driver = http: // webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/A2_Selenium/xpath.html")
time.sleep(3)
driver.find_element("xpath", "html/body/div[2]/input[2]").send_keys("Username4")
"""
"""
driver = http: // webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/")
time.sleep(3)
driver.find_element("xpath", "html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a").click()
"""
