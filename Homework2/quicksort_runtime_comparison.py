import Homework2.quicksort as qs
import numpy as np
from sys import argv
from time import time
from matplotlib import pyplot as plt

"""
OVERVIEW:
This script will display the difference in runtime between four different quicksort algorithms. 
"""

# Sets the array size
size = 1000
if len(argv) > 1:
    size = int(argv[1])

# Containers for the runtimes
qsn = []        # quicksort_normal
qsp = []        # quicksort_prime
rqsn = []       # randomized_quicksort_normal
rqsp = []       # randomized_quicksort_prime

for i in range(0, size):
    # Random int array which increased its size based on i
    arr = np.random.randint(-1000000, 1000000, (1, i + 1))[0]

    # Quicksort_normal
    qsn_start_time = time()
    qs.quicksort_algorithm_normal(np.copy(arr), 0, arr.size - 1)
    qsn.append(time() - qsn_start_time)

    # quicksort_prime
    qsp_start_time = time()
    qs.quicksort_algorithm_prime(np.copy(arr), 0, arr.size - 1)
    qsp.append(time() - qsp_start_time)

    # randomized_quicksort_normal
    rqsn_start_time = time()
    qs.randomized_quicksort_normal(np.copy(arr), 0, arr.size - 1)
    rqsn.append(time() - rqsn_start_time)

    # randomized_quicksort_prime
    rqsp_start_time = time()
    qs.randomized_quicksort_prime(np.copy(arr), 0, arr.size - 1)
    rqsp.append(time() - rqsp_start_time)

# Graph for QS Normal vs. QS Prime
plt.style.use("dark_background")
plt.plot(qsn, label="QS Normal")
plt.plot(qsp, label="QS Prime")
legend = plt.legend(loc="upper left")
plt.setp(legend.get_texts(), color="lime")
plt.xlabel('Array Size')
plt.ylabel('Runtime(sec)')
plt.title("QS Normal Vs. QS Prime")
plt.show()

# Graph for RQS Normal vs. RQS Prime
plt.style.use("dark_background")
plt.plot(rqsn, label="RQS Normal")
plt.plot(rqsp, label="RQS Prime")
legend = plt.legend(loc="upper left")
plt.setp(legend.get_texts(), color="lime")
plt.xlabel('Array Size')
plt.ylabel('Runtime(sec)')
plt.title("RQS Normal Vs. RQS Prime")
plt.show()

# Graph for all quicksort comparitors
plt.style.use("dark_background")
plt.plot(qsn, label="QS Normal")
plt.plot(qsp, label="QS Prime")
plt.plot(rqsn, label="RQS Normal")
plt.plot(rqsp, label="RQS Prime")
legend = plt.legend(loc="upper left")
plt.setp(legend.get_texts(), color="lime")
plt.xlabel('Array Size')
plt.ylabel('Runtime(sec)')
plt.title("All Quicksort Versions")
plt.show()
