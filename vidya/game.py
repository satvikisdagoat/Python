import random

secret_num = random.randint(1,100)

max_attempts = 3

attempts = 0

print (" Welcome to the game, Guess the number between 1 to 100")

while attempts < max_attempts:
    guess = input("Enter your Guess:")
    if  guess == secret_num:
        print (" Congrats! you guessed it right, please collect your gift")
        attempts = attempts + 1
        break
    else:
        print ("You guessed it wrong, please try again")
        attempts = attempts + 1
        if attempts == max_attempts:
            print ("game is over, the correct number is", secret_num)
