from tttmenace.autoplayer import AutoPlayer
from tttmenace import game


def main():
    games_to_play = 1
    is_printing = True

    count = {'X': 0, 'O': 0, '-': 0}

    ap = AutoPlayer('X')
    ap.load_chances('decision_model.yaml')

    while games_to_play > 0:
        games_to_play -= 1
        field = '.........'
        winner = ''
        while not winner:
            move = ap.decide_move(field)
            field = game.execute_move(field, move, 'X')
            if is_printing:
                game.show_field(field)
                print()
            winner = game.check_win(field)
            if not winner:
                # move = game.read_move(field)
                move = game.read_move(field)
                field = game.execute_move(field, move, 'O')
                if is_printing:
                    game.show_field(field)
                    print()
                winner = game.check_win(field)
        ap.finished(winner)
        if is_printing:
            print(f'{winner=}')
        count[winner] += 1
        if is_printing:
            print(count)
            print()
    ap.save_chances('decision_model.yaml')
    print(count)


if __name__ == '__main__':
    main()
