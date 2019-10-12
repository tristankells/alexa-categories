from Category import Category
from CategoryEnum import CategoryEnum
from Translator import Translator
from Player import Player
from CategoryData import get_category_things


class Categories:
    def __init__(self, session_variables):
        self.player = Player(session_variables['player']['is_playing'])
        self.category = self.get_category()

        self.speech_text = None
        self.re_prompt = None

    def launch(self):
        """
        Called from LaunchRequestHandler
        :return:
        """
        self.begin_round()
        self.speech_text = Translator.launch.format(self.category.name)

    def make_a_guess(self, guess):
        """
        Called from CountryIntentHandler
        :param guess: string containing a category guess
        :return: void
        """
        if self.category.is_guess_in_category(guess):
            self.good_guess()
        else:
            self.bad_guess()

    def bad_guess(self):
        self.player.is_playing = False
        self.speech_text = Translator.bad_guess

    def good_guess(self):
        self.speech_text = Translator.good_guess

    def begin_round(self):
        self.player.is_playing = True

    @staticmethod
    def get_category() -> Category:
        name = 'Country'
        things = get_category_things(CategoryEnum.COUNTRIES)

        return Category(name, things)

    def get_player(self) -> Player:
        raise NotImplementedError

    @staticmethod
    def get_random_category() -> CategoryEnum:
        return CategoryEnum.COUNTRY

    @staticmethod
    def get_initial_dict() -> dict:
        """
        Gets the initial state of the game variables as
        """
        return {
            'player': {
                'is_playing': False
            },
            'category': {
                'name': 'none',
                'category': CategoryEnum.COUNTRIES
            }
        }
