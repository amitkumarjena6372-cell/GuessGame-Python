import random

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 50.")

# Generate a random number
number_to_guess = random.randint(1, 50)
attempts = 0

while True:
    guess = input("Take a guess: ")
    
    # Check if input is a number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congrats! You guessed it in {attempts} attempts.")
        break
