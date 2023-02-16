import random
import CONSTANTS

def get_color_change():
    """ Function to get the color each square should change to.
    Args:
        None

    Returns:
        array: contains shuffled RGB color code to assign to each square in main.py
    """
    colors = [CONSTANTS.GREEN, CONSTANTS.RED]
    random.shuffle(colors)

    return colors
