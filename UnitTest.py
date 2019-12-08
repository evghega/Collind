import unittest
import check


class TestStringMethods(unittest.TestCase):

    def test_excel_func(self):
        self.assertTrue(check.checkAnswer(2,2,"A"),"Not True, check Cube")
        self.assertFalse(check.checkAnswer(2, 2, "A"), "Not False, check Cube or answer")


if __name__ == '__main__':
    unittest.main()


