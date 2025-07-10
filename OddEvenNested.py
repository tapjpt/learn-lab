# Prompts the user to input a number, converts it to an integer, and stores it in the variable `num`
num = int(input("Enter a number: "))

# Checks if the number is greater than zero (positive)
if num > 0:
    # If the number is positive, checks whether it is divisible by 2
    # The modulo operator (%) is used to check divisibility
    # If the remainder when dividing by 2 is 0, it is an even number
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        # If the remainder is not 0, the number is odd
        print("Positive Odd Number")

# If the number is less than zero, it is negative
elif num < 0:
    print("Negative Number")

# If the number is not greater than zero and not less than zero, it must be zero
else:
    print("Zero")