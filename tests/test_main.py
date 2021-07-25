import unittest

import main


class MainTests(unittest.TestCase):

    def test_check_win(self):
        field = 'XOO' \
                'OX.' \
                'X..'
        self.assertEqual(
            '',
            main.check_win(field)
        )
