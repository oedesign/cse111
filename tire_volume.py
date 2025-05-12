#tire volume

import math

# promt user for the tire dimentions ...
width = int(input("What is the width of the tire? "))
aspect_ratio = int(input("What is the aspect ratio of the tire? "))
diameter = int(input("What is the aspect ratio of the tire? " ))
# Calculating the volume using the given formula
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000 # given formular
print(f"\nThe approximate volume is {volume:.2f} liters.")

