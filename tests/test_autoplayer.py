import unittest

import autoplayer


class AutoPlayerTest(unittest.TestCase):

    def test_decide_move(self):
        ap = autoplayer.AutoPlayer('O')
        ap.chances = {
            '........X': {
                0: 1,
                1: 1,
                2: 1,
                3: 1,
                4: 1,
                5: 1,
                6: 1,
                7: 93,
            }
        }
        moves = [ap.decide_move('X........') for _ in range(100)]
        self.assertGreater(moves.count(1), 80)
