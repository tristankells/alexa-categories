from Category import Category


class Categories:
    def __init__(self, session_variables):
        self.is_playing = session_variables.is_playing
        self.category = session_variables.current_category

        player = Player(session_variables.player)

        countries = ['New Zealand', 'Australia']

        self.country = Category(countries)

    def make_a_guess(self):
        raise NotImplementedError

    def launch(self):
        player.is_playing = True

