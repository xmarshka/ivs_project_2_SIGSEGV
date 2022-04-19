##
# @file calc.py
#
# @brief Python library with mathematical functions
# @author xvadov01, xsmata03
#

##
# @brief Sum of two numbers
#
# @param x first number
# @param y second number
#
# @return sum of numbers x, y
def add(x, y):
    return round(x + y, 8)

##
# @brief Subtraction of two numbers
#
# @param x first number
# @param y second number
#
# @return subtraction of numbers x, y
def subtract(x, y):
    return round(x - y, 8)

##
# @brief Multiplication of two numbers
#
# @param x first number
# @param y second number
#
# @return multiplication of numbers x, y
def multiply(x, y):
    return round(x * y, 8)

##
# @brief Division of two numbers
#
# @param x first number
# @param y second number
#
# @return division of numbers x, y
def divide(x, y):
    if y == 0:
        raise ValueError('Division by zero')

    return round(x / y, 8)

## 
# @brief The function calculates the nth power of the number
#
# @param base Real number
# @param exponent Natural number
#
# @return The result of a exponentiation
def to_the_power_of(base, *args):
    if len(args) != 1:
        raise ValueError("Incorrect count of arguments")
    else:
        exponent = args[0]
    if not isinstance(exponent, int):
        raise ValueError("Number must be a NATURAL NUMBER")
    elif exponent < 0:
        raise ValueError("Number must be a NATURAL NUMBER")
    return round(base ** exponent, 8)

## 
# @brief The function calculates the nth root of the number
#
# @param radicand Real number
# @param index Natural number(An optional parameter - defaul 2)
#
# @return The nth root of a number   
def root(radicand, *args):
    if len(args) == 0:
        index = 2
    elif len(args) > 1:
        raise ValueError("Incorrect count of arguments")
    else:
        index = args[0]
    if not isinstance(index, int):
        raise ValueError("Number must be a NATURAL NUMBER")
    elif index < 0:
        raise ValueError("Number must be a NATURAL NUMBER")
    elif index % 2 == 0 and radicand < 0:
        raise ValueError("Radicand must be a POSITIVE NUMBER")
    if radicand >= 0:
        return round(radicand ** (1/index), 8)
    else:
        return round(-abs(radicand) ** (1/index), 8)

## 
# @brief The function to compute factorial of a natural number
#
# @param number Natural number
#
# @return Factorial of a given natural number
def factorial(number):
    factorial = 1
    if not isinstance(number, int):
        raise ValueError("Number must be a NATURAL NUMBER")
    elif number < 0:
        raise ValueError("Number must be a NATURAL NUMBER")
    elif number == 0:
        return factorial
    for i in range(1,number + 1):
           factorial *= i
    return factorial

## 
# @brief Function to determine whether number is a prime number or not
#
# @param number Natural number
#
# @return True if number is a prime number, else False
def prime(number):
    if not isinstance(number, int):
        raise ValueError("Number must be a NATURAL NUMBER")
    elif number < 0:
        raise ValueError("Number must be a NATURAL NUMBER")
    elif number == 1 or number == 0:
        return False
    elif number & 1 == 0: # number is divisible by 2
        return False
    divisor = 3
    while divisor < number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True