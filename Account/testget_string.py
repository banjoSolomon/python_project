from unittest import TestCase

import define


class Test(TestCase):
    def test_my_code(self):
        getString = define.Define()
        getString.getString("hello")
        self.assertEqual("HELLO", getString.printString())
