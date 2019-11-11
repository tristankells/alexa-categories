from category.category import Category
from category.category_enum import CategoryEnum
import translator
from category.player import Player
from category.category_data import get_category_things


class Categories:
    def __init__(self, session_variables):
        self.player = Player(session_variables['player']['is_playing'])

        category_enum = CategoryEnum(session_variables['category'])
        self.category = self.get_category(category_enum)

        self.previous_guesses = session_variables['previous_guesses']

        self.re_prompt = None
        self.speech_text = None

    def launch(self):
        """
        Called from LaunchRequestHandler
        :return:
        """
        self._begin_round()
        self.speech_text = translator.launch(self.category.name)

    def make_a_guess(self, guess):
        """
        Called from CountryIntentHandler
        :param guess: string containing a category guess
        :return: void
        """
        # Bad guess - not unique in for the round
        if guess in self.previous_guesses:
            self.speech_text = translator.bad_guess_not_unique(len(self.previous_guesses))
            self.player.is_playing = False
            self.previous_guesses = []
            return

        # Bad guess - not in the current category
        if not self.category.guess_in_category(guess):
            self.speech_text = translator.bad_guess_not_in_category(len(self.previous_guesses))
            self.player.is_playing = False
            self.previous_guesses = []
            return

        self._good_guess()
        self.previous_guesses.append(guess)

    def _bad_guess(self):
        self.speech_text = translator.bad_guess_not_in_category(len(self.previous_guesses))
        self.player.is_playing = False
        self.previous_guesses = []

    def _good_guess(self):
        self.speech_text = translator.good_guess

    def _begin_round(self):
        self.player.is_playing = True

    @staticmethod
    def get_category(category_enum) -> Category:
        things = get_category_things(category_enum)

        return Category(category_enum, things)

    @staticmethod
    def get_random_category() -> CategoryEnum:
        return CategoryEnum.COUNTRIES

    @staticmethod
    def get_initial_session_attributes() -> dict:
        """
        Gets the initial state of the game variables as
        """
        return {
            'player': {
                'is_playing': False
            },
            'category': CategoryEnum.COUNTRIES,
            'previous_guesses': []
        }

    def get_session_attributes(self) -> dict:
        """
        Gets the initial state of the game variables as
        """
        return {
            'player': {
                'is_playing': self.player.is_playing
            },
            'category': self.category.enum,
            'previous_guesses': self.previous_guesses
        }
