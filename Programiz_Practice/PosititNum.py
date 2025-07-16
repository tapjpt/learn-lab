# Python Program to calculate the square root

#Note: change this value for a different result

import cmath
#imports the complex math module 
#can now take the square root of a neg number

num= float(input("Input a positive number: "))

num_sqrt = num**0.5

print("The square root of %.3f is %.3f"%(num, num_sqrt))

print("Do you want to take a square root of a negative number?")

num = float(input("Input a negative number and see: "))

num_sqrt = cmath.sqrt(num)
print("The square root of {:.3f} is {:.3}j".format(num, num_sqrt))

