import math
from datetime import datetime
import random

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

print("Welcome to the Tire Volume Calculator!\n")

# Prompt user for tire dimensions with validation
width = get_int_input("Enter the width of the tire in mm: ")
aspect_ratio = get_int_input("Enter the aspect ratio of the tire: ")
diameter = get_int_input("Enter the diameter of the wheel in inches: ")

# Calculate volume
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
print(f"\nThe approximate volume is {volume:.2f} liters.")

# Optional: estimate tire price
price = round(random.uniform(50, 200), 2)
print(f"Estimated tire price: ${price}")

# Ask if user wants to be contacted
contact_choice = input("Would you like to be contacted with tire purchase options? (yes/no): ").strip().lower()

name = phone = None
if contact_choice in ["yes", "y"]:
    name = input("Enter your name: ").strip()
    phone = input("Enter your phone number: ").strip()

# Get current date
current_date = datetime.now().date()

# Log the data to volumes.txt
with open("volumes.txt", "a") as file:
    file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, ${price}")
    if name and phone:
        file.write(f", {name}, {phone}")
    file.write("\n")

print("\nThank you for using the Tire Volume Calculator!")
