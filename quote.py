from liner_toolkit import *


# Quote class that contains whole order
class Quote:
    def __init__(self):
        self.lining_system = LiningSystem()
        self.accessories = Accessories()


# Accessories class
class Accessories:
    def __init__(self):
        self.geo = Geo(0, 0, 0)


# Geo class
class Geo:
    def __init__(self, wall_thickness, liner_bottom_square_footage, liner_wall_square_footage):
        self.wall_sq_price = self.__calculate_wall_sq_price(wall_thickness)
        self.floor_sq_price = 0.59
        self.wall_sq_weight = self.__calculate_wall_sq_weight(wall_thickness)
        self.floor_sq_weight = 0.10
        self.bottom_square_footage = liner_bottom_square_footage
        self.wall_square_footage = liner_wall_square_footage
        self.layers = 1
        self.cost = self.__calculate_cost()
        self.weight = self.__calculate_weight()
        self.total_cost = self.cost
        self.total_weight = self.weight

    @staticmethod
    # Calculates cost of material
    def __calculate_wall_sq_price(wall_thickness):
        if wall_thickness == 16:
            return 0.59
        else:
            return 0.45

    @staticmethod
    # Calculates weight of material
    def __calculate_wall_sq_weight(wall_thickness):
        if wall_thickness == 16:
            return 0.10
        else:
            return 0.08

    # Add layer to geo
    def add_layer(self, added_layers):
        self.layers += added_layers
        self.set_total_cost()
        self.set_total_weight()

    # Calculate cost
    def __calculate_cost(self):
        return round((self.wall_square_footage * self.wall_sq_price) + (self.bottom_square_footage *
                                                                        self.floor_sq_price), 2)

    # Calculate weight
    def __calculate_weight(self):
        return round((self.wall_square_footage * self.wall_sq_weight) + (self.bottom_square_footage *
                                                                         self.floor_sq_weight))

    # Calculates total cost (in case of layers)
    def set_total_cost(self):
        return self.layers * self.cost

    # Calculates total weight (in case of layers)
    def set_total_weight(self):
        return self.layers * self.weight


# Batten Strip class
class BattenStrips:
    def __init__(self, batten_strip_type, area):
        self.type = self.__configure_type(batten_strip_type.lower())
        self.price_per_unit = self.__calculate_price_per_unit()
        self.cost = self.__calculate_cost(area)

    @staticmethod
    # Assigns type of batten strip
    def __configure_type(type):
        if type[0] == 'p':
            return "poly-pro"
        else:
            return "stainless steel"

    # Calculates cost per batten strip based off type
    def __calculate_price_per_unit(self):
        if self.type[0] == 'p':
            return 10.0
        else:
            return 33.30

    # Calculates batten strip cost
    def ___calculate_cost(self, area):
        return round(area * self.price_per_unit, 2)


# JBolt class
class JBolts:
    def __init__(self, area):
        self.jbolt_cost = 9.5
        self.jbolt_number = self.__calculate_jbolt_number(area)
        self.cost = self.__calculate_cost()

    @staticmethod
    # Calculates number of jbolts
    def __calculates_jbolt_number( area):
        return math.ceil(area / 1.5)

    # Configures cost for jbolts
    def __calculate_cost(self, area):
        return round(self.jbolt_cost * self.jbolt_number, 2)


# Oarlocks class
class Oarlocks:
    def __init__(self, oarlocks_number):
        self.oarlock_price = 9.00
        self.oarlocks_number = oarlocks_number
        self.oarlocks_cost = self.__calculate_cost()

    # Configures cost for oarlocks
    def __calculate_cost(self):
        return round(self.oarlock_price * self.oarlocks_number, 2)


# Crates class
class Crate:
    def __init__(self, size):
        self.size = size.lower()
        self.cost = self.__calculate_cost()
        self.weight = self.__calculate_weight()

    # Configures cost of crate
    # Large or small sizes
    def __calculate_cost(self):
        if self.size[0] == 'l':
            return 650
        elif self.size[0] == 's':
            return 375
        else:
            return 0

    # Configures weight of crate
    # Large or small sizes
    def __calculate_weight(self):
        if self.size[0] == "l":
            return 510
        elif self.size[0] == "s":
            return 140
        else:
            return 0


# Leak Detection class
class LeakDetection:
    def __init__(self, area):
        self.price_per_unit = 10.00
        self.cost = self.__calculate_cost(area)

    # Configures cost of leak detection
    def __calculate_cost(self, area):
        return round(area * self.price_per_unit, 2)


# Nailing Strip class
class NailingStrip:
    def __init__(self, area):
        self.price_per_unit = 1.00
        self.cost = self.__calculate_cost(area)

    # Configures cost of nailing strip
    def __calculate_cost(self, area):
        return round(area * self.price_per_unit, 2)


# Stainless Clip class
class StainlessClips:
    def __init__(self, area):
        self.price_per_unit = 6.00
        self.cost = self.__calculate_cost(area)

    # Configures cost of stainless clips
    def __calculates_cost(self, area):
        return math.ceil(self.price_per_unit * area)


# Installation class
class InstallationPackage:
    def __init__(self, is_inside_usa, is_within_600_miles, traveling_cost, lining_system):
        self.site_survey_cost = self.__calculate_site_survey_cost(is_inside_usa.lower(), is_within_600_miles.lower())
        self.traveling_cost = traveling_cost
        self.tools_and_hardware = lining_system.liner_cost * 0.1
        self.total_tools_and_hardware = self.tools_and_hardware * lining_system.total_liners
        self.install_cost = self.__calculate_install_cost(lining_system)
        self.cost = self.__calculate_cost()

    # Calculates total cost of installation package
    def __calculate_cost(self):
        return self.site_survey_cost + self.traveling_cost + self.total_tools_and_hardware + self.install_cost

    @staticmethod
    # Calculates site survey cost depending on location
    def __calculate_site_survey_cost(is_inside_usa, is_within_600_miles):
        if is_inside_usa[0] == "y":
            if is_within_600_miles[0] == 'y':
                return 1500
            else:
                return 2500
        # Will have to update with information later in gui_help
        else:
            return 0

    # Sets site survey cost (in case falls out of jurisdiction)
    def set_site_survey_cost(self, site_survey_cost):
        self.site_survey_cost = site_survey_cost

    # Calculates install price depending on liner argument
    def __calculate_install_cost(self, lining_system):
        length = self.__calculate_length(lining_system)
        employee_price = 750
        if length < 30:
            number_employees = 5
            number_days = 3
        elif length < 50:
            number_employees = 5
            number_days = 4
        elif length < 70:
            number_employees = 5
            number_days = 5
        elif length < 90:
            number_employees = 5
            number_days = 6
        elif length < 110:
            number_employees = 6
            number_days = 6
        elif length < 130:
            number_employees = 6
            number_days = 7
        elif length < 150:
            number_employees = 6
            number_days = 8
        else:
            number_employees = 0
            number_days = 0
        return employee_price * number_employees * number_days

    @staticmethod
    # Calculates length used for install depending on tank shape
    def __calculate_length(lining_system):
        if isinstance(lining_system.liner.info, CLiner):
            return lining_system.liner.info.diameter_liner
        elif isinstance(lining_system.liner.info, RLiner):
            return max(lining_system.liner.info.width_liner, lining_system.liner.info.length_liner)
        else:
            return 0

    # Sets install cost in case of modification
    def set_install_cost(self, install_cost):
        self.install_cost = install_cost


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
