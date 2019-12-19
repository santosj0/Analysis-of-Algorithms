import math


def find_maximum_subarray_quadratic(arr):
    """
    Brute Force method which examines each element of the array in a Θ(n^2) runtime meaning a for-loop inside of
    another for-loop. The method starts at the first index of the array, checking to see if that number is greater than
    the place holder number. Then it adds the next index and checks to see if that temporary number is greater. It
    continues to check for the length of the array. Then it moves to the next index it was previously on and does the
    same. This method will return the subset of the array where the maximum number is produced. This algorithm was
    derived from "Introduction to Algorithms - Third Edition" and modified to work with Python.
    :param arr: An array of all real numbers.
    :return: Returns the start index of the subset, the last index of the subset, and the highest number, respectively.
    """

    # Check to make sure array has at least one element
    if len(arr) < 1:
        return None

    # Starts at negative infinity since a subset is required to have at least one element for an answer.
    highest_num = -math.inf

    # Start and end of the subset
    start_index = 0
    end_index = 0

    for i in range(len(arr)):
        # Place holder for comparison
        temp_num = 0

        for j in range(i, len(arr)):
            # Adds number to the temporary number holder
            temp_num += arr[j]

            # Replaces highest number and sets the subset indexes if true
            if temp_num > highest_num:
                highest_num = temp_num
                start_index = i
                end_index = j

    return start_index, end_index, highest_num


if __name__ == "__main__":
    # Test cases
    arr1 = [1, 2, 3]                                                                # Positive Case
    arr2 = [-1, -2, -3, 4, -5, -6, -7]                                              # Negative Case
    arr3 = [8]                                                                      # Singular Case
    arr4 = [8, -1, 5, -1]                                                           # Positive/Negative Case
    arr5 = [1.3, -1.5, 4.9, -0.29]                                                  # Floats
    arr6 = [13, -3, -25, 20, -3, -16, -23, 18.0, 20, -7, 12, -5, -22, 15, -4, 7]    # Book example
    arr7 = []                                                                       # Empty case
    arr8 = [math.sqrt(2), 1, -2]                                                    # Irrational

    # Checking for validity
    assert find_maximum_subarray_quadratic(arr1) == (0, 2, 6), "Function does not work properly"
    assert find_maximum_subarray_quadratic(arr2) == (3, 3, 4), "Function does not work properly"
    assert find_maximum_subarray_quadratic(arr3) == (0, 0, 8), "Function does not work properly"
    assert find_maximum_subarray_quadratic(arr4) == (0, 2, 12), "Function does not work properly"
    assert find_maximum_subarray_quadratic(arr5) == (2, 2, 4.9), "Function does not work properly"
    assert find_maximum_subarray_quadratic(arr6) == (7, 10, 43.0), "Function does not work properly"
    assert find_maximum_subarray_quadratic(arr7) is None, "Function does not work properly"
    assert find_maximum_subarray_quadratic(arr8) == (0, 1, (math.sqrt(2) + 1)), "Function does not work properly"

    print("All tests passed.")
