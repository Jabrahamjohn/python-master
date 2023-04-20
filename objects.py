#usr/bin/python
import random
import sys
import os

class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    #constructor
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
#getters and setters
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height

    def set_weight(self, weight):
        self.__weight = weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_height(self, height):
        return str(self.__height)

    def get_weight(self, weight):
       return str(self.__weight)

    def get_sound(self, sound):
        return self.__sound

    def get_type(self):
        print "animal"

    def toString(self):
        return "{} is {} cm tall and {} kgs and say {}".format(self.__name,
                   self.__height,
                   self.__weight,
                   self.__sound)
    cat = animal('whiskers', 33, 10,"meow")
