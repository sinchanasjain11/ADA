import random
import time
import matplotlib.pyplot as plt


def partition_hoare(arr, low, high):
    pivot = arr[low]   
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr, low, high):
    if low < high:
        pi = partition_hoare(arr, low, high)
        quick_sort(arr, low, pi)
        quick_sort(arr, pi + 1, high)


sizes = [5000, 6000, 7000, 8000, 9000, 10000]
times = []

for s in sizes:
    arr = [random.randint(1, 10000) for _ in range(s)]
    start = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    end = time.time()
    times.append(end - start)

print("Sizes:", sizes)
print("Times:", times)



plt.figure(figsize=(8, 5))
plt.plot(sizes, times, marker='o', linestyle='-', color='blue')
plt.title("Quick Sort Time Complexity (Hoare Partition)")
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.show()
