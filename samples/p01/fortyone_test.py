from . import fortyone
import unittest

class FortyoneTest(unittest.TestCase):
  def test_fortyone(self):
    self.assertEqual(41, fortyone.fortyone())
