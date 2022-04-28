'''
# Názov projektu: Projekt kalkulačka
# Súbor: profilling.py
# Dátum: 26.3.2020
# Autor: xsmata03
# Licencia : Projekt je distribuovaný pod licenciou GNU General Public License version 3
#
# Popis: Program pre výpočet výberovej smerodajnej odchýlky
#
'''

##
# @file profilling.py
#
# @brief Program pre výpočet výberovej smerodajnej odchýlky
# @author xsmata03
# @copyright Projekt je distribuovaný pod licenciou GNU General Public License version 3 
#

import random
from sys import stdin
from calc import *

##
# @brief Funkcia počíta výberovú smerodajnú odchýlku
#
# @param numbers pole čísel
#
def standard_deviation(numbers):
    n = len(numbers)
    x_avg = 0
    res = 0
    for i in numbers:
        x_avg = add(int(i), x_avg) # sucet cisel v poli
        res = add(to_the_power_of(int(i), 2), res) # sucet kvadratov cisel v poli

    x_avg = divide(x_avg, n) # x (aritmeticky priemer)
    x_avg = multiply(n, to_the_power_of(int(x_avg), 2)) # N * x^2
    s = multiply(subtract(res, x_avg), divide(1, n-1)) # vyraz pod odmocninou ((res - x^2) / n-1)
    s = root(s, 2)

    print(s) # vysledok smerovej odchylky 

##
# @brief Vyplnenie poľa náhodnými číslami
#
# @param n počet čísel v poli
# @param numbers pole čísel
#
def generate_numbers(n, numbers):
    random.seed() # nastavenie seedu na systemovy cas
    for i in range(1, n+1):
        # append to numbers array random integer
        numbers.append(random.randint(1, 1000))

if __name__ == '__main__':
    inputs = []
    # nacitaj cisla zo stdin oddelene medzerami
    if not stdin.isatty():
        for line in stdin:
            inputs.extend(line.split())
            if not inputs:
                break # prazdny riadok
    else:
        generate_numbers(1000, inputs)

    standard_deviation(inputs)

### Koniec súboru profilling.py ###