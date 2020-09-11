import math

x = 5

radius_str = input("Enter the radius of a circle: ")
radius_int = int(radius_str)

def circumference():
    c = 2 * math.pi * radius_int
    return c

def area():
    a = math.pi *(radius_int ** 2)
    return a