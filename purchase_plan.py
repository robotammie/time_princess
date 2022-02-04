# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Item:
    def __init__(self, set_name, kind, cost, stars):
        self.set = set_name
        self.kind = kind
        self.cost = cost
        self.stars = stars

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

money = 1254

items = set({
    Item('Midspring Plum', 'dress', 700, 6),
    Item('Midspring Plum', 'hair', 380, 6),
    Item('Midspring Plum', 'hat', 290,5),
    Item('Midspring Plum', 'makeup', 90, 5),
    Item('Midspring Plum', 'earrings', 90, 4),
    Item('Midspring Plum', 'branch', 400, 6),
    Item('Midspring Plum', 'gloves', 130, 4),
    Item('Midspring Plum', 'ring', 80, 4),
    Item('Midspring Plum', 'stockings', 120, 5),
    Item('Midspring Plum', 'shoes', 270, 5),
    # Item('', 'fan', 435, 6),
    # Item('Moonlit Cliff', 'dress', 780, 6),
    # Item('Moonlit Cliff', 'hair', 380, 6),
    # Item('Moonlit Cliff', 'hat', 250, 5),
    # Item('Moonlit Cliff', 'makeup', 65, 4),
    # Item('Moonlit Cliff', 'mask', 70, 5),
    # Item('Moonlit Cliff', 'earrings', 110, 5),
    # Item('Moonlit Cliff', 'ring', 80, 4),
    # Item('Moonlit Cliff', 'instrument', 450, 6),
    # Item('Moonlit Cliff', 'stockings', 85, 4),
    # Item('Moonlit Cliff', 'shoes', 270, 5),
})

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def purchase_plan(items, money):
    '''
    least_money_left takes in a list of Dress Up Time Princess items and
    an amount of gold on hand, and returns a list of items which can be
    purchased, leaving the least amount of money left.
    '''
    if money < 0:
        raise ValueError("Not enough money")

    final_purchased = []
    final_remaining = money

    for item in items:
        money_left = money - item.cost
        items_left = items.difference(set({item}))

        try:
            purchased, remaining = least_money_left(items_left, money_left)
        except ValueError:
            return [], money

        if remaining < final_remaining:
            final_remaining = remaining
            final_purchased = [item.set + '::' + item.kind] + purchased

    return final_purchased, final_remaining

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    print(purchase_plan(items, money))

