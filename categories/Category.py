from CategoryEnum import CategoryEnum


class Category:
    def __init__(self, enum: CategoryEnum, things: list):
        self.enum = enum

        self.name = enum.value

        self.things = [x.lower() for x in things]  # An list of strings representing things that belong to a category

    def guess_in_category(self, guess: str):
        return guess in self.things
