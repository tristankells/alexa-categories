"""
A 'static' module for all the game response
"""


def launch(category): return 'Welcome to Categories. Your category is, drum roll please...{}'.format(category)


good_guess = 'Correct'

_round_over = 'Round over. You got {} guess correct. Would you like to play again?'


def bad_guess_not_in_category(guesses_count): return 'Not in category. ' + _round_over.format(guesses_count)


def bad_guess_not_unique(guesses_count): return 'Not a unique answer. ' + _round_over.format(guesses_count)
