import unittest
from Translator import Translator
from Categories import Categories


class CategoriesTests(unittest.TestCase):

    def test__skill_launches(self):
        session_variables = Categories.get_initial_dict()

        categories = Categories(session_variables)

        categories.launch()

        # Confirm player gets the correct message
        self.assertEqual(Translator.launch.format('Country'), categories.speech_text, '')

    def test__make_a_guess__good_guess__works_correctly(self):
        session_variables = Categories.get_initial_dict()
        session_variables['player']['is_playing'] = True

        categories = Categories(session_variables)

        categories.make_a_guess('afghanistan')

        # round continues
        self.assertEqual(True, categories.player.is_playing, 'Player should be still playing')
        # correct message plays
        self.assertEqual(Translator.good_guess, categories.speech_text, 'Should get a good guess speech response')
        #

    def test__make_a_guess__bad_guess__works_correctly(self):
        session_variables = Categories.get_initial_dict()
        session_variables['player']['is_playing'] = True

        categories = Categories(session_variables)

        categories.make_a_guess('america')

        # round ends
        self.assertEqual(categories.player.is_playing, False, 'Player should no longer be playing')
        # correct error message plays
        self.assertEqual(categories.speech_text, Translator.bad_guess, 'Should get a bad guess speech response')



if __name__ == '__main__':
    unittest.main()
