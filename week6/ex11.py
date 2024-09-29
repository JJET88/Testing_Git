import random

# Generate a random number between 1 and 9
target_number = random.randint(1, 9)

# Infinite loop to keep prompting the user until the guess is correct
while True:
    # Ask the user for a guess
    guess = input("Guess a number between 1 and 9: ")
    
    # Check if the guess is correct
    if guess.isdigit():
        if int(guess) == target_number:
            print("Well guessed!")
            break  # Exit the loop on correct guess
        else:
            # print(target_number)
            print("Try again!")
    else:
        print("Input must be number")
