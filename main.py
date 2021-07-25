import random

import tools
from autoplayer import AutoPlayer


def make_random_move(field: str) -> int:
    possibilities = tools.get_possible_moves(field)
    move = random.choice(possibilities)
    return move


def read_move(field: str) -> int:
    key_map = {'q': 0, 'w': 1, 'e': 2,
               'a': 3, 's': 4, 'd': 5,
               'z': 6, 'x': 7, 'c': 8}
    move = -1
    while move == -1:
        key = input('your move: ')
        move = key_map.get(key, -1)
        if field[move] != '.':
            print('illegal move')
            move = -1
    return move


def execute_move(field: str, move: int, side: str) -> str:
    if field[move] != '.':
        raise ValueError(f'Illegal move: {move}')
    return field[:move] + side + field[move + 1:]


def show_field(field: str):
    """
    >>> show_field('X.O....OX')
    X . O
    . . .
    . O X
    """
    print('\n'.join(
        ' '.join(c for c in field[r:r + 3])
        for r in range(0, 9, 3)))


def check_win(field: str) -> str:
    winner = ''
    if 'XXX' in (field[:3], field[3:6], field[6:9]):
        winner = 'X'
    if 'OOO' in (field[:3], field[3:6], field[6:9]):
        winner = 'O'
    for i in range(0, 3):
        if field[i] + field[i + 3] + field[i + 6] in ('XXX', 'OOO'):
            winner = field[i]
            break
    if field[0] + field[4] + field[8] in ('XXX', 'OOO'):
        winner = field[4]
    if field[2] + field[4] + field[6] in ('XXX', 'OOO'):
        winner = field[4]
    if field.count('.') == 0 and not winner:
        winner = '-'
    return winner


def main():
    games_to_play = 10
    is_printing = True

    count = {'X': 0, 'O': 0, '-': 0}

    # ap1 = AutoPlayer('O')
    # ap1.load_chances('chances_x.bin')

    ap2 = AutoPlayer('X')
    ap2.load_chances('chances_o.bin')

    while games_to_play > 0:
        games_to_play -= 1
        field = '.........'
        winner = ''
        while not winner:
            # move = make_random_move(field)
            # move = read_move(field)
            move = ap2.decide_move(field)
            field = execute_move(field, move, 'X')
            if is_printing:
                show_field(field)
                print()
            winner = check_win(field)
            if not winner:
                # move = ap1.decide_move(field)
                move = read_move(field)
                field = execute_move(field, move, 'O')
                if is_printing:
                    show_field(field)
                    print()
                winner = check_win(field)
        # ap1.finished(winner)
        ap2.finished(winner)
        if is_printing:
            print(f'{winner=}')
        count[winner] += 1
        if is_printing:
            print(count)
            print()
    # ap1.save_chances('chances_x.bin')
    ap2.save_chances('chances_o.bin')
    print(count)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
