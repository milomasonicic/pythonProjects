import random

upperrange = input("Top range: ")
random_number = random.randint(0, int(upperrange))

guesses = 0 

while True:
    guesses += 1

    guess = input("Your guess: ")
    user_guess = int(guess)

    if user_guess == random_number:
        print("Great! Your number of guesses is " + str(guesses))
        break
    elif user_guess < random_number:
        print("Your guess is smaller than the random number.")
    else:
        print("Your guess is larger than the random number.")
