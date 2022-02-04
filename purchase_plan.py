import optimizers
import spring_prelude
from classes import Item
from classes import Plan


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
    show_plan(purchase_plan(
        spring_prelude.items,
        spring_prelude.money,
        optimizers.LeastRemainingMoney()
    ))

