from unittest import TestCase

import another_task
from another_task import *


class function_Test(TestCase):
    def test_sum_collection(self):
        numbers = {2, 10, 15, 20, 23, 26}
        result = sum_collection(numbers)
        expected_sum = 96
        self.assertEqual(96, result)

    def test_remove_item(self):
        numbers = {2, 4, 6, 8, 15, 19, 10}
        element = 8
        self.assertEqual(8, remove_item(numbers, element))
