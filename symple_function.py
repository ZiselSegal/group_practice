
# subtracts num2 from num1
def subtract(num1,num2):
    return num1-num2

# adds both variables
def add(num1,num2):
    return num1 + num2

# function devides num1 by num2 and returns error message if num2 is 0
def divide(num1,num2):
    if num2 == 0:
        return 'error cant divide by zero'
    return num1 / num2

#returns the num1 in power of num
def power(num1,num2):
    return num1 ** num2

#returns the absolute value of num
def absolute_val(num1):
    return abs(num1)