arr =[]
n = int(input("Enter number of elements in the array: "))
for i in range(n):
    arr.append(int(input("Enter the array elements: ")))
    
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            
print("Sorted array is: ")
for i in range(n):
    print(arr[i], end=" ")                                                                                                                    