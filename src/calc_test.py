'''
# Nazov projektu: Projekt kalkulacka
# Subor: calc_test.py
# Datum: 24.3.2020
# Autor: xvadov01, xsmata03
#
# Popis: Testy matematickej kniznice calc.py
#
'''
##
# @file calc_test.py
# @brief Testy matematickej knižnice calc.py

# run with: python3 -m unittest calc_test

import unittest
from calc import *

## @class AddTest
# @brief Testy funkcie add()
# @param unittest.TestCase
class AddTest(unittest.TestCase):

    ##
    # @test Sčítanie pozitívych hodnôt
    # @param self Ukazateľ na triedu
    def test_add_positive(self):
        self.assertEqual(add(1, 100), 101)
        self.assertEqual(add(32768, 32768), 65536)
        self.assertEqual(add(2147483648, 2147483648), 4294967296)

    ##
    # @test Sčítanie negatívnych hodnôt
    # @param self Ukazateľ na triedu
    def test_add_negative(self):
        self.assertEqual(add(-2, -10), -12)
        self.assertEqual(add(-32768, -32768), -65536)
        self.assertEqual(add(-2147483648, -2147483648), -4294967296)

    ##
    # @test Sčítanie hodnôt s desatinnou časťou
    # @param self Ukazateľ na triedu    
    def test_add_floating(self):
        self.assertAlmostEqual(add(2.2291, 9.882), 12.1111, 8)
        self.assertAlmostEqual(add(-88183.293, -19383.28), -107566.573, 8)
        self.assertAlmostEqual(add(-29.11, 29994.238), 29965.128, 8)
        self.assertAlmostEqual(add(281.20398173, 0.184875102391), 281.388856832391, 8)

    ##
    # @test Sčítanie kombinovaných hodnôt(kladné, záporné, desatinné, celé čísla)
    # @param self Ukazateľ na triedu
    def test_add_combined(self):
        self.assertEqual(add(-2844.1, 9288), 6443.9)
        self.assertEqual(add(-184413, -138941.22), -323354.22)

## @class SubtractTest
# @brief Testy funkcie substract()
# @param unittest.TestCase
class SubtractTest(unittest.TestCase):

    ##
    # @test Odčítanie nezáponých hodnôt
    # @param self Ukazateľ na triedu
    def test_sub_positive(self):
        self.assertEqual(subtract(201, 102), 99)
        self.assertEqual(subtract(0, 65536), -65536)
    
    ##
    # @test Odčítanie záporných hodnôt a nuly
    # @param self Ukazateľ na triedu
    def test_sub_negative(self):
        self.assertEqual(subtract(-183, -248881), 248698)
        self.assertEqual(subtract(-199234, 0), -199234)

    ##
    # @test Odčítanie hodnôt s desatinnou časťou
    # @param self Ukazateľ na triedu
    def test_sub_floating(self):
        self.assertAlmostEqual(subtract(2.1231, 21.312), -19.1889, 8)
        self.assertAlmostEqual(subtract(-12.138, -1283.2), 1271.062, 8)
        self.assertAlmostEqual(subtract(-2912.39, 2919992.2), -2922904.59, 8) 

    ##
    # @test Odčítanie kombinovaných hodnôt(kladné, záporné, desatinné, celé čísla)
    # @param self Ukazateľ na triedu
    def test_sub_combined(self):
        self.assertEqual(subtract(21, -1.19), 22.19)
        self.assertEqual(subtract(-3, -1.2), -1.8)

## @class MultiplyTest
# @brief Testy funkcie multiply()
# @param unittest.TestCase
class MultiplyTest(unittest.TestCase):

    ##
    # @test Násobenie nulou
    # @param self Ukazateľ na triedu
    def test_mul_zero(self):
        self.assertEqual(multiply(2199, 0), 0)
        self.assertEqual(multiply(0, 0), 0)

    ##
    # @test Násobenie kladnými hodnotami
    # @param self Ukazateľ na triedu
    def test_mul_positive(self):
        self.assertEqual(multiply(21, 1), 21)
        self.assertEqual(multiply(281, 1391), 390871)
        self.assertEqual(multiply(2919389, 1000), 2919389000)

    ##
    # @test Násobenie zápornými hodnotami
    # @param self Ukazateľ na triedu
    def test_mul_negative(self):
        self.assertEqual(multiply(-12, -2), 24)
        self.assertEqual(multiply(-2919389, -1000), 2919389000)

    ##
    # @test Násobenie hodnôt s desatinnou časťou
    # @param self Ukazateľ na triedu
    def test_mul_floating(self):
        self.assertAlmostEqual(multiply(1.293, 4.7), 6.0771, 8)
        self.assertAlmostEqual(multiply(-183.18, 487.648), -89327.36064, 8)

    ##
    # @test Násobenie kombinovaných hodnôt(kladné, záporné, desatinné, celé čísla)
    # @param self Ukazateľ na triedu
    def test_mul_combined(self):
        self.assertAlmostEqual(multiply(255, -16.7), -4258.5, 8)
        self.assertAlmostEqual(multiply(-385.2, 284.1022), -109436.16744, 8)

## @class DivideTest
# @brief Testy funkcie divide()
# @param unittest.TestCase
class DivideTest(unittest.TestCase):

    ##
    # @test Delenie nulou
    # @param self Ukazateľ na triedu
    def test_div_zero(self):
        self.assertEqual(divide(0, 182), 0)
        self.assertRaises(ValueError, divide, 283, 0)
        self.assertRaises(ValueError, divide,-284.1, 0)

    ##
    # @test Delenie kladných hodnôt
    # @param self Ukazateľ na triedu
    def test_div_positive(self):
        self.assertEqual(divide(290, 2), 145.0)
        self.assertEqual(divide(64905, 5), 12981.0)

    ##
    # @test Delenie záporných hodnôt kladnými hodnotami
    # @param self Ukazateľ na triedu
    def test_div_negative(self):
        self.assertEqual(divide(-291, 2), -145.5)
        self.assertEqual(divide(-201410040, 80), -2517625.5)

    ##
    # @test Delenie hodnôt s desatinnou časťou
    # @param self Ukazateľ na triedu
    def test_div_floating(self):
        self.assertAlmostEqual(divide(2.46, 1.2), 2.05, 8)
        self.assertAlmostEqual(divide(91664.0, -918725.0), -0.0997730550, 8)

    ##
    # @test Delenie kombinovaných hodnôt(kladné, záporné, desatinné, celé čísla)
    # @param self Ukazateľ na triedu
    def test_div_combined(self):
        self.assertAlmostEqual(divide(940, 3.333), 282.028202820, 8)
        self.assertAlmostEqual(divide(-1920002.15, 69), -27826.1181159420, 8)
        self.assertAlmostEqual(divide(-385.1, -1), 385.1, 8)

## @class ToThePowerOfTest
# @brief Testy funkcie to_the_power_of()
# @param unittest.TestCase
class ToThePowerOfTest(unittest.TestCase):

    ##
    # @test Umocňovanie nulou - výsledok je vždy 1
    # @param self Ukazateľ na triedu
    def test_to_the_power_of_zero(self):
        self.assertEqual(to_the_power_of(0, 0), 1)
        self.assertEqual(to_the_power_of(131, 0), 1)
        self.assertEqual(to_the_power_of(-131, 0), 1)
        self.assertEqual(to_the_power_of(-23.29, 0), 1)
        self.assertEqual(to_the_power_of(23.29, 0), 1)
        
    ##
    # @test Umocňovanie párnym číslom
    # @param self Ukazateľ na triedu    
    def test_to_the_power_of_even(self):
        self.assertEqual(to_the_power_of(17, 2), 289)
        self.assertEqual(to_the_power_of(-7, 4), 2401)
        self.assertEqual(to_the_power_of(23.29, 4), 294223.90426081)
        self.assertEqual(to_the_power_of(-23.29, 2), 542.4241)
    
    ##
    # @test Umocňovanie nepárnym číslom
    # @param self Ukazateľ na triedu
    def test_to_the_power_of_odd(self):
        self.assertEqual(to_the_power_of(17, 3), 4913)
        self.assertEqual(to_the_power_of(-7, 1), -7)
        self.assertAlmostEqual(to_the_power_of(23.29, 5), 6852474.73023, 5)
        self.assertAlmostEqual(to_the_power_of(-23.29, 3), -12633.057289, 6)
        
    ##
    # @test Umocňovanie dvojkou
    # @param self Ukazateľ na triedu
    def test_to_the_power_of_two(self):
        self.assertEqual(to_the_power_of(131, 2), 17161)
        self.assertEqual(to_the_power_of(997, 2), 994009)
        self.assertEqual(to_the_power_of(-191, 2), 36481)
        self.assertEqual(to_the_power_of(-313, 2), 97969)
        self.assertEqual(to_the_power_of(4,), 16)

    ##
    # @test Umocňovanie záporným párnym číslom - ValueError
    # @test Umocňovanie desatinným číslom - ValueError
    # @test Umocňovanie záporným desatinným číslo - ValueError
    # @test Umocňovanie záporným nepárnym číslom - ValueError
    # @param self Ukazateľ na triedu 
    def test_failure_to_the_power_of(self):
        self.assertRaises(ValueError, to_the_power_of, -313, -2)                   # exponent must be a Natural number (negative even number)
        self.assertRaises(ValueError, to_the_power_of, 191, 7.3)                   # exponent must be a Natural number (floating point number)
        self.assertRaises(ValueError, to_the_power_of, 313, -3.17)                 # exponent must be a Natural number (negative floating point number)
        self.assertRaises(ValueError, to_the_power_of, 17, -5)                     # exponent must be a Natural number (negative odd number)
        self.assertRaises(ValueError, to_the_power_of, 10.0, 500)                     # exponent must be a Natural number (negative odd number)
        
## @class RootTest
# @brief Testy funkcie root()
# @param unittest.TestCase
class RootTest(unittest.TestCase): # radicand and then index: square root of 4... root(4, 2) or root(4, )
    
    ##
    # @test Odmocnina nuly - výsledok je vždy 0
    # @param self Ukazateľ na triedu
    def test_root_of_zero(self):
        self.assertEqual(root(0, ), 0)
        self.assertEqual(root(0, 2), 0)
        self.assertEqual(root(0, 5), 0)
        
    ##
    # @test Druhá odmocnina
    # @param self Ukazateľ na triedu    
    def tets_square_root_of(self):
        self.assertEqual(root(64, ), 8)
        self.assertAlmostEqual(root(100.5, ), 10.02497, 5)
        self.assertEqual(root(16, 2), 4)

    ##
    # @test Párna odmocnina
    # @param self Ukazateľ na triedu
    def test_even_root_of(self):
        self.assertAlmostEqual(root(64, 4), 2.82843, 5)
        self.assertEqual(root(15625, 6), 5)
        self.assertEqual(root(10000000000, 10), 10)

    ##
    # @test Nepárna odmocnina
    # @param self Ukazateľ na triedu
    def test_odd_root_of(self):
        self.assertEqual(root(-27, 3), -3)
        self.assertEqual(root(27, 3), 3)
        self.assertEqual(root(100000, 5), 10)
        self.assertEqual(root(-100000, 5), -10)
        self.assertAlmostEqual(root(-1000.5, 3), -10.00167, 5)
        self.assertAlmostEqual(root(100000.5, 5), 10.00001, 5)

    ##
    # @test Odmocňovanie záporným číslom - ValueError
    # @test Záporné číslo nie je možné odmocniť párnou odmocninou(v množine reálnych čísel) - ValueError
    # @test Desatinná odmocnina - ValueError
    # @test Záporná desatinná odmocnina - ValueError
    # @test Záporná odmocnina - ValueError
    # @test Nultá odmocnina - ValueError
    # @param self Ukazateľ na triedu 
    def test_failure_root_of(self):
        self.assertRaises(ValueError, root, -313, )                 # radicand of a square root must not be negative
        self.assertRaises(ValueError, root, -313, 4)                # radicand of an even root must not be negative
        self.assertRaises(ValueError, root, 191, 7.3)                # root index must be a Natural number
        self.assertRaises(ValueError, root, 313, -3.17)              # root index must be a Natural number
        self.assertRaises(ValueError, root, 17, -5)                  # root index must be a Natural number
        self.assertRaises(ValueError, root, 19, 0)                  # root index must not be zero

## @class FactorialTest
# @brief Testy funkcie factorial()
# @param unittest.TestCase
class FactorialTest(unittest.TestCase):

    ##
    # @test Faktorial rôznych čísel
    # @param self Ukazateľ na triedu
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(12), 479001600)
        self.assertEqual(factorial(18), 6402373705728000)

    ##
    # @test Faktorial desatinného čísla - ValueError
    # @test Faktorial záporného čísla - ValueError
    # @param self Ukazateľ na triedu
    def test_faulire_factorial(self):
        self.assertRaises(ValueError, factorial, 3.13)
        self.assertRaises(ValueError, factorial, -313)                          # negative number given

## @class PrimeNumberTest
# @brief Testy funkcie prime()
# @param unittest.TestCase
class PrimeNumberTest(unittest.TestCase): # radicand and then index: square root of 4... root(4, 2) or root(4, )
    
    ##
    # @test Testy určenia, či sú čísla rôznej hodnoty správne určené ako prvočísla
    # @param self Ukazateľ na triedu
    def test_prime(self):
        self.assertTrue(prime(191))
        self.assertTrue(prime(2999957))
        self.assertTrue(prime(75437))
        self.assertFalse(prime(0))
        self.assertFalse(prime(1))
        self.assertFalse(prime(64))
        self.assertFalse(prime(245655))
    
    ##
    # @test Prvočíslo nemôže byť záporné číslo
    # @test Prvočíslo nemôže byť záporné desatinné číslo
    # @test Prvočíslo nemôže byť desatinné číslo
    # @param self Ukazateľ na triedu
    def test_failure_prime(self):
        self.assertRaises(ValueError, prime, -84184)                 # operand must not be negative
        self.assertRaises(ValueError, prime, -123.1)                 # operand must be a Natural number
        self.assertRaises(ValueError, prime, 123.15)                 # operand must be a Natural number

if __name__ == '__main__':
    unittest.main()

### Koniec súboru calc_test.py ###