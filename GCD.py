a=int(input("enter A"))
b=int(input("enter B"))
while b!=0:
    a,b=b,a%b
print("GCD ",a)
