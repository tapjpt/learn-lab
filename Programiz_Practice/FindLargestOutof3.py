try:
    # Prompts the user to enter three numbers and converts each input to a float
    # to handle both integer and decimal values.
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Checks if all three numbers are equal.
    if (num1 == num2) and (num2 == num3):
        # If all three numbers are equal, directly print the equality statement
        print("All three numbers are equal.")
    else:
        # Executes only if not all numbers are equal.
        # Nested `if-elif-else` checks the largest among the three numbers.

        # First condition: Checks if the first number is greater than or equal
        # to both the second and third numbers.
        if (num1 >= num2) and (num1 >= num3):
            # If true, assigns the first number as the largest.
            largest = num1
        # Second condition: Checks if the second number is greater than or equal
        # to both the first and third numbers.
        elif (num2 >= num1) and (num2 >= num3):
            # If true, assigns the second number as the largest.
            largest = num2
        else:
            # Default/fallback condition: If the above conditions are false,
            # the third number must be the largest.
            largest = num3

        # Prints the result, specifying the largest number.
        print(f"The largest number is {largest}")

# Handles cases where the user enters an invalid (non-numeric) input.
except ValueError:
    print("Please enter a valid numeric value.")