import unittest
from superhero import *

class TestSuperhero(unittest.TestCase):

    def test_SuperheroMustHaveNameProperty(self):

        random_superhero = Superhero("bilbo")
        self.assertEqual(random_superhero.name, "bilbo")

    def test_SuperheroAddPowerMustIncludePower(self):

        random_superhero = Superhero("Clark")
        random_superhero.add_power("invisible")
        self.assertIn("invisible", random_superhero.powers)

if __name__ == '__main__':
    unittest.main()
