# function devides num1 by num2 and returns error message if num2 is 0
def add(num1,num2):
    return num1 + num2

def divide(num1,num2):
    if num2 == 0:
        return 'error cant divide by zero'
    return num1 / num2

#returns the num1 in power of num
def power(num1,num2):
    return num1 ** num2