import math


def floor_circular_tank_sq_footage(diameter):
    return round(diameter ** 2)


def wall_circular_tank_sq_footage(diameter, depth):
    circumference = diameter * math.pi
    return round(circumference * depth)


# Calculates square footage of a circular liner
def circular_tank_sq_footage(diameter, depth):

    # Floor square footage
    floor = floor_circular_tank_sq_footage(diameter)
    print("Bottom square footage: {:,} ft.".format(floor))

    # Side Wall square footage
    side_wall = wall_circular_tank_sq_footage(diameter, depth)
    print("Side wall square footage: {:,} ft.".format(side_wall))

    # Total square footage
    sqft_total = side_wall + floor
    print("Total tank square footage: {:,} ft.".format(sqft_total))
    return sqft_total


# Calculates the weight of a circular tanked liner
def circular_weight(diameter, depth, material_weight):

    # Weight of the wall
    circumference = diameter * math.pi
    wall_sqft = circumference * depth
    wall_weight = wall_sqft * material_weight

    # Weight of the floor
    floor_sqft = diameter ** 2
    floor_weight = floor_sqft * material_weight

    # Total weight of the liner
    total_weight = math.ceil(floor_weight + wall_weight)
    return total_weight


def floor_rectangular_tank_sq_footage(length, width):
    return round(length * width)


def wall_rectangular_tank_sq_footage(length, width, depth):
    return round((length + width) * 2 * depth)


# Calculates the square footage of a rectangular tank
def rectangular_tank_sq_footage(length, width, depth):

    # Calculates the square footage of the bottom
    bottom_sqft = floor_rectangular_tank_sq_footage(length, width)
    print('Bottom square footage: {:,} ft.'.format(bottom_sqft))

    # Calculates the square footage of the sidewalls
    sidewall_sqft = wall_rectangular_tank_sq_footage(length, width, depth)
    print('Side wall square footage: {:,} ft.'.format(sidewall_sqft))

    # Calculates and returns the total square footage
    sqft_total = sidewall_sqft + bottom_sqft
    print("Total tank square footage: {:,} ft.".format(sqft_total))
    return sqft_total


# Calculates the weight of a rectangular tanked liner
def rectangular_weight(length, width, depth, material_weight):

    # Weight of the wall
    wall_sqft = (length * depth * 2) + (width * depth * 2)
    wall_weight = wall_sqft * material_weight

    # Weight of the floor
    floor_sqft = length * width
    floor_weight = floor_sqft * material_weight

    # Total weight of the liner
    total_weight = math.ceil(floor_weight + wall_weight)
    return total_weight


# Adds appropriate number of extra length to diameter
def diameter_modifier(diameter):

    if diameter < 16:
        diameter += converter(0, 3)

    elif diameter < 31:
        diameter += converter(0, 6)

    else:
        diameter += 1

    return diameter


# Adds appropriate number of extra material to length
def length_modifier(length):

    if length < 16:
        length += converter(0, 3)
    elif length < 31:
        length += converter(0, 6)
    elif length < 101:
        length += converter(1, 0)
    else:
        length += converter(0, 18)

    return length


# Converts imperial measurements to double
def converter(feet, inches):

    total_converted = feet + (inches / 12)
    return total_converted

