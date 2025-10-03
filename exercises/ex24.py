#prints out the strings with use of the escapes
print "Let's practise everything"
print 'you\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs'

#printing out a large stringof text
poem = """
\t the lovely world with logic so firmly planted cannot discern \n the needs of love"""

print "---------------"
print poem
print "---------------"

#declaring the variable five with the values inside it
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

#function to multiply and divide so as to get the total number
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
#declares the argument to be used will be 10000
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "with a starting point of: %d" % start_point
print "we'd like %d beans, %d jars and %d crates." % (beans,jars,crates)


