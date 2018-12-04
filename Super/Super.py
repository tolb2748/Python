'''
Created on Dec 3, 2018

@author: Brandon
'''
#This demonstrates how to use super in python. In order to perform inheritance
#in python, you have to extend/inherit the superclass using Dog(Mammal) and then
#you have to use the super method to call the constructer in the superclass

#By defualt, java substitues super for you

class Mammal():
    def __init__(self, name):
        print(name + ' is a warm-blooded animal');
    
    def sayHi(self):
        print('Hi');
        

class Dog(Mammal):
    def __init__(self, x):
        super().__init__(x)
        self.x = x;
        print('Dog Class Executed');
        

dog = Dog('holdout');
