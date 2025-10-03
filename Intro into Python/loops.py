#usr/bin/python
import random
import sys
import os

for x in range(0,10):
    print x

print "\n"

grocery_list = ['juice','tomatoes', 'potatoes',
               'bananas']
for y in grocery_list:
    print y

for x in [2,3,4,5,6,7,8]:
    print x

num_list = [[1,2,3],[10,20,30],[100,200,300]]

for  x in range(0,3):
    for y in range(0,3):
        print num_list[x][y]

#while loops
random_num = random.randrange(0,100)
while random_num != 15:
    print random_num
    random_num = random.randrange(0,100)

#other method for while loop
i = 0;
while 1<=20:
    if i%2 == 0:
        print i
    elif i == 9:
        break
    else:
        i +=1
        continue
    i += 1
