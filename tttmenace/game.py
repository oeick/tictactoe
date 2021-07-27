import random

from tttmenace import tools


def make_random_move(field: str) -> int:
    possibilities = tools.get_possible_moves(field)
    move = random.choice(possibilities)
    return move


def read_move(field: str) -> int:
    """
    Returns id of move, or -1 if player wants quit playing.
    """
    key_map = {'q': 0, 'w': 1, 'e': 2,
               'a': 3, 's': 4, 'd': 5,
               'z': 6, 'x': 7, 'c': 8}
    move = -1
    while move == -1:
        key = input('your move: ')
        if key == '!':
            return -1
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
    print('\n'.join(
        ' '.join(c for c in field[r:r + 3])
        for r in range(0, 9, 3)))


def check_win(field: str) -> str:
    significant_places = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    winners = [field[i] for i, j, k in significant_places
               if field[i] == field[j] == field[k]
               and field[i] in ('X', 'O')]
    if winners:
        return winners[0]
    if field.count('.') == 0:
        return '-'
    return ''
