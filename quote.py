from abc import ABC, abstractmethod


class Liner:
    def __init__(self, tank, price, weight):
        self.tank_type = tank
        self.sqft_price = price
        self.sqft_weight = weight

