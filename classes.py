import sys


class Item:
    def __init__(self, set_name, kind, cost, stars):
        self.set = set_name
        self.kind = kind
        self.cost = cost
        self.stars = stars

    def name(self) -> str:
        return self.set + '::' + self.kind


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Plan:
    def __init__(self, money: int):
        self.money_remaining = money
        self.stars = 0
        self.items = []

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

sys.path.append(".")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
