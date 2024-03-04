from unittest import TestCase

import refection


class Test(TestCase):
    def test_number_upper_lower(self):
        letter = "ayomide ORE"
        expected = "check_lower 7 check_upper 3"
        self.assertEqual(expected, refection.number_upper_lower(letter))


class CheckTest(TestCase):
    def test_number_of_letter_number_of_lower(self):
        letter = "Hello 122"
        expected = "number_of_digit 3 number_of_letters 5"
        self.assertEqual(expected, refection.number_of_letter_number_of_lower(letter))
