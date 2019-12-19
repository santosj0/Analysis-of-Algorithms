import random

from Homework2.quicksort import randomized_partition_normal as rpn
from Practice.sorts.merge_sort import merge_sort


def randomized_select(arr, start, end, position):
    """
    Algorithm modified from "Introductions to Algorithms, Third Edition." This algorithm will recursively return the
    smallest number based on the position. For example, if 2 was passed into the position parameter, the function
    will return the second smallest number.
    :param arr: Array of all real numbers
    :param start: Starting index of the array
    :param end: Final index of the array
    :param position: Smallest number you wish to return
    :return: An integer of the smallest number based on its position in the array
    """
    if start == end:
        return arr[start]
    pivot = rpn(arr, start, end)
    k = pivot - start + 1
    if position == k:
        return arr[pivot]
    elif position < k:
        return randomized_select(arr, start, pivot - 1, position)
    else:
        return randomized_select(arr, pivot + 1, end, position - k)


def sorted_select(arr, start, end, position):
    """
    Uses merge-sort to sort the array to return the position based on index
    :param arr: Array of all real numbers
    :param start: Starting index
    :param end: Final index
    :param position: Smallest number you wish to return
    :return: An integer of the smallest number based on its position in the array
    """
    merge_sort(arr, start, end)

    return arr[position - 1]


if __name__ == "__main__":
    # Test Cases
    test_cases = [
        [8, 2, 4, 1, 6, 7, 3, 5, 9],            # Normal Case
        [-1, -5, -3, -2, -6, -4, -7, -9, -8],   # Negative Case
        [8, 5, 9, 5, 0, 5, 3, 5],               # Similar Case
        [1, 2, 3, 4, 5, 6, 7, 8, 9]             # Sorted Case
    ]

    # Answers
    answers = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [-9, -8, -7, -6, -5, -4, -3, -2, -1],
        [0, 3, 5, 5, 5, 5, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]

    # Randomized Select Test
    for test_case, answer in zip(test_cases, answers):
        for i in range(len(answer) - 1):
            assert randomized_select(test_case, 0, len(test_case) - 1, i + 1) == answer[i], "Randomized Select does " \
                                                                                            "not work properly."

    for test_case in test_cases:
        random.shuffle(test_case)

    # Sorted Select Test
    for test_case, answer in zip(test_cases, answers):
        for i in range(len(answer) - 1):
            assert sorted_select(test_case, 0, len(test_case) - 1, i + 1) == answer[i], "Sorted Select does not " \
                                                                                        "work properly."

    print("All tests passed")
