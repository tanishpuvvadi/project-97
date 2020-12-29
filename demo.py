import random
num= random.randint(1,9)
chance=1
while(chance<=3):
    choice=int(input("enter your choice"))
    if(choice==num):
        print("you won")
        break
    else:
        print("try again")
    chance = chance+1         

