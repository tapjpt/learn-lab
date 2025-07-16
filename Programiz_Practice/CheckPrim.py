# Import math module to use mathematical functions like square root
import math  

# Define the number to check for primality
num = int(input("Enter a number: "))

# Initialize a flag variable
flag = False  # This will signal whether a factor is found

# Step 1: Handle special cases
# Prime numbers must be greater than 1
if num <= 1:  
    print(num, "is not a prime number")

# The number 2 is a prime number (the smallest and even prime)
elif num == 2:  
    print(num, "is a prime number")

# Step 2: Check for factors for numbers greater than 2
else:
    # Loop from 2 to the square root of the number (inclusive)
    # Explanation: We only need to check up to √num for efficiency
    for i in range(2, int(math.sqrt(num)) + 1):  
        if (num % i) == 0:  # If num is divisible by i, it's not a prime number
            flag = True  # Set flag to True since a factor is found
            break  # Exit the loop early to save computation time
    
    # Step 3: Determine and print the result based on the flag
    if flag:  
        print(num, "is not a prime number")  # If a factor was found
    else:
        print(num, "is a prime number")  # If no factors were found