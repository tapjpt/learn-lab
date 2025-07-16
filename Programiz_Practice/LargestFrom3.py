# Python program to find the largest number among the three

try:
    # Getting input inside the try block
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    
    # Comparing the numbers to find the largest
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3
    
    print(f"The largest number is {largest}")

# Handles cases where the user enters an invalid (non-numeric) input
except ValueError:
    print("Please enter a valid numeric value.")