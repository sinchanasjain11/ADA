import random
import time
import matplotlib.pyplot as plt

def insert_sort(A):
    for i in range(1, len(A)):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v

sizes = [5000, 6000, 7000, 8000, 9000, 10000]
times = []

for s in sizes:
    arr = [random.randint(1, 10000) for _ in range(s)]
    start = time.time()
    insert_sort(arr)
    end = time.time()
    times.append(end - start)

print(sizes)
print(times)

plt.plot(sizes, times)
plt.show()
