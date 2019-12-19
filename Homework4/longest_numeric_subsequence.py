import numpy as np


def longest_increasing_subsequence(a):
    """
    Determines the longest subsequence in an array of integers
    :param a: Array of integers
    :return: Array of indexes for where the longest increasing subsequence is location in the array(a),
    the length of the subsequence, and the final index position of the subsequence
    """
    # Sets up the arrays
    n = len(a)
    d = np.zeros(n)
    p = np.zeros(n)
    d[0] = 1
    p[0] = 0

    # Marks the location of each integer in the subsequence
    for i in range(1, n):
        d[i] = 1
        p[i] = 0
        for j in range(i - 1, -1, -1):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                p[i] = j

    # Determines the length of the subsequence/Provides the final index of the longest subsequence
    k = 0
    for i in range(1, n + 1):
        if d[i - 1] > k:
            k = d[i - 1]
            t = i - 1

    return p, k, t


def print_subsequence(array, position, length, start):
    """
    Displays the longest increasing subsequence
    :param array: Array of integers
    :param position: Array of indexes based on the array of integers
    :param length: Integer representing the length of the subsequence
    :param start: Index of the last number in the subsequence
    :return:
    """
    if length == 0:
        return

    print_subsequence(array, position, length - 1, int(position[start]))
    print(array[start], end=' ')


if __name__ == "__main__":
    arr = [42, 45, 23, 90, 3, 99, 108, 76, 12, 77, 16, 18, 4]

    a, b, c = longest_increasing_subsequence(arr)
    print_subsequence(arr, a, b, c)
