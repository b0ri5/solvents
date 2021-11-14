import unittest

from math import gcd
from reduced_residue_system import (
    _reduced_residue_system_primorial_brute_force, children,
    composite_and_composite_between_prime_and_primorial,
    composite_and_prime_between_prime_and_primorial, filter_twin_primes,
    filter_twos, full_prime_residues, min_child, min_extension,
    min_prime_descendant, prime_and_composite_between_prime_and_primorial,
    prime_residues, prime_residues_inverse, primoradic,
    primorial_multiplicative_inverse, reduced_residue_system_primorial,
    reduced_residue_system_primorial_two_classification,
    reduced_residue_system_primorial_twos,
    reduced_residue_system_primorial_applied_gaps,
    reduced_residue_system_primorial_gaps,
    twin_primes_between_prime_and_primorial, TwoClassification)
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
        self.assertEqual([1], sorted(reduced_residue_system_primorial(1)))
        self.assertEqual([1, 5], sorted(reduced_residue_system_primorial(2)))
        self.assertEqual([1, 7, 11, 13, 17, 19, 23, 29],
                         sorted(reduced_residue_system_primorial(3)))
        self.assertEqual([
            1, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
            73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 121, 127, 131, 137,
            139, 143, 149, 151, 157, 163, 167, 169, 173, 179, 181, 187, 191,
            193, 197, 199, 209
        ], sorted(reduced_residue_system_primorial(4)))

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
        # Not an OEIS sequence and it shouldn't be one since the first term is
        # a bit misleading in that the applied gap is {3}.
        self.assertEqual([0, 1, 3, 13, 67, 465, 4632], sizes)

    def test_twin_primes_between_prime_and_primorial(self):
        sizes = []
        for i in range(1, 8):
            size = len(twin_primes_between_prime_and_primorial(i))
            sizes.append(size)
        # Not an OEIS sequence yet but I'll submit it as one.
        self.assertEqual([1, 1, 3, 13, 67, 465, 4632], sizes)

    def test_prime_and_composite_between_prime_and_primorial(self):
        sizes = []
        for i in range(1, 7):
            size = len(prime_and_composite_between_prime_and_primorial(i))
            sizes.append(size)
        # Not an OEIS sequence yet but I'll submit it as one.
        self.assertEqual([0, 0, 0, 1, 28, 383], sizes)

    def test_composite_and_prime_between_prime_and_primorial(self):
        sizes = []
        for i in range(1, 7):
            size = len(composite_and_prime_between_prime_and_primorial(i))
            sizes.append(size)
        # Not an OEIS sequence yet but I'll submit it as one.
        self.assertEqual([0, 0, 0, 1, 28, 358], sizes)

    def test_composite_and_composite_between_prime_and_primorial(self):
        sizes = []
        for i in range(1, 7):
            size = len(composite_and_composite_between_prime_and_primorial(i))
            sizes.append(size)
        # Not an OEIS sequence yet but I'll submit it as one.
        self.assertEqual([0, 0, 0, 0, 12, 279], sizes)

    def test_sum_of_classification_of_two_between_prime_and_primorial(self):
        sizes = []
        for i in range(1, 7):
            size = (
                len(composite_and_composite_between_prime_and_primorial(i)) +
                len(composite_and_prime_between_prime_and_primorial(i)) +
                len(prime_and_composite_between_prime_and_primorial(i)) +
                len(twin_primes_between_prime_and_primorial(i)))
            sizes.append(size)

        # See https://oeis.org/A059861
        self.assertEqual([1, 1, 3, 15, 135, 1485], sizes)

    def test_children(self):
        self.assertEqual([1, 5], list(children(1, 1)))
        self.assertEqual([1, 7, 13, 19], list(children(1, 2)))
        self.assertEqual([11, 17, 23, 29], list(children(5, 2)))
        self.assertEqual([1, 31, 61, 121, 151, 181], list(children(1, 3)))
        self.assertEqual([37, 67, 97, 127, 157, 187], list(children(7, 3)))
        self.assertEqual([11, 41, 71, 101, 131, 191], list(children(11, 3)))

    def test_min_child(self):
        self.assertEqual(1, min_child(1, 1))
        self.assertEqual(11, min_child(5, 2))
        self.assertEqual(37, min_child(7, 3))
        self.assertEqual(11, min_child(11, 3))
        self.assertEqual(331, min_child(121, 4))
        self.assertEqual(169, min_child(169, 4))
        self.assertEqual(2479, min_child(169, 5))

    def test_min_extension(self):
        # Primes are already considered fully extended
        self.assertEqual((1, 1), min_extension(1, 1))
        self.assertEqual((5, 2), min_extension(5, 2))

        # 121 = 11 * 11 and 7 is the 4th prime and 11 is the 5th.
        # So 121 is not in rrs(5) and so its smallest child is
        # 121 + primorial(4) = 121 + (2 * 3 * 5 * 7) = 121 + 210 = 331.
        self.assertEqual((331, 5), min_extension(121, 4))

        # 169 = 13 * 13 and 13 is the 6th prime so 169 is not in rrs(6).
        # Then its smallest child is 169 + primorial(5) = 169 + 2310 = 2479.
        # Then 2479 = 37 * 67 and 37 is the 12th prime so the min child of 2479
        # in rrs(11) is 2479 + primorial(11) = 200560492609 = 89 * 20479 * 110039.
        # 89 is the 24th prime so the child of 200560492609 in rrs(23) is
        # 200560492609 + primorial(23) = 267064515689275851355824578485399
        self.assertEqual(
            (169 + primorial(5) + primorial(11) + primorial(23), 24),
            min_extension(169, 4))
        self.assertEqual((267064515689275851355824578485399, 24),
                         min_extension(169, 4))

        # The composite elements of rrs(4) are {121, 143, 169, 187, 209}.
        self.assertEqual((353, 5), min_extension(143, 4))
        self.assertEqual((397, 5), min_extension(187, 4))
        self.assertEqual((419, 5), min_extension(209, 4))

    def test_min_prime_descendant(self):
        self.assertEqual((331, 5), min_prime_descendant(121, 4))
        self.assertEqual((353, 5), min_prime_descendant(143, 4))
        self.assertEqual((379, 5), min_prime_descendant(169, 4))
        self.assertEqual((397, 5), min_prime_descendant(187, 4))
        self.assertEqual((419, 5), min_prime_descendant(209, 4))

        # These require going more than one level deep and are so cool.
        self.assertEqual((19525829, 9), min_prime_descendant(126449, 7))
        self.assertEqual((9913361, 9), min_prime_descendant(213671, 7))
        self.assertEqual((10120951, 9), min_prime_descendant(421261, 7))
        self.assertEqual((892971133, 10), min_prime_descendant(599653, 8))
        self.assertEqual((1116141781, 10), min_prime_descendant(677431, 8))
        self.assertEqual((1339256201, 10), min_prime_descendant(698981, 8))
        self.assertEqual((223877011, 10), min_prime_descendant(784141, 8))
        self.assertEqual((456749701, 10), min_prime_descendant(864271, 8))
        self.assertEqual((447287131, 10), min_prime_descendant(1101391, 8))
        self.assertEqual((224434261, 10), min_prime_descendant(1341391, 8))

    def test_children_residues(self):
        self.assertEqual((1,), prime_residues(1, 1))
        self.assertEqual([(1, 1), (1, 2)],
                         [prime_residues(c, 2) for c in children(1, 1)])

        self.assertEqual((1, 1), prime_residues(1, 2))
        self.assertEqual({(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4)},
                         {prime_residues(c, 3) for c in children(1, 2)})

        self.assertEqual((1, 2), prime_residues(5, 2))
        self.assertEqual({(1, 2, 1), (1, 2, 2), (1, 2, 3), (1, 2, 4)},
                         {prime_residues(c, 3) for c in children(5, 2)})

        self.assertEqual((1, 1, 1), prime_residues(1, 3))
        self.assertEqual(
            {(1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 1, 3), (1, 1, 1, 4),
             (1, 1, 1, 5), (1, 1, 1, 6)},
            {prime_residues(c, 4) for c in children(1, 3)})

        self.assertEqual((1, 1, 2), prime_residues(7, 3))
        self.assertEqual(
            {(1, 1, 2, 1), (1, 1, 2, 2), (1, 1, 2, 3), (1, 1, 2, 4),
             (1, 1, 2, 5), (1, 1, 2, 6)},
            {prime_residues(c, 4) for c in children(7, 3)})

        self.assertEqual((1, 2, 1), prime_residues(11, 3))
        self.assertEqual(
            {(1, 2, 1, 1), (1, 2, 1, 2), (1, 2, 1, 3), (1, 2, 1, 4),
             (1, 2, 1, 5), (1, 2, 1, 6)},
            {prime_residues(c, 4) for c in children(11, 3)})

    def test_reduced_residue_system_primorial_gaps(self):
        self.assertEqual([2], reduced_residue_system_primorial_gaps(1))
        self.assertEqual([4, 2], reduced_residue_system_primorial_gaps(2))
        self.assertEqual([6, 4, 2, 4, 2, 4, 6, 2],
                         reduced_residue_system_primorial_gaps(3))
        self.assertEqual([
            10, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8, 4,
            2, 4, 2, 4, 8, 6, 4, 6, 2, 4, 6, 2, 6, 6, 4, 2, 4, 6, 2, 6, 4, 2, 4,
            2, 10, 2
        ], reduced_residue_system_primorial_gaps(4))

    def test_reduced_residue_system_primorial_applied_gaps(self):
        self.assertEqual([3], reduced_residue_system_primorial_applied_gaps(1))
        self.assertEqual([5, 7],
                         reduced_residue_system_primorial_applied_gaps(2))
        self.assertEqual([7, 11, 13, 17, 19, 23, 29, 31],
                         reduced_residue_system_primorial_applied_gaps(3))
        self.assertEqual([
            11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
            79, 83, 89, 97, 101, 103, 107, 109, 113, 121, 127, 131, 137, 139,
            143, 149, 151, 157, 163, 167, 169, 173, 179, 181, 187, 191, 193,
            197, 199, 209, 211
        ], reduced_residue_system_primorial_applied_gaps(4))

    def test_reduced_residue_system_primorial_two_classification(self):
        two_classification1 = reduced_residue_system_primorial_two_classification(
            1)
        self.assertEqual(
            two_classification1,
            TwoClassification(composite_to_composite=0,
                              composite_to_prime=0,
                              prime_to_composite=0,
                              prime_to_prime=1))
        self.assertEqual(1, sum(two_classification1))

        two_classification2 = reduced_residue_system_primorial_two_classification(
            2)
        self.assertEqual(
            two_classification2,
            TwoClassification(composite_to_composite=0,
                              composite_to_prime=0,
                              prime_to_composite=0,
                              prime_to_prime=1))
        self.assertEqual(1, sum(two_classification2))

        two_classification3 = reduced_residue_system_primorial_two_classification(
            3)
        self.assertEqual(
            two_classification3,
            TwoClassification(composite_to_composite=0,
                              composite_to_prime=0,
                              prime_to_composite=0,
                              prime_to_prime=3))
        self.assertEqual(3, sum(two_classification3))

        two_classification4 = reduced_residue_system_primorial_two_classification(
            4)
        self.assertEqual(
            two_classification4,
            TwoClassification(composite_to_composite=0,
                              composite_to_prime=1,
                              prime_to_composite=1,
                              prime_to_prime=13))
        self.assertEqual(15, sum(two_classification4))

        two_classification5 = reduced_residue_system_primorial_two_classification(
            5)
        self.assertEqual(
            two_classification5,
            TwoClassification(composite_to_composite=12,
                              composite_to_prime=28,
                              prime_to_composite=28,
                              prime_to_prime=67))
        self.assertEqual(135, sum(two_classification5))

        two_classification6 = reduced_residue_system_primorial_two_classification(
            6)
        self.assertEqual(
            two_classification6,
            TwoClassification(composite_to_composite=279,
                              composite_to_prime=358,
                              prime_to_composite=383,
                              prime_to_prime=465))
        self.assertEqual(1485, sum(two_classification6))

    def test_prime_residues(self):
        self.assertEqual((1,), prime_residues(1, 1))
        self.assertEqual((1, 1), prime_residues(1, 2))
        self.assertEqual((1, 1, 1), prime_residues(1, 3))

        self.assertEqual((0,), prime_residues(2, 1))
        self.assertEqual((0, 2), prime_residues(2, 2))
        self.assertEqual((0, 2, 2), prime_residues(2, 3))

    def test_prime_residues_inverse(self):
        self.assertEqual(29, prime_residues_inverse((1, 2, 4)))
        self.assertEqual(157, prime_residues_inverse((1, 1, 2, 3)))

    def test_full_prime_residues(self):
        self.assertEqual((), full_prime_residues(1))
        self.assertEqual((0,), full_prime_residues(2))
        self.assertEqual((1, 0), full_prime_residues(3))
        self.assertEqual((0, 1), full_prime_residues(4))
        self.assertEqual((1, 2, 0), full_prime_residues(5))
        self.assertEqual((0, 0, 1), full_prime_residues(6))
        self.assertEqual((1, 1, 2, 0), full_prime_residues(7))
        self.assertEqual((0, 2, 3, 1), full_prime_residues(8))
        self.assertEqual((1, 0, 4, 2), full_prime_residues(9))
        self.assertEqual((0, 1, 0, 3), full_prime_residues(10))

    def test_primoradic(self):
        # Start with http://oeis.org/A049345
        self.assertEqual((0,), primoradic(0))
        self.assertEqual((1,), primoradic(1))
        self.assertEqual((0, 1), primoradic(2))
        self.assertEqual((1, 1), primoradic(3))
        self.assertEqual((0, 2), primoradic(4))
        self.assertEqual((1, 2), primoradic(5))
        self.assertEqual((0, 0, 1), primoradic(6))
        self.assertEqual((1, 0, 1), primoradic(7))

        # And some larger interesting numbers
        self.assertEqual((1, 2, 4, 0, 8, 2, 4), primoradic(126449))
        self.assertEqual((1, 2, 4, 0, 8, 2, 4, 0, 2), primoradic(19525829))

    def test_primorial_multiplicative_inverse(self):
        # https://oeis.org/A079276
        self.assertEqual(2, primorial_multiplicative_inverse(1))
        self.assertEqual(1, primorial_multiplicative_inverse(2))
        self.assertEqual(4, primorial_multiplicative_inverse(3))
        self.assertEqual(1, primorial_multiplicative_inverse(4))
        self.assertEqual(3, primorial_multiplicative_inverse(5))
        self.assertEqual(15, primorial_multiplicative_inverse(6))
        self.assertEqual(18, primorial_multiplicative_inverse(7))


if __name__ == '__main__':
    unittest.main()
