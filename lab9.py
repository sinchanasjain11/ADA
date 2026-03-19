""" Design and implement C/JAVA/Python Program to sort a given set of n integer 
elements using Selection Sort method and compute its time complexity. Run the 
program for varied values of n> 5000 and record the time taken to sort. Plot a graph 
of the time taken versus n. The elements can be read from a file or can be generated 
using the random number generator. """
import random
import time
import matplotlib.pyplot as plt

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


n_values = [5000, 7000, 9000, 11000, 13000]
time_taken = []

for n in n_values:
    arr = [random.randint(1, 100000) for _ in range(n)]
    
    start_time = time.time()
    selection_sort(arr)
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    time_taken.append(elapsed_time)
    
    print(f"n = {n}, Time Taken = {elapsed_time:.4f} seconds")


plt.plot(n_values, time_taken, marker='o')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Selection Sort: Time Complexity Analysis")
plt.grid(True)
# Save the plot
plt.savefig("selection_sort_time_complexity.png", dpi=300, bbox_inches='tight')
plt.show()
