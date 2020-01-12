import unittest
import excelfunc


class TestStringMethods(unittest.TestCase):

    def test_excel_func(self):
        self.assertTrue(excelfunc.checkAnswer(2, 2, "B"), "Not True, check Cube")
        self.assertFalse(excelfunc.checkAnswer(3, 2, "C"), "Not False, check Cube or answer")
        self.assertEqual(excelfunc.CreateGameID(), 19, "check if number is updated to the next one, need to update the last argument number!!")
        self.assertIsNone(excelfunc.Card_enable(1),"none if function worked")
        self.assertEqual(excelfunc.login("admin","klom"),(False,"badpassword"),"not Eqoual, check the function")
        self.assertFalse(excelfunc.addUser('admin', 'admin', 'team7', 'team7', 'team7@gmail.com', '543149811', 'admin'),"Check if the user exists twice!")
        self.assertFalse(excelfunc.deleteUser(40),"Wrong deletion, check the function")



if __name__ == '__main__':
    unittest.main()


