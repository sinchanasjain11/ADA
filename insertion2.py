import random
import time
def insert_sort(A):
    n=len(A)
    for i in range(1,n):
        v=A[i]
        j=i-1
        while j>=0 and A[j]>v:
            A[j+1]=A[j]
            j=j-1
        A[j+1]=v
n=[5000,6000,7000,8000,9000,10000]
sort_times=[]
for n in n:
    arr=[random.randint(1,10000) for _ in range(n)]
    s_t=time.time()
    insert_sort(arr)
    e_t=time.time()
    sort_times.append(e_t-s_t)
print(n)
print(sort_times)
      