class Category:
    def __init__(self, name, things):
        self.name = name

        self.things = [x.lower() for x in things]  # An list of strings representing things that belong to a category

    def is_guess_in_category(self, guess: str):
        return guess in self.things
