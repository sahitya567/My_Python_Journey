'''
1 for snake
-1 for water
0 for gun
'''
import random
computer = random.choice([-1,0,1])
youStr=input("enter your choice:")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:"water",0:"gun"}
you=youDict[youStr]

# By now we have 2 members, you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer==you):
    print("Draw")

else:
    if(computer==1 and you==-1):
        print("You lose!")
    elif(computer==1 and you==0):
        print("you win!")

    elif(computer==-1 and you==1):
        print("You win!")
    elif(computer==-1 and you==0):
        print("you lose!")

    elif(computer==0 and you==1):
        print("You lose!")
    elif(computer==0 and you==-1):
        print("you win!")

    else:
        print("Something went wrong!")
