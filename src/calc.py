##
# @file calc.py
#
# @brief Kniznica s matematickymi funkciami
# @author xvadov01, xsmata03
#

##
# @brief Funkcia vypocita vysledok scitania x+y
#
# @param x scitaniec - realne cislo
# @param y scitaniec - realne cislo
#
# @return Funkcia vracia vysledok scitania x+y, zaokruhleny na 8 desatinnych miest
def add(x, y):
    return round(x + y, 8)

##
# @brief Funkcia vypocita vysledok odcitania x-y
#
# @param x mensenec - realne cislo
# @param y menistel - realne cislo
#
# @return Funkcia vracia vysledok odcitania x-y, zaokruhleny na 8 desatinnych miest
def subtract(x, y):
    return round(x - y, 8)

##
# @brief Funkcia vypocita vysledok nasobenia x*y
#
# @param x cinitel - realne cislo
# @param ycinitel - realne cislo
#
# @return Funkcia vracia vysledok nasobenia x*y, zaokruhleny na 8 desatinnych miest
def multiply(x, y):
    return round(x * y, 8)

##
# @brief Funkcia vypocita vysledok delenia x/y
#
# @param x delitel - realne cislo
# @param y delenec - realne cislo
#
# @return Funkcia vracia vysledok delenia x/y, zaokruhleny na 8 desatinnych miest
def divide(x, y):
    if y == 0:
        raise ValueError("Delenie nulou")

    return round(x / y, 8)

## 
# @brief Funkcia vypocita n-tu mocninu realneho cisla
#
# @param base zaklad - realne cislo
# @param exponent exponent - prirodzene cislo
#
# @return Funkcia vracia vysledok umocnenia zaokruhleny na 8 desatinnych miest
def to_the_power_of(base, *args):
    if len(args) != 1:
        raise ValueError("Nespavny pocet argumentov")
    else:
        exponent = args[0]
    if not isinstance(exponent, int):
        raise ValueError("Zadaj iba prirodzene cislo")
    elif exponent < 0:
        raise ValueError("Zadaj iba prirodzene cisla")
    return round(base ** exponent, 8)

## 
# @brief Funkcia pocita n-tu odmocninu z cisla
#
# @param radicand odmocnenec - realne cislo
# @param index odmocnitel - prirodzene cislo
#
# @return Funkcia vracia n-tu odmocninu z cisla zaokruhlenu na 8 desatinnych miest
def root(radicand, *args):
    if len(args) == 0:
        index = 2
    elif len(args) > 1:
        raise ValueError("Nespavny pocet argumentov")
    else:
        index = args[0]
    if not isinstance(index, int):
        raise ValueError("Zadaj iba prirodzene cislo")
    elif index < 0:
        raise ValueError("Zadaj iba prirodzene cislo")
    elif index % 2 == 0 and radicand < 0:
        raise ValueError("Odmocnenec musi byt nezaporne cislo")
    if radicand >= 0:
        return round(radicand ** (1/index), 8)
    else:
        return round(-abs(radicand) ** (1/index), 8)

## 
# @brief Funkcia vypocita faktorial prirodzeneho cisla
#
# @param number prirodzene cislo
#
# @return Funkcia vracia faktorial cisla
def factorial(number):
    factorial = 1
    if not isinstance(number, int):
        raise ValueError("Zadaj iba prirodzene cislo")
    elif number < 0:
        raise ValueError("Zadaj iba prirodzene cislo")
    elif number == 0:
        return factorial
    for i in range(1,number + 1):
           factorial *= i
    return factorial

## 
# @brief Funkcia urci, ci cislo je prvocislo
#
# @param number prirodzene cislo
#
# @return Funkcia vraci True, ak je cislo prvocislo, inak False
def prime(number):
    if not isinstance(number, int):
        raise ValueError("Zadaj iba prirodzene cislo")
    elif number < 0:
        raise ValueError("Zadaj iba prirodzene cislo")
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