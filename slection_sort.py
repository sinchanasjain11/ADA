
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = []
n = int(input("Enter number of elements in the array: "))
for i in range(n):
    arr.append(int(input("Enter the array elements: ")))
sorted_arr = selection_sort(arr)
print("Sorted array is:", sorted_arr)
