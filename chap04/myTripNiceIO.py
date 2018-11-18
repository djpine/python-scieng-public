"""Calculates time, gallons of gas used, and cost of gasoline
for a trip"""

distance = float(input("Input trip distance (miles): "))

mpg = 30.             # car mileage
speed = 60.           # average speed
costPerGallon = 2.85  # price of gasoline

time = distance/speed
gallons = distance/mpg
cost = gallons*costPerGallon

print("\nDuration of trip = {0:0.1f} hours".format(time))
print("Gasoline used = {0:0.1f} gallons (@ {1:0.0f} mpg)"
      .format(gallons, mpg))
print("Cost of gasoline = ${0:0.2f} (@ ${1:0.2f}/gallon)"
      .format(cost, costPerGallon))

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-01-06

Scripting example with formatted print output
"""
