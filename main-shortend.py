import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1,0,1])
youstr = input("enter your choise :")
youDict = {"s": 1, "w": -1, "g": 0 }
reverseDict = {1:"snake" , -1:"water" , 0:"gun"}

you = youDict[youstr]

# By now we have computer and you choise in number form. Now we will find the winner.

print(f"your choise {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer == you):
    print("its a draw")
# else:
#     if(computer== -1 and you== 1):  (computer - you) -2
#         print("you win ")
#     elif(computer== -1 and you== 0):  (computer - you) -1
#         print("you lose ")
#     elif(computer== 1 and you== -1):  (computer - you) 2
#         print("you lose ")
#     elif(computer== 1 and you== 0):  (computer - you) 1
#         print("you win ")
#     elif(computer== 0 and you== -1):  (computer - you) 1
#         print("you win ")
#     elif(computer== 0 and you== 1):  (computer - you) -1
#         print("you lose ")
#     else:
#         print("someting wenr wrong" )
# use the logic of difference between computer and you choise to find the winner means (computer-you) if the difference is 0 then its a draw if the difference is -1 or 2 then you win else you lose
else:
    if((computer-you)==-2 or (computer-you)==1):
        print("you win ")
    else:
        print("you lose ")