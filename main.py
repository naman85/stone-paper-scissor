
# stone paper scissor project 

import random 

'''

-1 for stone
0 for paper
1 for cissor

'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"c": 1, "s": -1, "p": 0}
reversDict = {1: "cissor", -1: "stone", 0: "paper"}

you = youDict[youstr]

print(f"You chose {reversDict[you]}\nComputer chose {reversDict[computer]}")

if(computer == you):
    print("Its a draw")


if(computer == -1 and you == 1):
    print("You lose!")

elif(computer == -1 and you == 0):
    print("You win!")

elif(computer == 1 and you == -1):
    print("You win!")    

elif(computer == 1 and you == 0):
    print("You lose!")    

elif (computer == 0 and you ==-1):
    print("You lose!")

elif(computer == 0 and you == 1):
    print("You win!")

else:
    print("something went wrong")