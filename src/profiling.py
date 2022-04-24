from sys import stdin
from calc import *

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

if __name__ == '__main__':
    inputs = []
    # nacitaj cisla zo stdin oddelene medzerami
    for line in stdin:
        inputs.extend(line.split())
        if not inputs:
            break # prazdny riadok
    standard_deviation(inputs)