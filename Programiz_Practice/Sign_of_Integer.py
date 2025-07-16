# This script determines if a number is positive, negative, or zero.
# It also handles cases where the user provides invalid input.

try:
    # Prompts the user to enter a number
    num = float(input("Enter a number: "))

    # Checks the number's value
    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")
except ValueError:
    # Handles non-numeric input
    print("Invalid input. Please enter a numeric value.")
