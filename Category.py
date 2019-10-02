class Category:
    def __init__(self, name, things):
        self.name = name
        self.things = things # An array of strings representing things that belong to a category

    def is_guess_in_category(self, guess):
        raise NotImplementedError
        # if guess in in things
        #   then return true
        # If it is not
        #   return false
