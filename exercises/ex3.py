# variable should always be defined first otherwise it outputs na error
nissans = 20
cabs = 100
space_in_a_cab = 4.0
drivers = 30
passengers = 90
cars_not_driven = cabs - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_cab
average_passengers_per_car = passengers / cars_driven
vehicles = nissans + cabs #+buses

print ("There are", cabs, "cabs available.\n")

print ("There are only", drivers, "drivers available.\n")

print ("There will be", cars_not_driven, "empty cabs today.\n")

print ("We can transport", carpool_capacity, "people today.\n")

print ("We have", passengers, "to carpool today.\n")

print ("We need to put about", average_passengers_per_car, "in each cab.\n")
# uncomment buses in line 11 above to see the error if undefined variables are used

print ("we have", vehicles ," vehicles available for use")

