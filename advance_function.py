from class_error import NegativeNumberError
from math import pi
# calculates the area of a circle gets radius as a parameter
def calc_circle_area(radius):
    if radius < 0:
        raise NegativeNumberError
    else:
        return pi * radius ** 2

 # calculates the area of a triangle get base and hight as parameters  
def calc_triangle_area(hight,base):
    if hight < 0 or base < 0:
        raise NegativeNumberError
    return hight * base / 2

# calculates the area of a square get side1 and side2 as parameters
def calc_square_area(side1,side2):
    if side1 < 0 or side2 < 0:
        raise NegativeNumberError
    return side1 * side2