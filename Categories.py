from Category import Category
from CategoryEnum import CategoryEnum
from Translator import Translator
from Player import Player



class Categories:
    def __init__(self, session_variables):
        self.player = self.getPlayer(session_variables.player)
        self.category = self.getCategory(session_variables.category)

        self.speech_text = None
        self.re_prompt = None

    def launch(self):
        self.player.is_playing = True
        self.speech_text = Translator.launch.format(self.category.name)
        raise NotImplementedError

    def make_a_guess(self):
        raise NotImplementedError

    def get_category(self) -> Category:
        raise NotImplementedError

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
                'category'
            }
        }
