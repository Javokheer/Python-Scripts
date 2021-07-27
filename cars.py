# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 15:16:58 2021

@author: acer
"""

class Car:
    """Create a new Car object from the given object. It takes follows arguments and holds setter and getter methods
        Parameters:
            make - Manufacturer of the car class
            model - model of the specific car class
            color - color of the class
            price - price of the car class
            km - km car driven so far. This is optional, by default it's zero km and it cannot be changed without using add_km method
    """
    def __init__(self, model, make, year, km=0, price=None):
        self.model = model
        self.make = make
        self.year = year
        self.price = price
        self.__km = km 
        
    def set_km(self, km):
        """ sets km to Car object
            Input:  km parameter takes integer """
        if km >= 0:
            self.__km += km
        else:
          raise ValueError('You cannot dicrease km !')
            
    def get_km(self):
        """returns all km passed by specific car object"""
        return self.__km
        
    def set_price(self, price):
        """ sets price to Car object
            Input:  km parameter takes integer """
        self.price = price
            
        
    def get_info(self):
        """returns string of  full information about a specific car object with its parameters including:
        model, make, price, year, km, price if present
        """
        info = f"Car's model {self.model}, it's make {self.make} "
        info += f' Year is {self.year} and km is {self.__km} and it is price is {self.price} '
        if self.price:
            info += f' Price: {self.price}'
        return info
