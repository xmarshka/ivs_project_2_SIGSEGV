##
# @file calc.py
# @brief Mathematic library
# @author Matej Vadovic, Andrej Smatana

##
# @brief Sum of two numbers
#
# @param x first number
# @param y second number
#
# @return sum of numbers x, y
def add(x, y):
    return round(x + y, 10)

##
# @brief Subtraction of two numbers
#
# @param x first number
# @param y second number
#
# @return subtraction of numbers x, y
def subtract(x, y):
    return round(x - y, 10)

##
# @brief Multiplication of two numbers
#
# @param x first number
# @param y second number
#
# @return multiplication of numbers x, y
def multiply(x, y):
    return round(x * y, 10)

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

    return round(x / y, 10)

def prime(number):
    if number & 1 == 0: # number is divisible by 2
        return false
    divisor = 3
    while divisor < number:
        if number % divisor == 0:
            return false
        divisor += 2
    return true
