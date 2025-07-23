def c_to_f(c):
    return ((9/5)*c)+32 

c=int(input("enter temperature in celcius:"))
f=c_to_f(c)
print(f"{round(f,2)}°F")
