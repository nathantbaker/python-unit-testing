import unittest
from superman import *

class TestSuperman(unittest.TestCase):

    def test_SupermanIsBulletproof(self):

        superman = Superman()
        self.assertTrue(superman.is_bulletproof)

    def test_SupermanIsASuperhero(self):

        superman = Superman()
        self.assertIsInstance(superman, Superhero)

    def test_SupermanIsAFlyingSuperhero(self):

        superman = Superman()
        self.assertIsInstance(superman, Flight)

    def test_SupermanIsSwimmingFast(self):

        superman = Superman()
        self.assertEqual(superman.water_speed, 250)

    def test_SupermanIsFlyingFast(self):

        superman = Superman()
        self.assertEqual(superman.air_speed, 1000000)

if __name__ == '__main__':
    unittest.main()