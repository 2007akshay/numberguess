import random

number = random.randint(1,9)
print('guess any number between 1 & 9')

chance=0

while chance<5 :
        
        guess=int(input('enter your guess  :'))
        if guess==number:
                print("congratulation u won")
                break
        elif guess<number:
                print("enter a number greater number ")
        else: 
                print("enter lowere number")
        chance+=1

if chance == 5:
    print("you lost the game, number is",number)