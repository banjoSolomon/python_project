from unittest import TestCase
from gun import *


class TestGun(TestCase):
    def test_load_bullets(self):
        my_gun = Gun(caliber='9mm', capacity=17)
        bullets_load = 10
        my_gun.load_bullets(bullets_load)
        result = my_gun.bullets_loaded
        expected = 10
        self.assertEqual(expected, result)


class TestGun(TestCase):
    def test_shoot(self):
        my_gun = Gun(caliber='9mm', capacity=17)
        for _ in range(3):
            my_gun.shoot()
        result = my_gun.bullets_loaded
        expected = 14
        self.assertEqual(expected,result)
