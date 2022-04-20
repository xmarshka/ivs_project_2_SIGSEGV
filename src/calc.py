'''
# Nazov projektu: Projekt kalkulacka
# Subor: calc.py
# Datum: 25.3.2020
# Autor: xvadov01, xsmata03
#
# Popis: Kniznica s matematickymi funkciami
#
'''

##
# @file calc.py
#
# @brief Knižnica s matematickými funkciami
# @author xvadov01, xsmata03
#

##
# @brief Funkcia vypočíta výsledok sčítania x+y
#
# @param x sčítaniec - reálne číslo
# @param y sčítaniec - reálne číslo
#
# @return Funkcia vracia výsledok sčítania x+y zaokrúhlený na 8 desatinných miest
def add(x, y):
    return round(x + y, 8)

##
# @brief Funkcia vypočíta výsledok odčítania x-y
#
# @param x menšenec - reaálne číslo
# @param y menšiteľ - reálne číslo
#
# @return Funkcia vracia výsledok odčítania x-y zaokrúhlený na 8 desatinných miest
def subtract(x, y):
    return round(x - y, 8)

##
# @brief Funkcia vypočíta výsledok násobenia x*y
#
# @param x činiteľ - reálne číslo
# @param y činiteľ - reálne číslo
#
# @return Funkcia vracia výsledok násobenia x*y zaokrúhlený na 8 desatinných miest
def multiply(x, y):
    return round(x * y, 8)

##
# @brief Funkcia vypočíta výsledok delenia x/y
#
# @param x deliteľ - reálne číslo
# @param y delenec - reálne číslo
#
# @return Funkcia vracia výsledok delenia x/y zaokrúhlený na 8 desatinných miest
def divide(x, y):
    if y == 0:
        raise ValueError("Delenie nulou")

    return round(x / y, 8)

## 
# @brief Funkcia vypočíta n-tú mocninu reálneho čísla
#
# @param base základ - reálne číslo
# @param exponent exponent - prirodzené číslo
#
# @return Funkcia vracia výsledok umocnenia zaokrúhlený na 8 desatinných miest
def to_the_power_of(base, *args):
    if len(args) != 1:
        raise ValueError("Nespavny pocet argumentov")
    else:
        exponent = args[0]
    if not isinstance(exponent, int):
        raise ValueError("Zadaj iba prirodzene cislo")
    elif exponent < 0:
        raise ValueError("Zadaj iba prirodzene čísla")
    return round(base ** exponent, 8)

## 
# @brief Funkcia vypočíta n-tú odmocninu z čísla
#
# @param radicand odmocnenec - reálne číslo
# @param index odmocniteľ - prirodzené cislo
#
# @return Funkcia vracia n-tú odmocninu z čísla zaokrúhlenú na 8 desatinných miest
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
# @brief Funkcia vypočíta faktoriál prirodzeného čísla
#
# @param number prirodzené číslo
#
# @return Funkcia vracia faktoriál čísla
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
# @brief Funkcia určí, či číslo je prvočíslo
#
# @param number prirodzené číslo
#
# @return Funkcia vraci True, ak je číslo pročíslo, inak False
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