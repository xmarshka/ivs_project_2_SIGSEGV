print("test2")
def prime(number):
    if number & 1 == 0: # number is divisible by 2
        return false
    divisor = 3
    while divisor < number:
        if number % divisor == 0:
            return false
        divisor += 2
    return true