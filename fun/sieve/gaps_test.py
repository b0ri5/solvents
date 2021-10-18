import itertools
import unittest

import gaps


class GapsTest(unittest.TestCase):

    def test_gaps(self):
        self.assertEqual((3, (2,)), gaps.gaps(2))
        self.assertEqual((5, (2, 4)), gaps.gaps(3))
        self.assertEqual((7, (4, 2, 4, 2, 4, 6, 2, 6)), gaps.gaps(4))
        self.assertEqual(
            (11, (2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8, 4,
                  2, 4, 2, 4, 8, 6, 4, 6, 2, 4, 6, 2, 6, 6, 4, 2, 4, 6, 2, 6, 4,
                  2, 4, 2, 10, 2, 10)), gaps.gaps(5))
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
              6, 2, 6, 4, 2, 4, 12, 2, 12)), gaps.gaps(6))
        prime_7, gaps_7 = gaps.gaps(7)
        self.assertEqual((prime_7, len(gaps_7)), (17, 5760))
        prime_8, gaps_8 = gaps.gaps(8)
        self.assertEqual((prime_8, len(gaps_8)), (19, 92160))

    def test_apply_gaps(self):
        one_to_five = tuple(itertools.islice(gaps.apply_gaps(1, (1,)), 5))
        self.assertEqual((1, 2, 3, 4, 5), one_to_five)
        self.assertEqual((5, 7, 11, 13, 17, 19, 23, 25),
                         tuple(itertools.islice(gaps.apply_gaps(5, (2, 4)), 8)))

    def test_applied_gaps_are_not_divisible_by_smaller_primes(self):
        prime_2, gaps_2 = gaps.gaps(2)
        for i in itertools.islice(gaps.apply_gaps(prime_2, gaps_2), 20):
            self.assertTrue(i % 2 != 0)

        prime_3, gaps_3 = gaps.gaps(3)
        for i in itertools.islice(gaps.apply_gaps(prime_3, gaps_3), 20):
            self.assertTrue(i % 2 != 0)
            self.assertTrue(i % 3 != 0)

        prime_4, gaps_4 = gaps.gaps(4)
        for i in itertools.islice(gaps.apply_gaps(prime_4, gaps_4),
                                  len(gaps_4) * 100):
            self.assertTrue(i % 2 != 0)
            self.assertTrue(i % 3 != 0)
            self.assertTrue(i % 5 != 0)


if __name__ == '__main__':
    unittest.main()
