def merge_sort(arr):
    if len(arr) <= 1:
        return arr  
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]
    L = merge_sort(L)
    R = merge_sort(R)
    i = j = 0
    result = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1
    result.extend(L[i:])
    result.extend(R[j:])
    return result

arr = [1,44,23,5,6,7,8,9]
sorted_arr = merge_sort(arr)
print("Sorted array is:", sorted_arr)