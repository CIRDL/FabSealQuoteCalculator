import math

# Method toolkit for simplifying liner calculations


# Converts imperial measurements to double
def converter(feet, inches):
    total_converted = feet + (inches / 12)
    return total_converted


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
