#code along activities BYU Idaho ...

import math

def main():
    name= '#1 Picnic'
    radius= 6.83
    height= 10.16
    volume= can_volume(radius, height)
    area= can_area(radius, height)
    can_efficiency= volume/area
    print(f"Can name: {name} \nCan volume: {volume:.2f} \ncan_area: {area:.2f} \ncan_efficiency: {can_efficiency:.2f} ") 

def can_volume(radius, height):
    """Calculate the volume of a cylinder."""
    volume= math.pi * radius**2 * height
    return volume

def can_area(radius, height):
    """Calculate the surface area of a cylinder."""
    area=2 * math.pi * radius * (radius + height)
    return area
main()