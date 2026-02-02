from math import pi
# calculates the area of a circle gets radius as a parameter
def calc_circle_area(radius):
    if radius < 0:
        return 'error cant have negative values in geometric shapes'
    else:
        return pi * radius ** 2

 # calculates the area of a triangle get base and hight as parameters  
def calc_triangle_area(hight,base):
    if hight < 0 or base < 0:
        return 'error cant have negative values in geometric shapes'
    return hight * base / 2

# calculates the area of a square get side1 and side2 as parameters
def calc_square_area(side1,side2):
    if side1 < 0 or side2 < 0:
        return 'error cant have negative values in geometric shapes'
    return side1 * side2