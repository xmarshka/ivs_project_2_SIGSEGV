'''
# Názov projektu: Projekt kalkulačka
# Súbor: calc.py
# Dátum: 25.3.2020
# Autor: xvadov01, xsmata03
# Licencia : Projekt je distribuovaný pod licenciou GNU General Public License version 3
#
# Popis: Knižnica s matematickými funkciami
#
'''
##
# @file calc.py
#
# @brief Knižnica s matematickými funkciami
# @author xvadov01, xsmata03
# @copyright Projekt je distribuovaný pod licenciou GNU General Public License version 3 
#

##
# @brief Funkcia vypočíta výsledok sčítania x+y
#
# @param x sčítanec - reálne číslo
# @param y sčítanec - reálne číslo
# @return Funkcia vracia výsledok sčítania x+y zaokrúhlený na 8 desatinných miest
def add(x, y):
    return round(x + y, 8)

##
# @brief Funkcia vypočíta výsledok odčítania x-y
#
# @param x menšenec - reálne číslo
# @param y menšiteľ - reálne číslo
# @return Funkcia vracia výsledok odčítania x-y zaokrúhlený na 8 desatinných miest
def subtract(x, y):
    return round(x - y, 8)

##
# @brief Funkcia vypočíta výsledok násobenia x*y
#
# @param x činiteľ - reálne číslo
# @param y činiteľ - reálne číslo
# @return Funkcia vracia výsledok násobenia x*y zaokrúhlený na 8 desatinných miest
def multiply(x, y):
    return round(x * y, 8)

##
# @brief Funkcia vypočíta výsledok delenia x/y
#
# @param x deliteľ - reálne číslo
# @param y delenec - reálne číslo
# @return Funkcia vracia výsledok delenia x/y zaokrúhlený na 8 desatinných miest
def divide(x, y):
    if y == 0:
        raise ValueError("Delenie nulou")

    return round(x / y, 8)

## 
# @brief Funkcia vypočíta n-tú mocninu reálneho čísla
#
# @param base základ - reálne číslo
# @param args exponent - prirodzené číslo
# @return Funkcia vracia výsledok umocnenia zaokrúhlený na 8 desatinných miest
def to_the_power_of(base, *args):
    if len(args) == 0:
        exponent = 2
    elif len(args) > 1:
        raise ValueError("Nespavny počet argumentov")
    else:
        exponent = args[0]
    if exponent < 0 or not isinstance(exponent, int):
        raise ValueError("Zadaj prirodzené čísla")
    try:
        base ** exponent
    except OverflowError:
        raise ValueError("Príliš vysoké číslo")
    else:
        return round(base ** exponent, 8)

## 
# @brief Funkcia vypočíta n-tú odmocninu z čísla
#
# @param radicand odmocnenec - reálne číslo
# @param args odmocniteľ - prirodzené číslo alebo nič, potom sa doplní 2
# @return Funkcia vracia n-tú odmocninu z čísla zaokrúhlenú na 8 desatinných miest
def root(radicand, *args):
    if len(args) == 0:
        index = 2
    elif len(args) > 1:
        raise ValueError("Nesprávny počet argumentov")
    else:
        index = args[0]
    if index <= 0 or not isinstance(index, int):
        raise ValueError("Zadaj prirodzené číslo")
    elif not(index & 1 == 1) and radicand < 0:
        raise ValueError("Záporný odmocnenec")
    if radicand >= 0:
        return round(radicand ** (1/index), 8)
    else:
        return round(-abs(radicand) ** (1/index), 8)

## 
# @brief Funkcia vypočíta faktoriál prirodzeného čísla
#
# @param number prirodzené číslo
# @return Funkcia vracia faktoriál čísla
def factorial(number):
    if number > 30:
        raise ValueError("Mimo intervalu <0,30>")
    factorial = 1
    if not isinstance(number, int):
        raise ValueError("Zadaj prirodzené číslo")
    elif number < 0:
        raise ValueError("Mimo intervalu <0,30>")
    elif number == 0:
        return factorial
    for i in range(1,number + 1):
           factorial *= i
    return factorial

## 
# @brief Funkcia určí, či číslo je prvočíslo
#
# @param number prirodzené číslo
# @return Funkcia vraci True, ak je číslo pročíslo, inak False
def prime(number):
    if not isinstance(number, int):
        raise ValueError("Zadaj prirodzené číslo")
    elif number < 0:
        raise ValueError("Zadaj prirodzené číslo")
    elif number == 1 or number == 0:
        return False
    elif number & 1 == 0:
        return False
    divisor = 3
    while divisor < number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True

    ### Koniec súboru calc.py ###