import unittest
import excelfunc


class TestStringMethods(unittest.TestCase):

    def test_excel_func(self):
        self.assertTrue(excelfunc.checkAnswer(2, 2, "B"), "Not True, check Cube")
        self.assertFalse(excelfunc.checkAnswer(2, 2, "A"), "Not False, check Cube or answer")
        self.assertEqual(excelfunc.CreateGameID(), 19, "check if number is updated to the next one, need to update the last argument number!!")

if __name__ == '__main__':
    unittest.main()


