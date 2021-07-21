import random

random_number = random.randint(0, 11)

while True:
    user_guess = int(input("Guess a random number from 0-11: "))

    if (user_guess == random_number):
        print("You guessed" ,user_guess, "and the random number is" ,random_number, "congratulations")
        break

    elif (user_guess < random_number):
        n = random_number - user_guess
        print("You did not guess the correct number, you were" ,n, "off")

    else:
        n = user_guess - random_number
        print("You did not guess the correct number, you were" ,n, "off")

