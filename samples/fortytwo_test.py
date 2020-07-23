import fortytwo
import unittest

class FortytwoTest(unittest.TestCase):
  def test_fortytwo(self):
    self.assertEqual(42, fortytwo.fortytwo())
