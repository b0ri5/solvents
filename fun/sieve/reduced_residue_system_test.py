import unittest

from math import gcd
from reduced_residue_system import (
    _reduced_residue_system_primorial_brute_force,
    reduced_residue_system_primorial)
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
                1, 131, 137, 11, 139, 13, 143, 17, 19, 149, 23, 151, 29, 157,
                31, 163, 37, 167, 41, 169, 43, 173, 47, 179, 53, 181, 59, 187,
                61, 191, 193, 67, 197, 71, 199, 73, 79, 209, 83, 89, 97, 101,
                103, 107, 109, 113, 121, 127
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
                1, 131, 137, 11, 139, 13, 143, 17, 19, 149, 23, 151, 29, 157,
                31, 163, 37, 167, 41, 169, 43, 173, 47, 179, 53, 181, 59, 187,
                61, 191, 193, 67, 197, 71, 199, 73, 79, 209, 83, 89, 97, 101,
                103, 107, 109, 113, 121, 127
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


if __name__ == '__main__':
    unittest.main()
