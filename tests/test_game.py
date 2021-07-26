import unittest

from tttmenace import game


class GameTests(unittest.TestCase):

    def test_check_win__no_winner(self):
        field = 'XOO' \
                'OX.' \
                'X..'
        self.assertEqual(
            '',
            game.check_win(field)
        )

    def test_check_win__x(self):
        field = 'OOX' \
                'OX.' \
                'X..'
        self.assertEqual(
            'X',
            game.check_win(field)
        )

    def test_check_win__draw(self):
        field = 'XOX' \
                'OXO' \
                'OXO'
        self.assertEqual(
            '-',
            game.check_win(field)
        )

