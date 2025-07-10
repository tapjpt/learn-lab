
import random

# Prompt the user to guess a number and convert the input to an integer
your_guess = int(input("Guess a number I'm thinking from 0 thru 9   "))

# Generate a random integer between 0 and 9
random_number = random.randint(0, 9)

# Compare the user's guess with the random number
if your_guess == random_number:
    print("GOOD GUESS")
else:
    print("WRONG! Better luck next time")

# Display the user's guess and the random number
print(f"You guessed {your_guess}, I was thinking {random_number}")