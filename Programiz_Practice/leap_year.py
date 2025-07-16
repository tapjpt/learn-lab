# Leap Year Checker Program

# Checks for exceptions to handle invalid input gracefully
try:
    # Takes user input for the year and converts it to an integer
    year = int(input("Enter a year: "))

    # Checks if the year is a century year (divisible by 100) AND also divisible by 400
    # Century years (e.g., 1900, 2000) are only leap years if divisible by 400
    if (year % 400 == 0) and (year % 100 == 0):
        print(f"{year} is a leap year")

    # Checks if the year is not a century year AND divisible by 4
    # Non-century years (e.g., 2024, 2028) are leap years if divisible by 4
    elif (year % 4 == 0) and (year % 100 != 0):
        print(f"{year} is a leap year.")

    # If neither of the above conditions is true, the year is not a leap year
    else:
        print(f"{year} is not a leap year.")

# Catches cases where the user enters a non-numeric input (e.g., text)
except ValueError:
    print("Please enter a valid numeric value.")
