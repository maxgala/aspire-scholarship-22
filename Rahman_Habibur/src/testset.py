import unittest
from main import *
from rooster import *
from coffee_chat import *
from person import *


class TestStringMethods(unittest.TestCase):

    def test_new_rooster(self):
        rooster = new_rooster([], [])
        self.assertEqual(rooster.get_past(), [])
        self.assertEqual(rooster.get_upcoming(), [])

    def test_new_aspiring_professional(self):
        test = new_aspiring_professional("John", "Smith", "IT", "Python")
        self.assertEqual(test.get_first_name(), "John")
        self.assertEqual(test.get_last_name(), "Smith")
        self.assertEqual(test.get_industry(), "IT")
        self.assertEqual(test.get_interests(), "Python")

    def test_new_senior_executive(self):
        test = new_senior_executive("John", "Smith", "IT", "Weekly")
        self.assertEqual(test.get_first_name(), "John")
        self.assertEqual(test.get_last_name(), "Smith")
        self.assertEqual(test.get_industry(), "IT")
        self.assertEqual(test.get_frequency(), "Weekly")

    def test_new_rooster(self):
        rooster = new_rooster([], [])
        self.assertEqual(rooster.get_past(), [])
        self.assertEqual(rooster.get_upcoming(), [])

    def test_load_data(self):
        self.assertEqual(load_data("data/dummy.json"), [])
        self.assertEqual(load_data("data/dummy.json"), [])
        self.assertEqual(load_data("data/dummy.json"), [])

    def test_new_coffee_chat(self):
        test = new_coffee_chat("Test", "01/01/2020", "12:00", "Test", new_aspiring_professional(
            "John", "Smith", "IT", "Python"), new_senior_executive("John", "Smith", "IT", "Weekly"))
        self.assertEqual(test.get_name(), "Test")
        self.assertEqual(test.get_date(), "01/01/2020")
        self.assertEqual(test.get_time(), "12:00")
        self.assertEqual(test.get_location(), "Test")
        self.assertEqual(
            test.get_aspiring_professional().get_first_name(), "John")
        self.assertEqual(test.get_senior_executive().get_first_name(), "John")


if __name__ == '__main__':
    unittest.main()
