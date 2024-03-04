import string
from unittest import TestCase
import sample


class Test(TestCase):
    def test_sawp_number(self):
        letters = 'abc', 'xyz'
        self.assertEqual('xyc abz', sample.sawp_number('abc', 'xyz'))



