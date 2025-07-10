# Python program to swap two variables



#To take inputs from the user
x = input("Enter a value of x:  ")
y = input("Enter value of y:  ")

print(f"Your values of x is {x} and y is {y}")

#create a temporary variable and swap the values
temp = x  #works as a placeholder
x = y
y = temp

print(f"The value of x after swapping: {x}")
print(f"The value of y after swapping: {y}")