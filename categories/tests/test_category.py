import unittest
from CategoryEnum import CategoryEnum
from Category import Category


class CategoryTests(unittest.TestCase):
    def test__good_guess_returns_true(self):
        category = Category(CategoryEnum.COUNTRIES, ['Afghanistan', 'Armenia', 'Amsterdam'])

        guess = 'afghanistan'

        self.assertTrue(category.guess_in_category(guess))

    def test__bad_guess_returns_false(self):
        category = Category(CategoryEnum.COUNTRIES, ['Afghanistan', 'Armenia', 'Amsterdam'])

        guess = 'red'

        self.assertFalse(category.guess_in_category(guess))


if __name__ == '__main__':
    unittest.main()
