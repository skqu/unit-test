import unittest

# The function you want to test
def add(a, b):
    return a + b

# Create a test case class that inherits from unittest.TestCase
class TestAddition(unittest.TestCase):

    # Define test methods by starting their names with "test_"
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(1, -3), -2)

# Run the tests if the script is executed
if __name__ == '__main__':
    unittest.main()
