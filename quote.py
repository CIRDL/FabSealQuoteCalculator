from liner_toolkit import *


# Quote class that contains whole order
class Quote:
    def __init__(self):
        self.lining_system = LiningSystem()
        self.accessories = Accessories()


# Accessories class
class Accessories:
    def __init__(self):
        self.geo = 0


# Lining System class
class LiningSystem:
    def __init__(self):
        self.liner = Liner("empty", 0, 0)
        # In case of a discount
        self.liner_cost = 0
        # In case of a discount
        self.discount_percentage = 0
        self.total_liners = 1
        self.weight = 0
        self.cost = 0

    # Sets price of lifting hem
    def set_lifting_hem(self):
        self.liner.set_lifting_hem()
        self.set_weight()
        self.set_cost()

    # Discount liner
    def discount_liner(self, discount_percentage):
        # Record for documentation
        self.discount_percentage = discount_percentage
        # Gets real discount number
        discount_number = discount_percentage / 100

        # Records new single liner cost
        self.liner_cost = self.liner.total_cost - (discount_number * self.liner.total_cost)
        self.set_weight()
        self.set_cost()

    # Add liners
    def add_liners(self, added_liners):
        self.total_liners += added_liners
        self.set_weight()
        self.set_cost()

    # Calculates cost of liner (depending on discount)
    def get_liner_cost(self):
        if self.discount_percentage == 0:
            return self.liner.total_cost
        else:
            return self.liner_cost

    # Sets lining system weight
    def set_weight(self):
        self.weight = self.liner.total_weight * self.total_liners

    # Sets lining system cost
    def set_cost(self):
        self.cost = self.get_liner_cost() * self.total_liners


# Liner class for that encapsulates all shapes of liners
class Liner:
    def __init__(self, tank, price, weight):
        self.sq_price = price
        self.sq_weight = weight
        self.info = self.__create_liner(tank.lower())
        self.lifting_hem_area = 0
        self.tank_square_footage = 0
        self.five_percent = 0
        self.liner_square_footage = 0
        self.weight = 0
        self.cost = 0
        # Including lifting hem
        self.total_five_percent = 0
        # Including lifting hem
        self.total_liner_square_footage = 0
        # Including lifting hem
        self.total_cost = 0
        # Including lifting hem
        self.total_weight = 0

    # Updates liner configurations
    def configure(self):
        self.tank_square_footage = self.info.tank_square_footage
        self.five_percent = self.info.calculate_five_percent()
        self.liner_square_footage = self.info.liner_square_footage
        self.weight = self.__calculate_liner_weight()
        self.cost = self.__calculate_liner_cost()
        # Lifting hem
        self.total_five_percent = self.five_percent
        # Lifting hem
        self.total_liner_square_footage = self.liner_square_footage
        # Lifting hem
        self.total_cost = self.cost
        # Lifting hem
        self.total_weight = self.weight

    # Sets lifting hem for liner
    def set_lifting_hem(self):
        self.lifting_hem_area = self.__get_lifting_hem_area()
        self.total_liner_square_footage += self.lifting_hem_area
        self.total_five_percent = self.total_liner_square_footage * 0.05
        self.total_cost = self.__calculate_liner_cost()
        self.total_weight = self.__calculate_liner_weight()

    # Calculates weight of liner
    def __calculate_liner_weight(self):
        return round(self.sq_weight * (self.liner_square_footage + self.lifting_hem_area))

    # Calculates cost of liner
    def __calculate_liner_cost(self):
        return round(self.sq_price * (self.liner_square_footage + self.lifting_hem_area), 2)

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

    # Calculates lifting hem area depending on liner type
    def __get_lifting_hem_area(self):
        if isinstance(self.info, CLiner):
            return self.info.circumference_liner
        elif isinstance(self.info, RLiner):
            return self.info.perimeter_liner
        else:
            return 0


# Circular liner class
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
        return self.diameter_tank ** 2

    # Calculates square footage of tank wall
    def __tank_wall_square_footage(self):
        return self.circumference_tank * self.depth_tank

    # Calculates square footage of tank
    def __set_tank_square_footage(self):
        self.tank_square_footage = round(self.__tank_bottom_square_footage() + self.__tank_wall_square_footage())

    # Calculates five percent of liner order
    def calculate_five_percent(self):
        scrap_cost = 0.05
        return round(self.liner_square_footage * scrap_cost, 2)

    # Calculates square footage of liner bottom
    def __liner_bottom_square_footage(self):
        return self.diameter_liner ** 2

    # Calculates square footage of liner wall
    def __liner_wall_square_footage(self):
        return self.circumference_liner * self.depth_liner

    # Calculates square footage of liner
    def __set_liner_square_footage(self):
        self.liner_square_footage = round(self.__liner_bottom_square_footage() + self.__liner_wall_square_footage())


# Rectangular liner class
class RLiner:
    def __init__(self):
        self.length_tank = 0
        self.length_liner = 0
        self.width_tank = 0
        self.width_liner = 0
        self.depth_tank = 0
        self.depth_liner = 0
        self.perimeter_tank = 0
        self.perimeter_liner = 0
        self.tank_square_footage = 0
        self.liner_square_footage = 0

    # Update liner configuration
    def configure(self, length_ft, length_inch, width_ft, width_inch, depth_ft, depth_inch, depth_extensions):
        self.length_tank = converter(length_ft, length_inch)
        self.length_liner = length_modifier(self.length_tank)
        self.width_tank = converter(width_ft, width_inch)
        self.width_liner = self.width_tank
        self.depth_tank = converter(depth_ft, depth_inch)
        self.depth_liner = self.depth_tank + converter(0, depth_extensions)
        self.perimeter_tank = (self.length_tank + self.width_tank) * 2
        self.perimeter_liner = (self.length_liner + self.width_liner) * 2
        self.__set_tank_square_footage()
        self.__set_liner_square_footage()

    # Calculates square footage of tank bottom
    def __tank_bottom_square_footage(self):
        return self.length_tank * self.width_tank

    # Calculates square footage of tank wall
    def __tank_wall_square_footage(self):
        return (self.length_tank + self.width_tank) * 2 * self.depth_tank

    # Calculates square footage of tank
    def __set_tank_square_footage(self):
        self.tank_square_footage = round(self.__tank_bottom_square_footage() + self.__tank_wall_square_footage())

    # Calculates five percent of liner order
    def calculate_five_percent(self):
        scrap_cost = 0.05
        return round(self.liner_square_footage * scrap_cost, 2)

    # Calculates square footage of liner bottom
    def __liner_bottom_square_footage(self):
        return self.length_liner * self.width_liner

    # Calculates square footage of liner wall
    def __liner_wall_square_footage(self):
        return (self.length_liner + self.width_liner) * 2 * self.depth_liner

    # Calculates square footage of liner
    def __set_liner_square_footage(self):
        self.liner_square_footage = round(self.__liner_bottom_square_footage() + self.__liner_wall_square_footage())


# Flat sheet liner class
class FLiner:
    def __init__(self):
        self.length_liner = 0
        self.width_liner = 0
        self.tank_square_footage = 0
        self.liner_square_footage = 0

    # Update liner configuration
    def configure(self, length_ft, length_inch, width_ft, width_inch):
        self.length_liner = converter(length_ft, length_inch)
        self.width_liner = converter(width_ft, width_inch)
        self.tank_square_footage = round(self.length_liner * self.width_liner)
        self.liner_square_footage = self.tank_square_footage

    # Calculates five percent of liner order
    def calculate_five_percent(self):
        scrap_cost = 0
        return self.liner_square_footage * scrap_cost
