from math import pi
# calculates the area of a circle gets radius as a parameter
def calc_circle_area(radius):
    if radius < 0:
        return 'error cant have negative values in geometric shapes'
    else:
        return pi * radius ** 2
    
def calc_triangle_area(hight,base):
    if hight or base < 0:
        return 'error cant have negative values in geometric shapes'
    return hight * base / 2
    