## Unit test file

import unittest
from MonteCarloModules import *

class die_test(unittest.TestCase):
    '''Unit Test to test the die class'''
    def test_change_weight(self):
        '''Test if the change_weight function works'''
        die_object = Die(["A", "B", "C"])
        die_object.change_weight("A", 2)
        df = die_object.print_df()["weights"]
        df = list(df)
        testValue = [2,1,1]

        message = "Weight Not Changed"

        self.assertEqual(testValue, df, message)


    def test_rolls(self):
        '''test if the rolls function works'''
        die_object = Die(["A", "B", "C"])
        roll_object = die_object.rolls(10)
        testValue = len(roll_object)

        message = "Rolls doesn't work"

        self.assertEqual(testValue, 10, message)

    def test_print_df(self):
        '''test if the print_df function works'''
        die_object = Die(["A", "B", "C"])
        df = die_object.print_df()
        if (type(df) == pd.DataFrame):
            testValue = True
        else:
            testValue == False

        message = "print_df doesn't work"
        self.assertTrue(testValue, message)
    

class game_test(unittest.TestCase):
    '''Unit test to test game class'''
    def test_return_faces(self):
        '''tests if return_faces returns the correct faces'''
        die_object = Die(["a", "b"])
        game_object = Game([die_object])
        testValue = (list(game_object.return_faces()) == ["a", "b"])
        
        message = "return_faces does not return the correct faces"
        self.assertTrue(testValue, message)

    def test_play(self):
        '''test if play returns the correct outcomes'''
        die_object = Die(["a", "b"])
        game_object = Game([die_object])
        game_object.play(5)
        testValue = (game_object.show().shape == (1,5))

        message = "play does not return the correct values"
        self.assertTrue(testValue, message)

    def test_show(self):
        '''test if show returns the correct dataframe'''
        die_object = Die(["a", "b"])
        game_object = Game([die_object])
        game_object.play(5)
        test1 = (game_object.show().shape == (1,5))
        test2 = (type(game_object.show()) == pd.DataFrame)
        testValue = test1 + test2

        message = "show does not return the correct data frame"
        self.assertEqual(testValue, 2, message)


class analyzer_test(unittest.TestCase):
    '''this class tests the analyzer class'''
    def test_jackpot(self):
        '''this tests the jackpot method to see if it returns the correct values'''
        die_object = Die(["a","a"])
        game_object = Game([die_object, die_object])
        game_object.play(3)
        x = analyzer(game_object).jackpot()
        testValue = (x == 3)

        message = "the jackpot method failed to return the correct result"
        self.assertTrue(testValue, message)
        
    def test_combo(self):
        '''this tests the combo method to make sure it returns the correct output'''
        die_object = Die(["a","a"])
        game_object = Game([die_object, die_object])
        game_object.play(2)
        combo = analyzer(game_object).combo()
        # x = (combo[0] == 2)
        y = (type(analyzer(game_object).combo()) == pd.DataFrame)
        # z = x + y

        message = "the combo method failed to return the correct values"
        self.assertEqual(y, 1, message)
    

    def test_face_counts_per_roll(self):
        '''This tests the face counts per roll method to make sure it returns the correct output'''
        die_object = Die(["a","a"])
        game_object = Game([die_object, die_object])
        game_object.play(2)
        x = analyzer(game_object).face_counts_per_roll()
        testValue = (type(x) == pd.DataFrame)

        message = "the face count per roll method failed to return the correct output"
        self.assertTrue(testValue, message)

        
if __name__ == '__main__':
	unittest.main(verbosity=3)