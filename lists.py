#usr/bin/python
import random
import sys
import os

grocery_list = ['juice','tomatoes', 'potatoes',
               'bananas']
print 'first item', grocery_list[0] #prints item at index 0 in list

grocery_list[0] = 'green juice' #changes the value of index 0
print 'first item', grocery_list[0]

print grocery_list[1:3] #prints items at index 1 and 2

#lists within a list
other_events = ['wash car', 'pick up kids', 'cash check']

to_do_list = [other_events, grocery_list] #lists within a list

print to_do_list
print to_do_list[1][2]

grocery_list.append('onions')
grocery_list.reverse()
grocery_list.sort()
del grocery_list[4]
print to_do_list

to_do_list2 = other_events + grocery_list
print to_do_list2
print len(to_do_list)
print len(to_do_list2)


