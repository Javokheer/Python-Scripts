# -*- coding: utf-8 -*-
"""
Created on Wed May  5 08:03:37 2021

@author: acer
"""

#Inheritance
class Parent:
    def __init__(self, a):
        self.a = a
    def method1(self):
        return self.a * 2
    def method2(self):
        return self.a + '!!!'

class Child(Parent):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def method1(self):
        return self.a * 7
    def method3(self):
        return self.a + self.b
    
p = Parent('hi')
c = Child('hi', 'bye')

print('Parent method 1: ', p.method1())
print('Parent method 2: ', p.method2())
print()
print('Child method 1: ', c.method1())
print('Child method 2: ', c.method2())
print('Child method 3: ', c.method3())


#Multiple Inheritance
class Shape:
    def __init__(self):
        self.color = (0, 0, 0)
        
    def __str__(self):
        return('RGB colors set to ()'.format(self.color))

class Rectangle(Shape):
    def __init__(self, w, h):
        Shape.__init__(self)
        self.width = w
        self.height = h
    
    def area(self):
        self.area = self.width * self.height
        return self.area
    
    def __str__(self):
        return('Height and Width of rectangle are {} and {} and colors are {}'
               .format(self.height, self.width, self.color))
    
class Square(Rectangle):
    def __init__(self, s):
        Rectangle.__init__(self, s, s)
        self.side = s
    
    def area(self):
        self.area = self.side ** 2
        return self.area
    
    def __str__(self):
        return('Side of Square is {} and colors are {}'
               .format(self.side, self.color))
    
r1 = Rectangle(10, 5)
print("Area of Rectangle: ", r1.area())
print(r1)

s1 = Square(10)
print("Area of Square: ", s1.area())

print("Square data members: ", s1.width, s1.height, s1.side, s1.color)

print(s1)



#Special Functions
from copy import *

class Student:
    def __init__(self, name, telephone, age):
        self.name = name
        self.telephone = telephone
        self.age = age
    
    def __len__(self):
        return(len(self.name))
    
    def __str__(self):
        return ("Name of student: {} Telephone of student: {} Age of student: {}".format(self.name, self.telephone, self.age))

s1 = Student('Tom', '999-999-999', 25)

print(s1)
print()

l_name = len(s1)

print("Length of name is: ", l_name)
print()

s2 = s1

s3 = copy(s1)

print(s2)
print()

s1.name = 'Harry'

print(s1)
print('------------------')
print(s2)
print('------------------')
print(s3)
