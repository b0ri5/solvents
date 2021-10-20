import unittest

from math import gcd
from reduced_residue_system import (
    _reduced_residue_system_primorial_brute_force, filter_twin_primes,
    filter_twos, reduced_residue_system_primorial,
    reduced_residue_system_primorial_twos)
from sympy import primorial


class Test(unittest.TestCase):

    def test_reduced_residue_system_primorial_brute_force(self):
        self.assertEqual({1}, _reduced_residue_system_primorial_brute_force(1))
        self.assertEqual({1, 5},
                         _reduced_residue_system_primorial_brute_force(2))
        self.assertEqual({1, 7, 11, 13, 17, 19, 23, 29},
                         _reduced_residue_system_primorial_brute_force(3))
        self.assertEqual(
            {
                1, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
                71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 121, 127, 131,
                137, 139, 143, 149, 151, 157, 163, 167, 169, 173, 179, 181, 187,
                191, 193, 197, 199, 209
            }, _reduced_residue_system_primorial_brute_force(4))

    def test_reduced_residue_system_primorial_brute_force_sizes(self):
        sizes = {
            len(_reduced_residue_system_primorial_brute_force(i))
            for i in range(1, 7)
        }
        # See https://oeis.org/A005867
        self.assertEqual({1, 2, 8, 48, 480, 5760}, sizes)

    def test_reduced_residue_system_primorial(self):
        self.assertEqual({1}, reduced_residue_system_primorial(1))
        self.assertEqual({1, 5}, reduced_residue_system_primorial(2))
        self.assertEqual({1, 7, 11, 13, 17, 19, 23, 29},
                         reduced_residue_system_primorial(3))
        self.assertEqual(
            {
                1, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
                71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 121, 127, 131,
                137, 139, 143, 149, 151, 157, 163, 167, 169, 173, 179, 181, 187,
                191, 193, 197, 199, 209
            }, reduced_residue_system_primorial(4))

    def test_reduced_residue_system_primorial_sizes(self):
        sizes = {len(reduced_residue_system_primorial(i)) for i in range(1, 9)}
        # See https://oeis.org/A005867
        self.assertEqual({1, 2, 8, 48, 480, 5760, 92160, 1658880}, sizes)

    def test_reduced_residue_system_primorial_is_rrs(self):
        for i in range(1, 8):
            primorial_i = primorial(i)
            rrs = reduced_residue_system_primorial(i)
            for residue in rrs:
                # Each residue must be less than primorial_i
                self.assertLess(residue, primorial_i)
                # And relatively prime to primorial_i
                self.assertEqual(1, gcd(residue, primorial_i))

    def test_filter_twos(self):
        twos_1 = filter_twos(reduced_residue_system_primorial(1))
        self.assertEqual({1}, twos_1)
        twos_2 = filter_twos(reduced_residue_system_primorial(2))
        self.assertEqual({5}, twos_2)
        twos_3 = filter_twos(reduced_residue_system_primorial(3))
        self.assertEqual({11, 17, 29}, twos_3)
        twos_4 = filter_twos(reduced_residue_system_primorial(4))
        self.assertEqual(
            {
                11, 17, 29, 41, 59, 71, 101, 107, 137, 149, 167, 179, 191, 197,
                209
            }, twos_4)

    def test_filter_twos_sizes(self):
        sizes = []
        for i in range(1, 9):
            size = len(filter_twos(reduced_residue_system_primorial(i)))
            sizes.append(size)
        # See https://oeis.org/A059861
        self.assertEqual([1, 1, 3, 15, 135, 1485, 22275, 378675], sizes)

    def test_reduced_residue_system_primorial_twos(self):
        twos_1 = reduced_residue_system_primorial_twos(1)
        self.assertEqual({1}, twos_1)
        twos_2 = reduced_residue_system_primorial_twos(2)
        self.assertEqual({5}, twos_2)
        twos_3 = reduced_residue_system_primorial_twos(3)
        self.assertEqual({11, 17, 29}, twos_3)
        twos_4 = reduced_residue_system_primorial_twos(4)
        self.assertEqual(
            {
                11, 17, 29, 41, 59, 71, 101, 107, 137, 149, 167, 179, 191, 197,
                209
            }, twos_4)

    def test_test_reduced_residue_system_primorial_twos_sizes(self):
        sizes = []
        for i in range(1, 10):
            size = len(reduced_residue_system_primorial_twos(i))
            sizes.append(size)
        # See https://oeis.org/A059861
        self.assertEqual([1, 1, 3, 15, 135, 1485, 22275, 378675, 7952175],
                         sizes)

    def test_filter_twin_primes(self):
        twin_primes_1 = filter_twin_primes(
            reduced_residue_system_primorial_twos(1))
        self.assertEqual(set(), twin_primes_1)
        twin_primes_1 = filter_twin_primes(
            reduced_residue_system_primorial_twos(2))
        self.assertEqual({5}, twin_primes_1)
        twin_primes_1 = filter_twin_primes(
            reduced_residue_system_primorial_twos(3))
        self.assertEqual({11, 17, 29}, twin_primes_1)
        twin_primes_1 = filter_twin_primes(
            reduced_residue_system_primorial_twos(4))
        self.assertEqual(
            {11, 17, 29, 41, 59, 71, 101, 107, 137, 149, 179, 191, 197},
            twin_primes_1)

    def test_filter_twin_primes_sizes(self):
        sizes = []
        for i in range(1, 8):
            size = len(
                filter_twin_primes(reduced_residue_system_primorial_twos(i)))
            sizes.append(size)
        # Not an OEIS sequence yet but I'll submit it as one.
        self.assertEqual([0, 1, 3, 13, 67, 465, 4632], sizes)


if __name__ == '__main__':
    unittest.main()
