import random 
chance = 0
numList = [1,2,3,4,5,6,7,8,9]
randomNum = random.choice(numList)
print(randomNum)

while chance<5:
    guess = int(input("Guess a number between 1 and 9: "))
    if guess == randomNum:
        print("Yay!You guessed the correct number!")
        break
    elif guess > randomNum:
        print("Too high :(, Try again")
    else:
        print("Too low :(, Try again")
    if not chance>5:
        print("YOU LOSE!! The number is: ",+randomNum)
    chance = chance + 1