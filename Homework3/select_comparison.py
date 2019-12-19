import Homework3.random_select as rs
import numpy as np
from sys import argv
from time import time
from matplotlib import pyplot as plt
from statistics import mean

"""
OVERVIEW:
This script will display the difference in runtime between the two different select algorithms. 
"""

# Sets the array size
size = 1000
if len(argv) > 1:
    size = int(argv[1])

# Containers for the runtimes
rsr = []
ssr = []

for i in range(0, size):
    # Random int array which increased its size based on i
    arr = np.random.randint(-1000000, 1000000, (1, i + 1))[0]

    # Randomized Select
    rsr_start_time = time()
    rs.randomized_select(np.copy(arr), 0, arr.size - 1, 1)
    rsr.append(time() - rsr_start_time)

    # Sorted Select
    ssr_start_time = time()
    rs.sorted_select(np.copy(arr), 0, arr.size - 1, 1)
    ssr.append(time() - ssr_start_time)

# Displays the average time
print("Randomized Select Average:", mean(rsr))
print("Sorted Select Average:", mean(ssr))

# Graph for Randomized Select vs. Sorted Select
plt.style.use("dark_background")
plt.plot(ssr, 'bo', label="Sorted Select")
plt.plot(rsr, 'rx', label="Randomized Select")
legend = plt.legend(loc="upper left")
plt.setp(legend.get_texts(), color="lime")
plt.xlabel('Array Size')
plt.ylabel('Runtime(sec)')
plt.title("Randomized Select vs. Sorted Select")
plt.show()
