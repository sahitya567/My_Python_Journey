a=int(input("Enter your age:"))
#if statement no.1
if(a%2==0):
    print("It is even")
#End of if statement no.1

#if statement no.2
if(a>=18):
    print("You are above the age of consent")
elif(a<0):
    print("You are entering an invalid age")
elif(a==0):
    print("You are entering 0 which is an invalid age")
else:
    print("You are below the age of consent")
#End of if statement no.2
