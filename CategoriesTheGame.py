from Category import Category

class CategoriesTheGame :

    def __init__(self, is_playing, current_category ) :
        self.is_playing = is_playing
        self.category = current_category

        countries = ['New Zealand', 'Australia']

        self.country = Category(countries)


        self.country.things



    def makeAGuess(self) :
        is_playing = False
        raise NotImplementedError


Game = CategoriesTheGame(True, "planets")


Game.makeAGuess()

