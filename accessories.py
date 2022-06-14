from liner import *


# Accessories class
class Accessories:
    def __init__(self):
        self.orders = []
        self.discount = False
        self.additional_liners = False
        self.cost = None
        self.weight = None

    # Add geo
    def add_geo(self, wall_thickness, liner_bottom_square_footage, liner_wall_square_footage):
        self.orders.append(Geo(wall_thickness, liner_bottom_square_footage, liner_wall_square_footage))
        self.__update()

    # Add batten strips
    def add_batten_strip(self, batten_strip_type, area):
        self.orders.append(BattenStrips(batten_strip_type, area))
        self.__update()

    # Add j-bolts
    def add_j_bolts(self, area):
        self.orders.append(JBolts(area))
        self.__update()

    # Add oarlocks
    def add_oarlocks(self, oarlocks_number):
        self.orders.append(Oarlocks(oarlocks_number))
        self.__update()

    # Add crate
    def add_crate(self, size):
        self.orders.append(Crate(size))
        self.__update()

    # Add leak detection
    def add_leak_detection(self, area):
        self.orders.append(LeakDetection(area))
        self.__update()

    # Add nailing strips
    def add_nailing_strips(self, area):
        self.orders.append(NailingStrip(area))
        self.__update()

    # Add stainless clips
    def add_stainless_clips(self, area):
        self.orders.append(StainlessClips(area))
        self.__update()

    # Add lifting hem
    def add_lifting_hem(self, quote):
        self.orders.append("Lifting hem")
        quote.lining_system.set_lifting_hem()

    # Add installation package
    def add_installation_package(self, is_inside_usa, is_within_600_miles, traveling_cost, lining_system):
        self.orders.append(InstallationPackage(is_inside_usa, is_within_600_miles, traveling_cost, lining_system))
        self.__update()

    # Adds boot
    def add_boot(self, size):
        self.orders.append(Boot(size))
        self.__update()

    # Adds sump
    def add_sump(self, square_footage, square_footage_price):
        self.orders.append(Sump(square_footage, square_footage_price))
        self.__update()

    # Adds manway
    def add_manway(self, square_footage, square_footage_price):
        self.orders.append(ManWay(square_footage, square_footage_price))
        self.__update()

    # Adds center pole
    def add_center_pole(self, square_footage, square_footage_price):
        self.orders.append(CenterPole(square_footage, square_footage_price))
        self.__update()

    # Adds column
    def add_column(self, square_footage, square_footage_price):
        self.orders.append(Column(square_footage, square_footage_price))
        self.__update()

    # Add liner
    def add_liner(self, quote, added_liners):
        quote.lining_system.add_liners(added_liners)
        self.additional_liners = True

    # Discounts liner
    def discount_liner(self, quote, discount_percentage):
        quote.lining_system.discount_liner(discount_percentage)
        self.discount = True

    # Finds total cost of argument item
    def find_total_cost_of(self, item):
        total_cost = 0
        for order in self.orders:
            if isinstance(order, item):
                total_cost += order.cost
        return total_cost

    # Sets cost of accessories
    def __set_cost(self):
        self.cost = 0
        for order in self.orders:
            self.cost += order.cost

    # Sets weight of accessories
    def __set_weight(self):
        self.weight = 0
        for order in self.orders:
            if isinstance(order, Geo) or isinstance(order, Crate):
                self.weight += order.weight

    # Updates accessories
    def __update(self):
        self.__set_cost()
        self.__set_weight()


# Geo class
class Geo:
    def __init__(self, wall_thickness, liner_bottom_square_footage, liner_wall_square_footage):
        self.wall_sq_price = self.__calculate_wall_sq_price(wall_thickness)
        self.floor_sq_price = 0.59
        self.wall_sq_weight = self.__calculate_wall_sq_weight(wall_thickness)
        self.floor_sq_weight = 0.10
        self.bottom_square_footage = liner_bottom_square_footage
        self.wall_square_footage = liner_wall_square_footage
        self.cost = self.__calculate_cost()
        self.weight = self.__calculate_weight()

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

    # Calculate cost
    def __calculate_cost(self):
        return round((self.wall_square_footage * self.wall_sq_price) + (self.bottom_square_footage *
                                                                        self.floor_sq_price), 2)

    # Calculate weight
    def __calculate_weight(self):
        return round((self.wall_square_footage * self.wall_sq_weight) + (self.bottom_square_footage *
                                                                         self.floor_sq_weight))


# Batten Strip class
class BattenStrips:
    def __init__(self, batten_strip_type, area):
        self.type = self.__configure_type(batten_strip_type.lower())
        self.price_per_unit = self.__calculate_price_per_unit()
        self.cost = self.__calculate_cost(area)

    @staticmethod
    # Assigns type of batten strip
    def __configure_type(batten_strip_type):
        if batten_strip_type[0] == 'p':
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


# Boot class
class Boot:
    def __init__(self, size):
        self.size = size
        self.cost = self.__calculate_cost

    # Calculates cost of boot
    def __calculate_cost(self):
        if 2.0 <= self.size <= 4.0:
            return 125
        elif 4.0 < self.size <= 8.0:
            return 150
        else:
            return 200


# General material customization class
class GeneralCustomization:
    def __init__(self, square_footage, square_footage_price):
        self.labor_cost = 250
        self.cost = self.__calculate_cost(square_footage, square_footage_price)

    # Calculates cost of sump
    def __calculate_cost(self, square_footage, square_footage_price):
        return self.labor_cost + square_footage_price * square_footage


# Sump class
class Sump(GeneralCustomization):
    def __init__(self, square_footage, square_footage_price):
        super().__init__(square_footage, square_footage_price)


# ManWay class
class ManWay(GeneralCustomization):
    def __init__(self, square_footage, square_footage_price):
        super().__init__(square_footage, square_footage_price)


# Center Pole class
class CenterPole(GeneralCustomization):
    def __init__(self, square_footage, square_footage_price):
        super().__init__(square_footage, square_footage_price)


# Column class
class Column(GeneralCustomization):
    def __init__(self, square_footage, square_footage_price):
        super().__init__(square_footage, square_footage_price)


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
