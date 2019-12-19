import math


def find_maximum_subarray_linear(arr):
    """
    Linear method to determing the maximum subarray in an array with an overall runtime of Θ(n) which means a single
    for-loop. The method starts by taking the first index of the array as the maximum value. Next, it will take this
    value(a) and adds the next index's value(b) to the current value to get a new value(c). It then compares the new
    value(c) with the value in the next index(b) and determines which is greater. If the new value(c) is greater, then
    it replaces the current maximum value(a) with that new value(c). This process continues either until the loop
    finished, or if the new value(c) is less than the value of the next index(b). If the latter occurs, the maximum
    value(a) is replaced by the next index's value(b) and the process continues. This algorithm was derived from
    "Introduction to Algorithms - Third Edition" and modified to work with Python.
    :param arr: An array of all real numbers.
    :return: Returns the start index of the subset, the last index of the subset, and the highest number, respectively.
    """

    # Check to make sure array has at least one element
    if len(arr) < 1:
        return None

    max_ending = arr[0]     # Comparator of next index plus current
    max_so_far = arr[0]     # Place holder for maximum number overall
    start = 0               # Starting index of the subarray
    end = 0                 # Last index of the subarray
    temp_start = 0          # Place holder for starting index
    temp_end = 0            # Place holder of last index

    for i in range(1, len(arr)):
        # Sets the temporary values based on maximum chain/reset of chain
        if max_ending + arr[i] > arr[i]:
            max_ending += arr[i]
            temp_end = i
        else:
            max_ending = arr[i]
            temp_start = i
            temp_end = i

        # Updates non-temporary positions/values
        if max_so_far < max_ending:
            max_so_far = max_ending
            start = temp_start
            end = temp_end

    return start, end, max_so_far


if __name__ == "__main__":
    # Test cases
    arr1 = [1, 2, 3]  # Positive Case
    arr2 = [-1, -2, -3, 4, -5, -6, -7]  # Negative Case
    arr3 = [8]  # Singular Case
    arr4 = [8, -1, 5, -1]  # Positive/Negative Case
    arr5 = [1.3, -1.5, 4.9, -0.29]  # Floats
    arr6 = [13, -3, -25, 20, -3, -16, -23, 18.0, 20, -7, 12, -5, -22, 15, -4, 7]  # Book example
    arr7 = []  # Empty case
    arr8 = [math.sqrt(2), 1, -2]  # Irrational

    # Checking for validity
    assert find_maximum_subarray_linear(arr1) == (0, 2, 6), "Function does not work properly"
    assert find_maximum_subarray_linear(arr2) == (3, 3, 4), "Function does not work properly"
    assert find_maximum_subarray_linear(arr3) == (0, 0, 8), "Function does not work properly"
    assert find_maximum_subarray_linear(arr4) == (0, 2, 12), "Function does not work properly"
    assert find_maximum_subarray_linear(arr5) == (2, 2, 4.9), "Function does not work properly"
    assert find_maximum_subarray_linear(arr6) == (7, 10, 43.0), "Function does not work properly"
    assert find_maximum_subarray_linear(arr7) is None, "Function does not work properly"
    assert find_maximum_subarray_linear(arr8) == (0, 1, (math.sqrt(2) + 1)), "Function does not work properly"

    print("All tests passed.")