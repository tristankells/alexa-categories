from categories.Category import Category
from categories.CategoryEnum import CategoryEnum
from categories.Translator import Translator
from categories.Player import Player
import csv


class Categories:
    def __init__(self, session_variables):
        self.player = Player(session_variables['player'])
        self.category = self.get_category(session_variables['category'])

        self.speech_text = None
        self.re_prompt = None

    def launch(self):
        self.player.is_playing = True
        self.speech_text = Translator.launch.format(self.category.name)

    @staticmethod
    def get_countries():

        with open('Data/Countries.csv', 'r') as f:
            reader = csv.reader(f)
            list_of_countries = list(reader)

        return list_of_countries

    def make_a_guess(self):
        raise NotImplementedError

    @staticmethod
    def get_category(category_variables) -> Category:
        name = 'Country'
        things = []

        return Category(name, things)

    def get_player(self) -> Player:
        raise NotImplementedError

    @staticmethod
    def get_random_category() -> CategoryEnum:
        return CategoryEnum.COUNTRY

    @staticmethod
    def get_initial_dict() -> object:
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
