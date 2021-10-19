import unittest

from reduced_residue_system import _reduced_residue_system_primorial_brute_force


class TestBruteForce(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
