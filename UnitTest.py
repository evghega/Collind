import unittest
import excelfunc
import cardandcube
import Main


class TestMethods(unittest.TestCase):

    def test_click_back(self):
        self.assertEqual(Main.ClickBack1(), 1, "not one , check the return")

    def test_excel_func(self):
        self.assertTrue(excelfunc.checkAnswer(1, 2, "B"), "Not True, check Cube")
        self.assertFalse(excelfunc.checkAnswer(3, 2, "C"), "Not False, check Cube or answer")
        self.assertEqual(excelfunc.CreateGameID(3), 52,
                         "check if number is updated to the next one, need to update the last argument number!!")
        self.assertIsNone(excelfunc.Card_enable(1), "none if function worked")
        self.assertTrue(excelfunc.answertoDB(True,30),"No Such Game,or Faild to access SQL")

    def test_action_list(self):
        self.assertEqual(excelfunc.checkDetails("admin", "klom"), (False, "badpassword"), "not Eqoual, check the function")
        self.assertFalse(excelfunc.addUser('admin', 'admin', 'team7', 'team7', 'team7@gmail.com', '543149811', 'admin'),
                         "Check if thade user exists twice!")
        self.assertFalse(excelfunc.deleteUser(40), "Wrong deletion, check the function")
        self.assertTrue(excelfunc.resetUser(2), "Wrong reset, check the function or number")
        self.assertEqual(excelfunc.gamesOfUser("tester"), [22,23,24,41,42,44,53,54],
                         "Exctart was wrong check SQL ALSO")

    def test_cardandcubefunc(self):
        self.assertTrue(cardandcube.cardenablef(3), "Card is Disable")
        self.assertFalse(cardandcube.cardenablef(8), "Card is Enable")


if __name__ == '__main__':
    unittest.main()
