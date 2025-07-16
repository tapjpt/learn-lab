#Python program to check if the input number is odd or even
# A n umber i even if division by 2 gives a remainder of 0
#if the remainder is 1, it is an odd number.

num = int(input("Enter a number: "))
if (num % 2) == 0:#uses the modulus to test the remainder
    print(f"{num} is Even")
else:
    print(f"{num} is ODD")