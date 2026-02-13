import random
import time
import matplotlib.pyplot as plt

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
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
plt.title("Quick Sort Time Complexity")
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.show()
