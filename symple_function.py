from class_error import NegativeNumberError,ZeroPowerZeroError
# subtracts num2 from num1
def subtract(num1,num2):
    return num1-num2

# adds both variables
def add(num1,num2):
    return num1 + num2

# function devides num1 by num2 and returns error message if num2 is 0
def divide(num1,num2):
    return num1 / num2

#returns the num1 in power of num
def power(num1,num2):
    if num1 == 0 and num2 == 0:
        raise ZeroPowerZeroError
    return num1 ** num2

#returns the absolute value of num
def absolute_val(num1):
    return abs(num1)

#returns num1 in root num2
def root(num1,num2):
    if num1 < 0 :
        raise NegativeNumberError
    else:
        return num1 ** (1/num2)
   