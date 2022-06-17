import math

# Method toolkit for simplifying liner calculations


# Converts imperial measurements to double
def converter(feet, inches):
    total_converted = feet + (inches / 12)
    return total_converted


# Converts from double to imperial measurements & returns feet
def feet_deconverter(converted_val):
    return math.floor(converted_val)


# Converts from double to imperial measurements & returns inches
def inch_deconverter(converted_val):
    return (converted_val - feet_deconverter(converted_val)) * 12


# Adds appropriate number of extra length to diameter
def diameter_modifier(diameter):
    if diameter < 15:
        diameter += converter(0, 3)
    elif diameter < 30:
        diameter += converter(0, 6)
    elif diameter < 100:
        diameter += 1
    else:
        diameter += converter(1, 6)
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
