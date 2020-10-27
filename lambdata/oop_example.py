"""OOP examples for module 2"""

import pandas as pd
import numpy as np


class BareMinimumClass:
    pass

class Complex:
    def __init__(self, realpart, imagpart):
        """
        Constructor for complex numbers.
        Complex numbers have a real part and imaginary part. 
        """
        self.r = realpart
        self.i = imagpart

    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i
    
    def __repr__(self):
        return '({}, {})'.format(self.r, self.i)

class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def recieve_upvotes(self, num_upvotes=1):
        self.upvotes += num_upvotes

    def  is_popular(self):
        return self.upvotes > 100

class Animal:
    """General Rep"""
    def _init_(self, name, weight, diet_type):
        self.name = name
        self.weight = weight
        self.diet_type = diet_type

    def run(self):
        return "Vroom"

    def eat(self, food):
        return 'i love' + str(food)

class Sloth(Animal):
    pass        



if __name__ == '__main__':
    num1 = Complex(3, 5)
    num2 = Complex(4, 2)
    num1.add(num2)
    print(num1.r, num1.i)

    user1 = SocialMediaUser('Justin', 'Provo')
    user2 = SocialMediaUser('Nick', 'Logan', 200)
    user3 = SocialMediaUser('Carl', 'Costa', 750000)
    user4 = SocialMediaUser('Rick', 'Majuro', 75)

    print('is popular: {}, num upvotes: {}'.format(user4.is_popular(), user4.recieve_upvotes()))
    print('is popular: {}, num upvotes: {}'.format(user3.is_popular(), user3.recieve_upvotes()))