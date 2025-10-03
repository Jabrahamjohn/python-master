#usr/bin/python
import random
import sys
import os

grocery_list = ['juice','tomatoes', 'potatoes',
               'bananas']
print (grocery_list[0]) #prints item at index 0 in list

grocery_list[0] = 'green juice' #changes the value of index 0
print (grocery_list[0])

print (grocery_list[1:3]) #prints items at index 1 and 2

#lists within a list
other_events = ['wash car', 'pick up kids', 'cash check']

to_do_list = [other_events, grocery_list] #lists within a list

print (to_do_list)
print (to_do_list[1][2])
grocery_list.append('onions') #adds item to end of list
grocery_list.insert(1, 'pickles') #adds item at index 1
grocery_list.append('onions')
grocery_list.reverse()
grocery_list.sort()
del grocery_list[4]
print (to_do_list)


to_do_list2 = other_events.extend(grocery_list) #adds grocery_list to end of other_events and assigns to to_do_list2
print (to_do_list2)
print (len(to_do_list))
print (to_do_list2)

grocery_list.extend(to_do_list2) #adds to_do_list2 to end of grocery_list
print (grocery_list)
