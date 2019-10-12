import unittest
from Translator import Translator
from Categories import Categories


class IntegrationTests(unittest.TestCase):
    def test__round_of_countries(self):
        session_variables = Categories.get_initial_dict()

        categories = Categories(session_variables)

        categories.launch()

        # Confirm player gets the correct message
        self.assertEqual(Translator.launch.format('Country'), categories.speech_text, '')
        self.assertEqual(True, categories.player.is_playing, '')

        guess = "afghanistan"

        categories.make_a_guess(guess)

        # Confirm player gets the correct message
        self.assertEqual(Translator.good_guess, categories.speech_text, '')
        self.assertEqual(True, categories.player.is_playing, '')

        guess = "new zealand"

        categories.make_a_guess(guess)

        # Confirm player gets the correct message
        self.assertEqual(Translator.good_guess, categories.speech_text, '')
        self.assertEqual(True, categories.player.is_playing, '')

        guess = "europe"

        categories.make_a_guess(guess)

        # Confirm player gets the correct message
        self.assertEqual(Translator.bad_guess, categories.speech_text, '')
        self.assertEqual(False, categories.player.is_playing, '')


if __name__ == '__main__':
    unittest.main()
