# Chapter 4 Exercise

# Defines the number of cars.
cars = 100
# Defines the number of seats available in each car.
space_in_a_car = 4.0
# Defines the number of drivers.
drivers = 30
# Defines the number of passengers.
passengers = 90
# Defines the number of cars not drivern.
cars_not_driven = cars - drivers
# Defines the number of cars that are driven.
cars_driven = drivers
# Calculates the number of passengers who can participate in a carpool.
carpool_capcity = cars_driven * space_in_a_car
# Calculates the average number of passengers per car.
average_passenger_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars todoay."
print "We can trasnport", carpool_capcity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passenger_per_car, "in each car."


# Chapter 4 Study Drills

# 0. Explain the following error:
# Traceback (most recent call last):
    # File "ex4.py", line 8, in <module>
        # average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined

# The error is that the variable 'car_pool_capacity' was not defined earlier in the code.


# 1. I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?

# By using 4.0, it allows the answer to have a decimal out to the tenths place. If the float was not used a float would not be permitted in the answer.


# 2. Remember that 4.0 is a floating point number. It's just a number with a decimal point, and you need 4.0 instead of just 4 so that it is floating point.

# No answer necessary


# 3. Write comments above each of the variable assignments.

# See above.

# 4. Try running python from the Terminal as a calculator like you did before and use variable names to do your calculations. Popular variable names are also i, x, and j.

x = 6
y = 22

print "When you multiply 6 x 22,", x * y, "is the answer."