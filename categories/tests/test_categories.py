import unittest
import Translator
from Categories import Categories


class CategoriesTests(unittest.TestCase):

    def test__skill_launches(self):
        session_variables = Categories.get_initial_session_attributes()

        categories = Categories(session_variables)

        categories.launch()

        # Confirm player gets the correct message
        self.assertEqual(Translator.launch('Countries'), categories.speech_text, '')

    def test__make_a_guess__good_guess(self):
        session_variables = Categories.get_initial_session_attributes()
        session_variables['player']['is_playing'] = True

        categories = Categories(session_variables)

        categories.make_a_guess('afghanistan')

        # round continues
        self.assertEqual(True, categories.player.is_playing, 'Player should be still playing')
        # correct message plays
        self.assertEqual(Translator.good_guess, categories.speech_text, 'Should get a good guess speech response')
        #

    def test__make_a_guess__not_in_category(self):
        session_variables = Categories.get_initial_session_attributes()
        session_variables['player']['is_playing'] = True

        categories = Categories(session_variables)

        categories.make_a_guess('america')

        # round ends
        self.assertEqual(categories.player.is_playing, False, 'Player should no longer be playing')
        # correct error message plays
        self.assertEqual(Translator.bad_guess_not_in_category(0), categories.speech_text, 'Should get a bad guess '
                                                                                          'speech response')

    def test__make_a_guess__not_unique(self):
        session_variables = Categories.get_initial_session_attributes()
        session_variables['player']['is_playing'] = True
        session_variables['previous_guesses'] = ['afghanistan']

        categories = Categories(session_variables)

        categories.make_a_guess('afghanistan')

        # round ends
        self.assertFalse(categories.player.is_playing, 'Player should no longer be playing')
        # correct error message plays
        self.assertEqual(Translator.bad_guess_not_unique(1), categories.speech_text, 'Should get a bad guess '
                                                                                     'speech response')


if __name__ == '__main__':
    unittest.main()
