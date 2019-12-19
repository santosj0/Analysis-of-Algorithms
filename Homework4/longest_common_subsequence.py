import numpy as np


def lcs_length(x, y):
    """
    Generates the b and c tables for the longest common subsequence in two character arrays.
    :param x: Array of characters
    :param y: Array of characters
    :return: Table showing direction/characters to print, different costs based on performance,
    and longest common subsequence length
    """
    # Length of each array
    m = len(x)
    n = len(y)

    # Generates empty tables
    b = np.empty([m + 1, n + 1], dtype='str')
    c = np.zeros([m + 1, n + 1])

    # Determine character location/longest value
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if x[i - 1] == y[j - 1]:
                c[i, j] = c[i - 1, j - 1] + 1
                b[i, j] = "↖"
            elif c[i - 1, j] >= c[i, j - 1]:
                c[i, j] = c[i - 1, j]
                b[i, j] = "↑"
            else:
                c[i, j] = c[i, j - 1]
                b[i, j] = "←"

    return b, c, c[m, n]


def print_lcs(b, x, i, j):
    """
    Based on the B table, display the longest common subsequence
    :param b: Table with direction to identify which characters to print
    :param x: Array of characters
    :param i: Length of the first(x) character array
    :param j: Length of the second(y) character array
    :return:
    """
    if i == 0 or j == 0:
        return

    if b[i, j] == "↖":
        print_lcs(b, x, i - 1, j - 1)
        print(x[i - 1], end=" ")
    elif b[i, j] == "↑":
        print_lcs(b, x, i - 1, j)
    else:
        print_lcs(b, x, i, j - 1)


if __name__ == "__main__":
    x = ['A', 'B', 'A', 'B', 'A']
    y = ['B', 'A', 'B', 'A', 'A']

    b, c, length = lcs_length(x, y)

    print_lcs(b, x, len(x), len(y))

    # x = ['B', 'B', 'A', 'B', 'A']
    # y = ['B', 'A', 'B', 'A', 'B']
    # b, c, length = lcs_length(x, y)
    # print(b)
    # print_lcs(b, x, len(x), len(y))

    # x = ['B', 'B', 'A', 'A', 'B', 'A']
    # y = ['B', 'A', 'A', 'B']
    # b, c, length = lcs_length(x, y)
    # print(b)
    # print_lcs(b, x, len(x), len(y))

    # x = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    # y = ['B', 'D', 'C', 'A', 'B', 'A']
    # b, c, length = lcs_length(x, y)
    # print(b)
    # print(length)
    # print_lcs(b, x, len(x), len(y))
