from liner_toolkit import *


# Quote class that contains whole order
class Quote:
    def __init__(self):
        self.liner = Liner("empty", 0, 0)


# Liner class for encapsulation of order
class Liner:
    def __init__(self, tank, price, weight):
        self.sq_price = price
        self.sq_weight = weight
        self.info = self.__create_liner(tank.lower())
        self.tank_square_footage = 0
        self.five_percent = 0
        self.liner_square_footage = 0
        self.weight = 0
        self.cost = 0

    # Updates liner configurations
    def configure(self):
        self.tank_square_footage = self.info.tank_square_footage
        self.five_percent = self.info.calculate_five_percent()
        self.liner_square_footage = self.info.liner_square_footage
        self.weight = self.__calculate_liner_weight()
        self.cost = self.__calculate_liner_cost()

    # Calculates weight of liner
    def __calculate_liner_weight(self):
        return self.sq_weight * self.liner_square_footage

    # Calculates cost of liner
    def __calculate_liner_cost(self):
        return self.sq_price * self.liner_square_footage

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
        self.diameter_tank = 0
        self.diameter_liner = 0
        self.depth_tank = 0
        self.depth_liner = 0
        self.circumference_tank = 0
        self.circumference_liner = 0
        self.tank_square_footage = 0
        self.liner_square_footage = 0
        self.weight = 0
        self.cost = 0

    # Update liner configurations
    def configure(self, diameter_ft, diameter_inch, depth_ft, depth_inch, depth_extensions):
        self.diameter_tank = converter(diameter_ft, diameter_inch)
        self.diameter_liner = diameter_modifier(self.diameter_tank)
        self.depth_tank = converter(depth_ft, depth_inch)
        self.depth_liner = self.depth_tank + converter(0, depth_extensions)
        self.circumference_tank = self.diameter_tank * math.pi
        self.circumference_liner = self.diameter_liner * math.pi
        self.__set_tank_square_footage()
        self.__set_liner_square_footage()

    # Calculates square footage of tank bottom
    def __tank_bottom_square_footage(self):
        return round(self.diameter_tank ** 2)

    # Calculates square footage of tank wall
    def __tank_wall_square_footage(self):
        return round(self.circumference_tank * self.depth_tank)

    # Calculates square footage of tank
    def __set_tank_square_footage(self):
        self.tank_square_footage = self.__tank_bottom_square_footage() + self.__tank_wall_square_footage()

    # Calculates five percent of liner order
    def calculate_five_percent(self):
        scrap_cost = 0.05
        return self.liner_square_footage * scrap_cost

    # Calculates square footage of liner bottom
    def __liner_bottom_square_footage(self):
        return round(self.diameter_liner ** 2)

    # Calculates square footage of liner wall
    def __liner_wall_square_footage(self):
        return round(self.circumference_liner * self.depth_liner)

    # Calculates square footage of liner
    def __set_liner_square_footage(self):
        self.liner_square_footage = self.__liner_bottom_square_footage() + self.__liner_wall_square_footage()


# Flat sheet liner class for encapsulation
class FLiner:
    def __init__(self):
        pass


# Rectangular liner class for encapsulation
class RLiner(FLiner):
    def __init__(self):
        pass
