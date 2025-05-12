#tire volume

import math
from datetime import datetime

# promt user for the tire dimentions ...
width = int(input("What is the width of the tire? "))
aspect_ratio = int(input("What is the aspect ratio of the tire? "))
diameter = int(input("What is the aspect ratio of the tire? " ))
# calculating the volume using the given formula
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000 
# display result
print(f"\nThe approximate volume is {volume:.2f} liters.")

# getting current date (without time)
current_date = datetime.now().date()

# opening file in appending mode and writing data 
with open("volumes.txt", "a") as file:
    file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}\n")

