import unittest

from samples import fortytwo


class FortytwoTest(unittest.TestCase):

    def test_fortytwo(self):
        self.assertEqual(42, fortytwo.fortytwo())


if __name__ == '__main__':
    unittest.main()
