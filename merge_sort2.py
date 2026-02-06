import random
import time
import matplotlib.pyplot as plt

def merge_sort(a):
    
    n=len(a)
    if (n>1):
        b=a[0:n//2]
        c=a[n//2:n]
        print(b,"|",c)
        merge_sort(b)
        merge_sort(c)
        merge(a,b,c)
def merge(a,b,c):
    n1=len(b)
    n2=len(c)
    i=j=k=0
    while (i<n1 and j<n2):
        if (b[i]<c[j]):
            a[k]=b[i]
            i+=1
        else:
            a[k]=c[j]
            j+=1
        k+=1
    while (i<n1):
        a[k]=b[i]
        i+=1
        k+=1
    while (j<n2):
        a[k]=c[j]
        j+=1
        k+=1
    print(a)
sizes = [5000, 6000, 7000, 8000, 9000, 10000]
times = []
for s in sizes:
    arr = [random.randint(1, 10000) for _ in range(s)]
    start = time.time()
    merge_sort(arr)
    end = time.time()
    times.append(end - start)
print(sizes)
print(times)
plt.plot(sizes, times)
plt.show()