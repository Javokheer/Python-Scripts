# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 16:11:39 2021

@author: acer
"""

from uuid import uuid4


class Car:
    """
    Create a new Car object from the given object and has following parameters as well as methods:
    Parameters:
        make - Manufacturer of the car class
        model - model of the specific car class
        color - color of the class
        price - price of the car class
        km - km car driven so far. This is optional, by default it's zero km and it cannot be changed without using add_km method

    Methods:
        get_km
        get_id
        add_km
    """
    __car_num = 0 
    
    def __init__(self, make, model, color, year, price, km=0):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.__km = km
        self.__id = uuid4()
        Car.__car_num += 1
        
    @classmethod
    def get_car_num(cls):
        """ returns number of car objects in the Car class"""
        return cls.__car_num
    
    def __repr__(self):
        return f'Car: {self.make} {self.model}'
    
    def __eq__(self, y):
        return self.price == y.price
    
    def __lt__(self,y):
        return self.price < y.price
    
    def __le__(self, y):
        return self.price <= y.price
    
    def get_km(self):
        """ returns km of passed by car"""
        return self.__km
    
    def get_id(self):
        """ returns id of 16 characters alphanumeric values   """
        return self.__id
    
    def add_km(self, km):
        """ adds kms to original"""
        if km >= 0:
            self.__km += km
        else:
            raise ValueError('Km cannot be decrased')
