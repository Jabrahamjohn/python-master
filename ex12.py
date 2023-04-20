#imports the argument variable
#it holds the arguments passed in the script
from sys import argv
#unpacks argv and assigns variables to it
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#run $python script.py 1st_argument 2nd_argument ...
