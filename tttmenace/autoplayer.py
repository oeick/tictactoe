import random
import yaml

from tttmenace import tools


class AutoPlayer:
    chances: dict[str, dict[int, int]] = {}
    history: list[tuple[str, int]] = []
    side: str

    def __init__(self, side: str):
        self.side = side

    def decide_move(self, field: str):
        representative, opi = tools.get_representative(field)
        if representative not in self.chances:
            possibilities = tools.get_possible_moves(representative)
            repr_move = random.choice(possibilities)
        else:
            min_value = min(self.chances[representative].values())
            choices = []
            for m, v in self.chances[representative].items():
                choices += [m for _ in range(v - min_value + 1)]
            repr_move = random.choice(choices)
        self.history.append((representative, repr_move))
        return tools.OPERATIONS[opi][repr_move]

    def finished(self, winner: str):
        if winner == self.side:
            self.change_chances(3)
        elif winner == '-':
            self.change_chances(1)
        else:
            self.change_chances(-1)
        self.history = []

    def change_chances(self, c):
        for field, move in self.history:
            if field not in self.chances:
                possibilities = tools.get_possible_moves(field)
                self.chances[field] = {p: 0 for p in possibilities}
            self.chances[field][move] += c

    def save_chances(self, filename: str):
        with open(filename, 'w', encoding='utf-8') as fp:
            yaml.dump(self.chances, fp)

    def load_chances(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as fp:
            self.chances = yaml.load(fp)
