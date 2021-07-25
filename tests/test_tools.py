import unittest

import tools


class ToolsTests(unittest.TestCase):

    def test_equivalent_hashes(self):
        self.assertEqual(
            ['X....X.O.',
             '.O.X....X',
             '..XX...O.',
             '.O...XX..',
             '..XO...X.',
             '.X...OX..',
             'X....O.X.',
             '.X.O....X'],
            tools.get_equivalent_fields('X....X.O.')
        )

    def test_get_representative(self):
        self.assertEqual(
            ('..XO...X.', 4),
            tools.get_representative('X....X.O.')
        )

    def test_get_representative__low(self):
        self.assertEqual(
            ('........X', 0), tools.get_representative('........X'))
        self.assertEqual(
            ('........X', 1), tools.get_representative('X........'))
        self.assertEqual(
            ('........X', 2), tools.get_representative('......X..'))
        self.assertEqual(
            ('........X', 3), tools.get_representative('..X......'))
