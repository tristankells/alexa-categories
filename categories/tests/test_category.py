import unittest
from Category import Category


class CategoryTests(unittest.TestCase):
    def test__good_guess_returns_true(self):
        category = Category('countries', ['Afghanistan', 'Armenia', 'Amsterdam'])

        guess = 'afghanistan'

        self.assertTrue(category.is_guess_in_category(guess))

    def test__bad_guess_returns_false(self):
        category = Category('countries', ['Afghanistan', 'Armenia', 'Amsterdam'])

        guess = 'red'

        self.assertFalse(category.is_guess_in_category(guess))


if __name__ == '__main__':
    unittest.main()
