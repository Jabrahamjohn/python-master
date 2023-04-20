#imports the feature argument
from sys import argv
#the variables are packed in the argv module
script, filename = argv
#opens the file
txt = open(filename)
#print out the file named in the argument
print "here's your file %r:" % filename
print txt.read()
#prints it out again
print "type of filename again"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()

