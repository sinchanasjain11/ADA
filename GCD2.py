def gcd(a,b):
    t=min(a,b)
    while t>0:
        if a%t==0 and b%t==0:
            return t
        t=t-1
    
print(gcd(14,12))