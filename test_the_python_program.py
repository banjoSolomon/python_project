import unittest
import main
import task


class TestFunctions(unittest.TestCase):
    def test_that_fuction_is_not_none(self):
        self.assertIsNotNone(task.list_sort)

        my_number = [10, 2, 8, 9, 3, 4, 1, 5]
        sample_output = [10]
        self.assertEqual(task.ascending_function(my_number.sample_output))


