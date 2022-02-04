from classes import Item
from classes import Plan


class OptimizerMeta(type):
    '''
    Optimizer Metaclass that will be used for optimizer class creation
    '''
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'optimize') and
                callable(subclass.optimize))


class BaseOptimizer(metaclass=OptimizerMeta):
    __slots__ = ['optimize']
    '''
    Used to confirm that all optimizers conform to the OptimizerMeta interface
    '''
    pass


class LeastRemainingMoney(BaseOptimizer):
    def optimize(self, state: Plan, item: Item, returns: Plan):
        if returns.money_remaining < state.money_remaining:
            state.money_remaining = returns.money_remaining
            state.stars = item.stars + returns.stars
            state.items = [item.name()] + returns.items
        return state

