n=int(input("enter any number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print(f"factorial of {n} is {fact}")