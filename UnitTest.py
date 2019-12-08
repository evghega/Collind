import unittest
import MathOperations


class TestStringMethods(unittest.TestCase):

    def test_multiply_function(self):
        self.assertEqual(0, MathOperations.multiply(10, 0), "Not equal!")
        self.assertEqual(0, MathOperations.multiply(0, 10), "Not equal!")
        self.assertEqual(6, MathOperations.multiply(2, 3), "Not equal!")




if __name__ == '__main__':
    unittest.main()


