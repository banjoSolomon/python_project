import unittest
import main

class TestAcendingFunction(unittest.TestCase):
    def test_that_fuction_is_not_none(self):

        self.assertIsNotNone(main.list_sort)

        def test_that_function_sort_array_in_ascending_order(self):
            sample_list = [10,2,8,9,3,4,1,5]
            sample_output = [1,2,3,4,5,8,9,10]
            self.assertEqual(main.ascending_function(sample_list.sample_output))