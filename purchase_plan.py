import optimizers
from classes import Item
from classes import Plan

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
    Item('', 'fan', 435, 6),
    Item('Moonlit Cliff', 'dress', 780, 6),
    Item('Moonlit Cliff', 'hair', 380, 6),
    Item('Moonlit Cliff', 'hat', 250, 5),
    Item('Moonlit Cliff', 'makeup', 65, 4),
    Item('Moonlit Cliff', 'mask', 70, 5),
    Item('Moonlit Cliff', 'earrings', 110, 5),
    Item('Moonlit Cliff', 'ring', 80, 4),
    Item('Moonlit Cliff', 'instrument', 450, 6),
    Item('Moonlit Cliff', 'stockings', 85, 4),
    Item('Moonlit Cliff', 'shoes', 270, 5),
})

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def purchase_plan(items: [Item],
                  money: int,
                  optimizer: optimizers.BaseOptimizer) -> Plan:
    '''
    least_money_left takes in a list of Dress Up Time Princess items and
    an amount of gold on hand, and returns a list of items which can be
    purchased, leaving the least amount of money left.
    '''
    if money < 0:
        raise ValueError("Not enough money")

    plan = Plan(money)

    for item in items:
        money_left = money - item.cost
        items_left = items.difference(set({item}))

        try:
            returns = purchase_plan(items_left, money_left, optimizer)
        except ValueError:
            return plan

        plan = optimizer.optimize(plan, item, returns)


    return plan


def show_plan(plan: Plan) -> None:
    print("Stars: {0}\nMoney Remaining: {1}".format(plan.stars, plan.money_remaining))
    print(plan.items)


if __name__ == '__main__':
    show_plan(purchase_plan(items, money, optimizers.LeastRemainingMoney()))

