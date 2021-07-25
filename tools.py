OPERATIONS = [
    (0, 1, 2, 3, 4, 5, 6, 7, 8),
    (8, 7, 6, 5, 4, 3, 2, 1, 0),
    (2, 1, 0, 5, 4, 3, 8, 7, 6),
    (6, 7, 8, 3, 4, 5, 0, 1, 2),
    (6, 3, 0, 7, 4, 1, 8, 5, 2),
    (2, 5, 8, 1, 4, 7, 0, 3, 6),
    (0, 3, 6, 1, 4, 7, 2, 5, 8),
    (8, 5, 2, 7, 4, 1, 6, 3, 0),
]


def get_possible_moves(field: str) -> list:
    return [i for i, c in enumerate(field) if c == '.']


def rearrange(field: str, indizes: tuple) -> str:
    return ''.join(field[i] for i in indizes)


def get_equivalent_fields(field: str) -> list:
    return [rearrange(field, op) for op in OPERATIONS]


def get_representative(field: str) -> (str, int):
    equivalent_fields = get_equivalent_fields(field)
    representative_field = sorted(equivalent_fields)[0]
    operation_index = equivalent_fields.index(representative_field)
    return representative_field, operation_index
