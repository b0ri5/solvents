import unittest

import fortytwo


class FortytwoTest(unittest.TestCase):

    def test_fortytwo(self):
        self.assertEqual(42, fortytwo.fortytwo())
