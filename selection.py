import random
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

n=5000
arr=[random.randint(1,10000) for _ in range(n)]
selection_sort(arr)
print("Sorted array is:", arr)
