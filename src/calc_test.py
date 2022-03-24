##
# @file calc_test.py
# @brief Tests of mathlib

# run with: python3 -m unittest calc

import unittest
from calc import *

class AddTest(unittest.TestCase):
    
    def test_add_positive(self):
        self.assertEqual(add(1, 100), 101)
        self.assertEqual(add(32768, 32768), 65536)
        self.assertEqual(add(2147483648, 2147483648), 4294967296)

    def test_add_negative(self):
        self.assertEqual(add(-2, -10), -12)
        self.assertEqual(add(-32768, -32768), -65536)
        self.assertEqual(add(-2147483648, -2147483648), -4294967296)
        
    def test_add_floating(self):
        self.assertAlmostEqual(add(2.2291, 9.882), 12.1111, 4)
        self.assertAlmostEqual(add(-88183.293, -19383.28), -107566.573, 3)
        self.assertAlmostEqual(add(-29.11, 29994.238), 29965.128, 3)

    def test_add_combined(self):
        self.assertEqual(add(-2844.1, 9288), 6443.9)
        self.assertEqual(add(-184413, -138941.22), -323354.22)


class SubtractTest(unittest.TestCase):

    def test_sub_positive(self):
        self.assertEqual(subtract(201, 102), 99)
        self.assertEqual(subtract(0, 65536), -65536)
        
    def test_sub_negative(self):
        self.assertEqual(subtract(-183, -248881), 248698)
        self.assertEqual(subtract(-199234, 0), -199234)

    def test_sub_floating(self):
        self.assertAlmostEqual(subtract(2.1231, 21.312), -19.1889, 4)
        self.assertAlmostEqual(subtract(-12.138, -1283.2), 1271.062, 3)
        self.assertAlmostEqual(subtract(-2912.39, 2919992.2), -29202904.59, 2) 

    def test_sub_combined(self):
        self.assertEqual(subtract(21, -1.19), 22.19)
        self.assertEqual(subtract(-3, -1.2), 1.8)

class MultiplyTest(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(multiply(2199, 0), 0)
        self.assertEqual(multiply(0, 0), 0)

    def test_mul_positive(self):
        self.assertEqual(multiply(21, 1), 21)
        self.assertEqual(multiply(281, 1391), 390871)
        self.assertEqual(multiply(2919389, 1000), 2919389000)

    def test_mul_negative(self):
        self.assertEqual(multiply(-12, -2), 24)
        self.assertEqual(multiply(-2919389, -1000), 2919389000)

    def test_mul_floating(self):
        self.assertAlmostEqual(multiply(1.293, 4.7), 6.0771, 4)
        self.assertAlmostEqual(multiply(-183.18, 487.648), -91159.16064, 5)

    def test_mul_combined(self):
        self.assertAlmostEqual(multiply(255, -16.7), -4258.5, 1)
        self.assertAlmostEqual(multiply(-385.2, 284.1022), -109436.16744, 5)

class DivideTest(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(divide(0, 182), 0)
        self.assertRaises(ValueError, divide(283, 0))
        self.assertRaises(ValueError, divide(-284.1, 0))

    def test_div_positive(self):
        self.assertEqual(divide(290, 2), 145)
        self.assertEqual(divide(64905, 5), 12891)

    def test_div_negative(self):
        self.assertEqual(divide(-291, 2), -145.5)
        self.assertEqual(divide(-201410040, 80), -2517625.5)

    def test_div_floating(self):
        self.assertAlmostEqual(divide(2.46, 1.2), 2.05, 2)
        self.assertAlmostEqual(divide(91664, -918725), 0.0997730550, 10)

    def test_div_combined(self):
        self.assertAlmostEqual(divide(940, 3.333), 100.717882781, 9)
        self.assertAlmostEqual(divide(-1920002.15, 69), -27.826.118115, 6)
        self.assertAlmostEqual(divide(-385.1, -1), 385.1, 1)
