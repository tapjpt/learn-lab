# Import complex math module
from cmath import sqrt

# Create the function to solve the quadratic
def solve_quadratic(a, b, c):
    # Calculate the discriminant
    d = (b**2) - (4*a*c)
    
    # Determine the number of solutions
    if d > 0:
        sol = 2
        root1 = (-b + d**0.5) / (2 * a)
        root2 = (-b - d**0.5) / (2 * a)
        solution = f"The solutions are: {root1} and {root2}"
    elif d == 0:
        sol = 1
        root = -b / (2 * a)
        solution = f"The solution is: {root}"
    else:
        sol = 0
        root1 = (-b + sqrt(d)) / (2 * a)
        root2 = (-b - sqrt(d)) / (2 * a)
        solution = f"The complex solutions are: {root1} and {root2}\nYou have imaginary solutions!"
        
    return sol, solution

# Introduction message
print("Let's solve quadratics! We'll need 3 numbers from you.")

# User input for coefficients
a = float(input("What is your first number? "))
b = float(input("What is your second number? "))
c = float(input("What is your third number? "))

# Call the function and unpack the results
sol, solution = solve_quadratic(a, b, c)

# Output the results
print(f"There are {sol} solution(s).")
print(solution)

