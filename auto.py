"""
AutoPlayer will play against itself.

Give number of rounds to play as command line parameter.
"""

import sys

from tttmenace.autoplayer import AutoPlayer
from tttmenace import game


def main(rounds_to_play: int):
    round_counter = 0

    count = {'X': 0, 'O': 0, '-': 0}

    ap_x = AutoPlayer('X')
    ap_x.load_chances('decision_model.yaml')

    ap_o = AutoPlayer('O')
    ap_o.load_chances('decision_model.yaml')

    while round_counter < rounds_to_play:
        round_counter += 1
        field = '.........'
        winner = ''
        while not winner:
            move = ap_x.decide_move(field)
            field = game.execute_move(field, move, 'X')
            winner = game.check_win(field)
            if not winner:
                move = ap_o.decide_move(field)
                field = game.execute_move(field, move, 'O')
                winner = game.check_win(field)
        ap_x.finished(winner)
        ap_o.finished(winner)
        count[winner] += 1
    ap_x.save_chances('decision_model.yaml')
    print(count)


if __name__ == '__main__':
    num_of_rounds = int(sys.argv[1])
    main(num_of_rounds)
