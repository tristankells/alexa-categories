import unittest
from Translator import Translator
import Categories


class TestDate(unittest.TestCase):
    def setUp(self):
        self.translator = Translator.Date.Conchita

    def test__skill_launches(self):
        session_variables = {}

        categories = Categories(session_variables)

        categories.launch()

        # Confirm player gets the correct message
        self.assertEqual(Translator.launch, categories.speech_text, '')


if __name__ == '__main__':
    unittest.main()