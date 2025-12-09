#oops
# class cars:
#     name
#     price
#     colour
#
#     start()
# car1="maruthi","300000","red"
# car2="toyota","257184","orange"
'''
class Cars:
    def __init__(self,name,price,color):
        self.name = name
        self.price = price
        self.color = color
    def start(self):
        print(self.name,"engine started")
car1 = Cars("maruthi","300000","red")
car2= Cars("toyota","257184","orange")
print(car1.name,car1.price,car1.color)
car1.start()
'''
####################################################################
# inheritance
'''class Person:                             #parent class
    def __init__(self,name,contact):
        self.name= name
        self.contact= contact
    def address(self):
        print(self.name, self.contact)
#child class
class Doctor(Person):
    pass                #if no proprties is typed use pass
class Patient(Person):
    pass
doc1=Doctor("john","26354871254")
pat1=Patient("leii",62354827)

doc1.address()
pat1.address()'''
###################################################################
#math functions
#min - functn used to get the min value
'''a= min(19.6,77,4,6)
print(a)'''
#max
'''a= max(19.6,77,4,6)
print(a)
'''
#exponential
'''a= pow(2,3)
print(a)#   2*2*2
'''
#math module functions
'''import math
a= math.pi
print(a)
#pi,sqrt,gcd'''


####################################################################

#pyhon module
def man(name):
    print("hello",name)
###########################################################




































































