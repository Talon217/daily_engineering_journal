"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


# (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

# (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


# (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the total preparation time

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.

    Returns:
        int: the preparation time of all the layers (in minutes) derived from 'PREPARATION_TIME'.

    Function that take the number of layers intended to be in the dish(int:)
    and multiplies that by the amount of time each layer takes to set up;
    giving you a grand total preperation time.
    """
    return number_of_layers * PREPARATION_TIME


# (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total time to make the dish.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): the amount of time cooked thus far.

    Returns:
        int: the total elapsed time (in minutes) derived from 'elapsed_bake_time', and 'number_of_layers'.

    Function that take the number of layers intended to be in the dish(int:)
    and multiplies that by the amount of time each layer takes to set up;
    giving you a grand total preperation time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


#  (student): Remember to go back and add docstrings to all your functions