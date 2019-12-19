import numpy as np
import math


def minimum(insert, delete, replace_copy, twiddle):
    """
    Determines the lowest value between the parameters
    :param insert: Integer value of insert
    :param delete: Integer value of delete
    :param replace_copy:  Integer value of replace or copy
    :param twiddle:  Integer value of twiddle
    :return: Lowest value between the parameters and its corresponding character
    """
    if replace_copy <= insert and replace_copy <= twiddle and replace_copy <= delete:
        return replace_copy, "rc"

    elif twiddle <= insert and twiddle <= delete:
        return twiddle, "t"

    elif insert <= delete:
        return insert, "i"

    else:
        return delete, "d"


def string_edit_cost_location(str1, str2, cpc=0, rpc=1, insc=1, delc=1, twidc=1):
    """
    Determines the cost of changing one string into another as well as what to do with it
    :param str1: String to be evaluated
    :param str2: Target String
    :param cpc: Cost of copying two characters (Defaults: 0)
    :param rpc: Cost of replacing a character (Defaults: 1)
    :param insc: Cost of inserting a character (Defaults: 1)
    :param delc: Cost of deleting a character (Defaults: 1)
    :param twidc: Cost of switching two characters (Defaults: 1)
    :return: Table of costs, Table of functions, Lowest cost
    """
    # Ignores case-sensitivity
    x = str1.lower()
    y = str2.lower()

    # Build the tables
    m = len(x)
    n = len(y)
    b = np.empty([m + 1, n + 1], dtype='str')
    c = np.zeros([m + 1, n + 1])
    for i in range(0, m + 1):
        c[i, 0] = i
        b[i, 0] = 'd'
    for j in range(0, n + 1):
        c[0, j] = j
        b[0, j] = 'i'
    b[0, 0] = ''

    # Determine costs
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Copy
            if x[i - 1] == y[j - 1]:
                cprp = cpc
                c_or_r = 'c'

            # Replace
            else:
                cprp = rpc
                c_or_r = 'r'

            c[i, j], val = minimum(c[i, j - 1] + insc,                                      # Insert
                                   c[i - 1, j] + delc,                                      # Delete
                                   c[i - 1, j - 1] + cprp,                                  # Copy/Replace
                                   c[i - 2, j - 2] + twidc if i >= 2 and j >= 2             # Twiddle
                                                              and x[i - 2] == y[j - 1]
                                                              and x[i - 1] == y[j - 2]
                                                           else math.inf)

            # Add to B Table
            if val == "rc":
                b[i, j] = c_or_r
            else:
                b[i, j] = val

    return c, b, c[m, n]


def print_string_edit(b, i, j):
    """
    Displays the functions needed to change evaluated string with target string
    :param b: Table of functional path
    :param i: Length of evaluated string
    :param j: Length of target string
    :return: None
    """
    # Base Case
    if i == 0 and j == 0:
        return

    # Copy or Repeat
    if b[i, j] in {'c', 'r'}:
        print_string_edit(b, i - 1, j - 1)
        print(b[i, j], end='')

    # Twiddle
    elif b[i, j] == 't':
        print_string_edit(b, i - 2, j - 2)
        print(b[i, j], end='')

    # Insert
    elif b[i, j] == 'i':
        print_string_edit(b, i, j - 1)
        print(b[i, j], end='')

    # Delete
    else:
        print_string_edit(b, i - 1, j)
        print(b[i, j], end='')


def print_string_edit_w_cost(x, y, cpc=0, rpc=1, insc=1, delc=1, twidc=1):
    """
    Displays evaluated string, target string, functions to get eval to target, and the total cost
    :param x: Evaluated String
    :param y: Target String
    :param cpc: Cost for copy
    :param rpc: Cost for replace
    :param insc: Cost for insert
    :param delc: Cost for delete
    :param twidc: Cost for twiddle
    :return: None
    """
    # Retrieve cost, function order, and lowest cost
    c, b, low = string_edit_cost_location(x, y, cpc=cpc, rpc=rpc, insc=insc, delc=delc, twidc=twidc)

    # Output
    print(x)                                # Display evaluated string
    print(y)                                # Display target string
    print_string_edit(b, len(x), len(y))    # Display function order
    print(' -', low)                        # Display lowest cost


if __name__ == "__main__":
    y = "ADD"
    x = "ADV"
    print_string_edit_w_cost(x, y, cpc=5, rpc=5)
