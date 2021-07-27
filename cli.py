"""
Human vs AutoPlayer.

Enter `!` to quit playing.

Use `q`, `w`, `e` for top row,
`a`, `s`, `d` for mid row, and
`z`, `x`, `c` for bottom row.
"""


from tttmenace.autoplayer import AutoPlayer
from tttmenace import game


def main():
    playing = True

    count = {'X': 0, 'O': 0, '-': 0}

    ap = AutoPlayer('X')
    ap.load_chances('decision_model.yaml')

    while playing:
        field = '.........'
        winner = ''
        while playing and not winner:
            move = ap.decide_move(field)
            field = game.execute_move(field, move, 'X')
            game.show_field(field)
            print()
            winner = game.check_win(field)
            if not winner:
                move = game.read_move(field)
                if move == -1:
                    playing = False
                else:
                    field = game.execute_move(field, move, 'O')
                    game.show_field(field)
                    print()
                    winner = game.check_win(field)
        if playing:
            ap.finished(winner)
            print(f'{winner=}')
            count[winner] += 1
            print(count)
            print()
    ap.save_chances('decision_model.yaml')
    print(count)


if __name__ == '__main__':
    main()
