#usr/bin/python
import random
import sys
import os

age = 30

if age > 16 :
    print 'you are old enough to drive'
else:
    print 'you are not old enough to drive'

if age >= 21 :
    print 'you are old enough to drive a tractor'
elif age >=16 :
    print 'you are old enough to drive a car'
else:
    print 'you are not old enough'


    #loops through all statements to get to the last statement
if age >= 1 and age <= 18:
    print 'you get a birthday'
elif age ==21 or age >=65:
    print 'you get a birthday'
elif age !=30:
    print 'you don\'t get a birthday'
else:
    print 'you get a bday yeah!'
