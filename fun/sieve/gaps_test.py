import unittest

from itertools import islice
from fun.sieve.gaps import apply_gaps, prime_gaps


class GapsTest(unittest.TestCase):

    def test_gaps(self):
        self.assertEqual((3, (2,)), prime_gaps(2))
        self.assertEqual((5, (2, 4)), prime_gaps(3))
        self.assertEqual((7, (4, 2, 4, 2, 4, 6, 2, 6)), prime_gaps(4))
        self.assertEqual(
            (11, (2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8, 4,
                  2, 4, 2, 4, 8, 6, 4, 6, 2, 4, 6, 2, 6, 6, 4, 2, 4, 6, 2, 6, 4,
                  2, 4, 2, 10, 2, 10)), prime_gaps(5))
        self.assertEqual(
            (13,
             (4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8, 4, 2, 4,
              2, 4, 14, 4, 6, 2, 10, 2, 6, 6, 4, 2, 4, 6, 2, 10, 2, 4, 2, 12,
              10, 2, 4, 2, 4, 6, 2, 6, 4, 6, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8, 4, 2,
              4, 6, 8, 6, 10, 2, 4, 6, 2, 6, 6, 4, 2, 4, 6, 2, 6, 4, 2, 6, 10,
              2, 10, 2, 4, 2, 4, 6, 8, 4, 2, 4, 12, 2, 6, 4, 2, 6, 4, 6, 12, 2,
              4, 2, 4, 8, 6, 4, 6, 2, 4, 6, 2, 6, 10, 2, 4, 6, 2, 6, 4, 2, 4, 2,
              10, 2, 10, 2, 4, 6, 6, 2, 6, 6, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8,
              4, 2, 6, 4, 8, 6, 4, 6, 2, 4, 6, 8, 6, 4, 2, 10, 2, 6, 4, 2, 4, 2,
              10, 2, 10, 2, 4, 2, 4, 8, 6, 4, 2, 4, 6, 6, 2, 6, 4, 8, 4, 6, 8,
              4, 2, 4, 2, 4, 8, 6, 4, 6, 6, 6, 2, 6, 6, 4, 2, 4, 6, 2, 6, 4, 2,
              4, 2, 10, 2, 10, 2, 6, 4, 6, 2, 6, 4, 2, 4, 6, 6, 8, 4, 2, 6, 10,
              8, 4, 2, 4, 2, 4, 8, 10, 6, 2, 4, 8, 6, 6, 4, 2, 4, 6, 2, 6, 4, 6,
              2, 10, 2, 10, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 6, 6, 4,
              6, 8, 4, 2, 4, 2, 4, 8, 6, 4, 8, 4, 6, 2, 6, 6, 4, 2, 4, 6, 8, 4,
              2, 4, 2, 10, 2, 10, 2, 4, 2, 4, 6, 2, 10, 2, 4, 6, 8, 6, 4, 2, 6,
              4, 6, 8, 4, 6, 2, 4, 8, 6, 4, 6, 2, 4, 6, 2, 6, 6, 4, 6, 6, 2, 6,
              6, 4, 2, 10, 2, 10, 2, 4, 2, 4, 6, 2, 6, 4, 2, 10, 6, 2, 6, 4, 2,
              6, 4, 6, 8, 4, 2, 4, 2, 12, 6, 4, 6, 2, 4, 6, 2, 12, 4, 2, 4, 8,
              6, 4, 2, 4, 2, 10, 2, 10, 6, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6,
              4, 2, 10, 6, 8, 6, 4, 2, 4, 8, 6, 4, 6, 2, 4, 6, 2, 6, 6, 6, 4, 6,
              2, 6, 4, 2, 4, 2, 10, 12, 2, 4, 2, 10, 2, 6, 4, 2, 4, 6, 6, 2, 10,
              2, 6, 4, 14, 4, 2, 4, 2, 4, 8, 6, 4, 6, 2, 4, 6, 2, 6, 6, 4, 2, 4,
              6, 2, 6, 4, 2, 4, 12, 2, 12)), prime_gaps(6))
        prime_7, gaps_7 = prime_gaps(7)
        self.assertEqual((prime_7, len(gaps_7)), (17, 5760))
        prime_8, gaps_8 = prime_gaps(8)
        self.assertEqual((prime_8, len(gaps_8)), (19, 92160))

    def test_apply_gaps(self):
        one_to_five = tuple(islice(apply_gaps(1, (1,)), 5))
        self.assertEqual((1, 2, 3, 4, 5), one_to_five)
        self.assertEqual((5, 7, 11, 13, 17, 19, 23, 25),
                         tuple(islice(apply_gaps(5, (2, 4)), 8)))

    def test_applied_prime_gaps_are_not_divisible_by_smaller_primes(self):
        prime_2, gaps_2 = prime_gaps(2)
        for i in islice(apply_gaps(prime_2, gaps_2), 20):
            self.assertTrue(i % 2 != 0)

        prime_3, gaps_3 = prime_gaps(3)
        for i in islice(apply_gaps(prime_3, gaps_3), 20):
            self.assertTrue(i % 2 != 0)
            self.assertTrue(i % 3 != 0)

        prime_4, gaps_4 = prime_gaps(4)
        for i in islice(apply_gaps(prime_4, gaps_4), len(gaps_4) * 100):
            self.assertTrue(i % 2 != 0)
            self.assertTrue(i % 3 != 0)
            self.assertTrue(i % 5 != 0)

        prime_5, gaps_5 = prime_gaps(5)
        for i in islice(apply_gaps(prime_5, gaps_5), len(gaps_5) * 100):
            self.assertTrue(i % 2 != 0)
            self.assertTrue(i % 3 != 0)
            self.assertTrue(i % 5 != 0)
            self.assertTrue(i % 7 != 0)

        prime_6, gaps_6 = prime_gaps(6)
        for i in islice(apply_gaps(prime_6, gaps_6), len(gaps_6) * 100):
            self.assertTrue(i % 2 != 0)
            self.assertTrue(i % 3 != 0)
            self.assertTrue(i % 5 != 0)

        prime_7, gaps_7 = prime_gaps(7)
        for i in islice(apply_gaps(prime_7, gaps_7), len(gaps_7) * 100):
            self.assertTrue(i % 2 != 0)
            self.assertTrue(i % 3 != 0)
            self.assertTrue(i % 5 != 0)
            self.assertTrue(i % 7 != 0)
            self.assertTrue(i % 11 != 0)


if __name__ == '__main__':
    unittest.main()
