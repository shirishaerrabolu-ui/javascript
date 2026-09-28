import random

print("==============================")
print("     NUMBER GUESSING GAME")
print("==============================")

secret_number = random.randint(1, 100)
attempts = 0

print("I have chosen a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("\nCongratulations! You guessed it!")
        print("The number was:", secret_number)
        print("Number of attempts:", attempts)
        break