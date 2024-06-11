from unittest import TestCase

import task


class Test(TestCase):
    def test_length_number(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        task.length_number(numbers)

        self.assertEqual(10, task.length_number(numbers))


class Test(TestCase):
    def test_sum_all_even_element(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        task.sum_all_even_element(numbers)

        self.assertEqual(30, task.sum_all_even_element(numbers))


class Test(TestCase):
    def test_sum_all_odd_position(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        task.sum_all_odd_position(numbers)

        self.assertEqual(25, task.sum_all_odd_position(numbers))


class Test(TestCase):
    def test_sum_two_numbers(self):
        numbers = 10
        numbers1 = 3
        task.sum_all_number(numbers, numbers1)
        self.assertEqual(13, task.sum_all_number(numbers, numbers1))


class Test(TestCase):
    def test_all_letters_contains_alphabet(self):
        letters = "the quick brown fox jumps over the lazy dog"
        task.all_alphabet(letters)
        self.assertTrue(letters, task.all_alphabet(letters))
