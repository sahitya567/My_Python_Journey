def rem(l,word):
    n=[]
    for item in l:
        n.append(item.strip(word))
    return n
l=["Sairam","Rohan","Vishnu","an"]
print(rem(l,"an"))