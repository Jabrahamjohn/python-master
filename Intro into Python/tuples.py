#usr/bin/python
import random
import sys
import os

#tuples are used for data that cannot be changed
pi_tuple = (3,1,4,5,9)

#converts tuple to list
new_tuple = list(pi_tuple)
#converts list to tuple
pi_tuple = tuple(new_tuple)


print pi_tuple
print new_tuple
print len(pi_tuple)
print min(pi_tuple)
print max(pi_tuple)
