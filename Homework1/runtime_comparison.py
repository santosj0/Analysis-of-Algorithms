
from Homework1.brute_force_method import find_maximum_subarray_quadratic as fmsq
from Homework1.linear_method import find_maximum_subarray_linear as fmsl
from Homework1.recursive_method import find_maximum_subarray_recurrsive as fmsr
import numpy as np
from sys import argv
from time import time
from matplotlib import pyplot as plt

"""
OVERVIEW:
This script will display the difference in runtime of three different algorithms for find the maximum subarray within an
array. The graph will show that the brute force method takes vastly more time than the recursive and linear method.
Due to time constraint, the array size defaults at 1000. However, the array size can be changed if passed with an
argument in the command line. Also, by default, this script only compares brute-force method with linear method. Pass
true flag as second argument to get
"""

# Sets the array size
size = 1000
if len(argv) > 1:
    size = int(argv[1])


# Containers for runtimes
fmsq_runtime = []   # Brute Force
fmsl_runtime = []   # Linear

# Flag true for recursive
if len(argv) > 2:
    if argv[2] == "true":
        fmsr_runtime = []   # Recursive

for i in range(0, size):
    # Random int array which increased its size based on i
    arr = np.random.randint(-1000000, 1000000, (1, i+1))[0]

    # Brute Force
    fmsq_start_time = time()
    fmsq(arr)
    fmsq_runtime.append(time() - fmsq_start_time)

    # Linear
    fmsl_start_time = time()
    fmsl(arr)
    fmsl_runtime.append(time() - fmsl_start_time)

    # Recursive
    if len(argv) > 2:
        if argv[2] == "true":
            fmsr_start_time = time()
            fmsr(arr, 0, len(arr) - 1)
            fmsr_runtime.append(time() - fmsr_start_time)


# Displays the graph
plt.style.use("dark_background")
plt.plot(fmsq_runtime, label="Brute Force")
plt.plot(fmsl_runtime, label="Linear")

if len(argv) > 2:
    if argv[2] == "true":
        plt.plot(fmsr_runtime, label="Recursive")

legend = plt.legend(loc="upper left")
plt.setp(legend.get_texts(), color="lime")
plt.xlabel('Array Size')
plt.ylabel('Runtime(sec)')
plt.title("Brute Force vs. Linear")
plt.show()
