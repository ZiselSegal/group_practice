from symple_function import multiply,divide,add,subtract,absolute_val,power
from advance_function import calc_circle_area,calc_triangle_area,calc_square_area
from class_error import NegativeNumberError, ZeroPowerZeroError

def menu():
    while True:
        try:
            func_choice = input("""please choose which of the following functions: 
                                                            1. multiply function
                                                            2. divide function
                                                            3. add function
                                                            4. subtraction function
                                                            5. 2 variable power function
                                                            6. 2 variable root function
                                                            7. absolute value function
                                                            8. area of triangle
                                                            9. area of rectangle/square function
                                                            10. are of circe function 
                                                            11. to exit program
                                """)
            func_choice = int(func_choice)
            break
        except ValueError:
            print("please eneter an action number not a string ")
    if func_choice != 11:
        match func_choice:
            case 1:
                while True:
                    try:
                        a = int(input("the first value"))
                        b = int(input("the second value"))
                        result = multiply(a,b)
                        print(f"{a}*{b}={result}")
                        break
                    except ValueError:
                        print("please eneter a number not a string ")
            case 2: 
                while True:
                    try:
                        a = int(input("the first value"))
                        b = int(input("the second value"))
                        result = divide(a,b)
                        print(f"{a}/{b}={result}")
                        break
                    except ValueError:
                        print("please eneter a number not a string ")
                    except ZeroDivisionError:
                        print("cannot devide by zero. PLease try again")
            case 3:
                while True:
                    try:
                        a = int(input("the first value"))
                        b = int(input("the second value"))
                        result = add(a,b)
                        print(f"{a}+{b}={result}")
                        break
                    except ValueError:
                        print("please eneter a number not a srtring")
            case 4:
                while True:
                    try:
                        a = int(input("the first value"))
                        b = int(input("the second value"))
                        result = subtract(a,b)
                        print(f"{a}-{b}={result}")
                        break
                    except ValueError:
                        print("please eneter a number not a string")
            case 5:
                while True:
                    try:
                        a = int(input("the base value"))
                        b = int(input("the power value"))
                        result = power(a,b)
                        print(f"{a}^{b}={result}")
                        break
                    except ValueError:
                        print("please eneter a number not a string ")
                    except ZeroPowerZeroError:
                        print("0^0 is undefined. Please try again")
                    except NegativeNumberError:
                        print("0^(negative value) is undefioned. Please try again")
            case 6:
                while True:
                    try:
                        a = int(input("the radicand value"))
                        b = int(input("the index value"))
                        result = root(a,b)
                        print(f"{a}root{b}={result}")
                        break
                    except ValueError:
                        print("please eneter a number not a string ")
                    except NegativeNumberError:
                        print("can do only Real numbers. Please try again")
            case 7: 
                while True:
                    try:
                        a = int(input("the value"))
                        result = absolute_val(a,b)
                        print(f"|{a}|={result}")
                        break
                    except ValueError:
                        print("please eneter a number not a string ")
            case 8:
                while True:
                    try:
                        a = int(input("the hight value"))
                        b = int(input("the base value"))
                        result = calc_triangle_area(a,b)
                        print(f"height:{a}, base:{b} ={result}")
                        break
                    except ValueError:
                        print("please eneter a number not a string")
                    except NegativeNumberError:
                        print("geometric values must be positive. please try again ")
            case 9:
                while True:
                    try:
                        a = int(input("the both sides value"))
                        b = int(input("the top and bottom value. Optional"))
                        result = calc_square_area(a,b=a)
                        print(f"height:{a}, base:{b} ={result}")
                        break
                    except ValueError:
                        print("please eneter a number not a string ")
                    except NegativeNumberError:
                        print("geometric values must be positive. please try again ")
            case 10:
                while True:
                    try:
                        a = int(input("the hight value"))
                        b = int(input("the base value"))
                        result = calc_circle_area(a,b)
                        print(f"height:{a}, base:{b} ={result}")
                        break
                    except ValueError:
                        print("please eneter a number not a string ")
                    except NegativeNumberError:
                        print("geometric values must be positive. please try again ")
            case _:
                print("sorry no such function")
