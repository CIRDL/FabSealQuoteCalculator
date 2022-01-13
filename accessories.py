import math


def geo_cost_circular(wall_material_type, sidewall_sqft, bottom_sqft):

    if wall_material_type == 16:
        wall_material_cost = 0.72
    else:
        wall_material_cost = 0.49

    floor_material_cost = 0.72
    #
    # # Sidewall square footage
    # circumference = diameter * math.pi
    # sidewall_sqft = round(circumference * depth)
    #
    # # Bottom square footage
    # bottom_sqft = round(diameter ** 2)

    # Calculate cost
    total_cost = (sidewall_sqft * wall_material_cost) + (bottom_sqft * floor_material_cost)
    return total_cost


def geo_weight_circular(wall_material_type, diameter, depth):

    if wall_material_type == 16:
        wall_material_weight = 0.10
    else:
        wall_material_weight = 0.08

    floor_material_weight = 0.10

    # Sidewall square footage
    circumference = diameter * math.pi
    sidewall_sqft = round(circumference * depth)

    # Bottom square footage
    bottom_sqft = round(diameter ** 2)

    # Calculate weight
    total_weight = (wall_material_weight + sidewall_sqft) + (floor_material_weight * bottom_sqft)
    return math.ceil(total_weight)


def geo_cost_rectangular(wall_material_type, sidewall_sqft, bottom_sqft):

    if wall_material_type == 16:
        wall_material_cost = 0.72
    else:
        wall_material_cost = 0.49

    floor_material_cost = 0.72

    # # Sidewall square footage
    # sidewall_sqft = round((length + width) * 2 * depth)

    # # Bottom square footage
    # bottom_sqft = round(length * width)

    # Calculate cost
    total_cost = (sidewall_sqft * wall_material_cost) + (bottom_sqft * floor_material_cost)
    return total_cost


def geo_weight_rectangular(wall_material_type, length, width, depth):

    if wall_material_type == 16:
        wall_material_weight = 0.10
    else:
        wall_material_weight = 0.08

    floor_material_weight = 0.10

    # Sidewall square footage
    sidewall_sqft = round((length + width) * 2 * depth)

    # Bottom square footage
    bottom_sqft = round(length * width)

    # Calculate weight
    total_weight = (wall_material_weight * sidewall_sqft) + (floor_material_weight * bottom_sqft)
    return math.ceil(total_weight)


def geo_cost_flatsheet(material_type, length, width):

    if material_type == 16:
        material_cost = 0.72
    else:
        material_cost = 0.49

    total_sqft = round(length * width)

    total_cost = (total_sqft * material_cost)
    return total_cost


def geo_weight_flatsheet(material_type, length, width):

    if material_type == 16:
        material_weight = 0.10
    else:
        material_weight = 0.08

    total_sqft = round(length * width)

    total_weight = total_sqft * material_weight
    return math.ceil(total_weight)


# Finds and allocates weight of the crate
def find_crate_weight(size):

    if size[0] == "b":
        crate_weight = 510

    elif size[0] == "s":
        crate_weight = 140

    else:
        crate_weight = 0

    return crate_weight


# Sorts into boot size
# Double check edge cases
def find_boot_price(boot_size_inches):

    if 2.0 <= boot_size_inches <= 4.0:
        boot_price = 125
    elif 4.1 <= boot_size_inches <= 8.0:
        boot_price = 150
    else:
        boot_price = 200

    return boot_price


def calc_installation_price(distance):

    employee_price = 750

    if distance < 30:
        number_employees = 5
        number_days = 3
    elif distance < 50:
        number_employees = 5
        number_days = 4
    elif distance < 70:
        number_employees = 5
        number_days = 5
    elif distance < 90:
        number_employees = 5
        number_days = 6
    elif distance < 110:
        number_employees = 6
        number_days = 6
    elif distance < 130:
        number_employees = 6
        number_days = 7
    elif distance < 150:
        number_employees = 6
        number_days = 8
    else:
        number_employees = 0
        number_days = 0

    installation_cost = (employee_price * number_employees) * number_days
    return installation_cost

