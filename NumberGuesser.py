import random

user_guess = int(input("Guess the random number: "))
random_number = random.randint(0, 11)

if (user_guess == random_number):
    print("You guessed " +str(user_guess)+ " and the random number is " +str(random_number)+ " congratulations")

elif (user_guess < random_number):
    n = random_number - user_guess
    print("You did not guess the correct number, you were " +str(n)+ " off")

else:
    n = user_guess - random_number
    print("You did not guess the correct number, you were " +str(n)+ " off")

print(random_number)
