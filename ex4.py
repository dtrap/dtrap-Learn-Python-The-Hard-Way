# the amount of cars we have is 100
cars = 100
# the space we have in the car is enough for 4 passengers
space_in_a_car = 4.0
# the number of drivers that we have is 30
drivers = 30
# the number of passengers we have is 80
passengers = 90
# we can create a function that tells us how many cars won't be driven by subtracting the cars from drivers...this gives us excess cars
cars_not_driven = cars - drivers
# we can equate drivers to cars driven, thereby renaming the variable because this is ultimately interchangable. 
cars_driven = drivers
# we can calculate the carpool capactiy by taking the product of the cars_driven and the space_in_the_car (these are the available seats
carpool_capacity = cars_driven * space_in_a_car
# we can produce an average of the number of passengers in the car by dividing the passengers by the numbers of cars driven.
average_passengers_per_car = passengers / cars_driven

# We can get the number of cars to print with text that makes this make sense by having the computer print normal English to give context for the variable.
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# From bottom to top- we ultimately want to figure our how many passengers we can put in each car. So we need to know how many passengers we have to carpool today, then the capacity of the carpools, free cars, free drivers and total cars we got. Boom goes the dynamite!
