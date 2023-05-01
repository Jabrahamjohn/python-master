# modifiers  are essential for use when data is certain to change at times or when its user input
# modifiers simply makes sure you don't haveto change the whole code when new input is enter but the definations only
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s.\n"%(my_name)) # "%s" is a string modifier
print("He's %d inches tall\n"%(my_height)) # "%d" is an integer modifier
print("He's %d pounds heavy.\n"%(my_weight),"Actually that's not too heavy.\n")
print("He's got %s eyes and %s hair.\n"%(my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee.\n"%(my_teeth))
# this line is tricky, try to get it exactly right
print("collectively %s is:\n %d years\n %d tall\n %d heavy %")
