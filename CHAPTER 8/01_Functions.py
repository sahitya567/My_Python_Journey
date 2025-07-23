'''
1st time

a=int(input("enter a number))
b=int(input("enter a number))
c=int(input("enter a number))
average=(a+b+c)/3
print(average)

2nd time

a=int(input("enter a number))
b=int(input("enter a number))
c=int(input("enter a number))
average=(a+b+c)/3
print(average)
'''
#but we can do many times like this using def keyword

# Function definition:
def avg():
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    c=int(input("enter a number:"))
    average=(a+b+c)/3
    print(average)

avg() #function call
avg()
avg()
