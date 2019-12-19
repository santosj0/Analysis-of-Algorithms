import numpy


def process_unit_length(arr):
    """
    Removes all numbers within a unit length of the previous number
    :param arr: Array of floats
    :return: Array of floats that do not have any number within a unit length of the previous number
    """
    # Generates arrays
    d = [arr[0]]
    k = arr[0] + 1

    # Removes integers a unit length from the previous number
    for i in range(1, len(arr)):
        if arr[i] > k:
            k = arr[i] + 1
            d.append(arr[i])

    return d, len(d)


if __name__ == "__main__":
    z = numpy.sort(numpy.around(numpy.random.random(50) * 10, decimals=1))
    a, b = process_unit_length(z)
    print(z)
    print(a)
    print(b)
