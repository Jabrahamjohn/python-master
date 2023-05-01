#usr/bin/python
import random
import sys
import os

def addnumber(fnum,lnum):
    sumnum = fnum +lnum
    return sumnum

#calls the function
print addnumber( 3,5)

#interacts with user and saves data in variable
print ('what is your name?')
name = sys.stdin.readline()

print ('hello ' + name)

