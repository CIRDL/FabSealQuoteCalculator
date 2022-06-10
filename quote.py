from abc import ABC, abstractmethod


# Quote class that contains whole order
class Quote:
    def __init__(self):
        self.liner = Liner("empty", 0, 0)


# Liner class for encapsulation of order
class Liner:
    def __init__(self, tank, price, weight):
        self.sq_price = price
        self.sq_weight = weight
        self.liner = self.__create_liner(tank.lower())

    @staticmethod
    # Creates specific liner
    def __create_liner(tank):
        if tank[0] == 'c':
            return CLiner()
        elif tank[0] == 'f':
            return FLiner()
        elif tank[0] == 'r':
            return RLiner()
        else:
            return 0


# Circular liner class for encapsulation
class CLiner:
    def __init__(self):
        pass


# Flat sheet liner class for encapsulation
class FLiner:
    def __init__(self):
        pass


# Rectangular liner class for encapsulation
class RLiner(FLiner):
    def __init__(self):
        pass
