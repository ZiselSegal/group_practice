from math import pi
def calc_circle_area(radius):
    if radius < 0:
        return "no negative radius"
    else:
        return pi * radius ** 2
    