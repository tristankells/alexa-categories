import unittest
from categories.Translator import Translator
from categories.Categories import Categories


class TestDate(unittest.TestCase):

    def test__skill_launches(self):
        session_variables = Categories.get_initial_dict()

        categories = Categories(session_variables)

        categories.launch()

        # Confirm player gets the correct message
        self.assertEqual(Translator.launch.format('Country'), categories.speech_text, '')


if __name__ == '__main__':
    unittest.main()