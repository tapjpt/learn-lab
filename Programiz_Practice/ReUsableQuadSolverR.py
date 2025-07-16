#Importing the cmath module, which allows us to perform 
#complex number calculations

from cmath import sqrt

#Function to solve the quadratic equation
def solve_quadratic(a, b, c):
    """
    This function calculates the solutions of a quadratic equation
    of the form ax^2 + bx + c = 0 using the quadratic formula.
    Parameters: 
        -a, b, c: Coefficients of the quadratic equation (a != 0)
    Returns: 
        -num_solutions: Number of solutions(real or complex)
        - solutions: A formatted string describing the solutions
    """

    #Step 1: Calculate the discriminant (b^2 - 4ac)
    discriminant = (b**2) - (4 * a * c)
    
    #variables for the mechanics of the quad equation
    two_a = 2 * a
    real_part = -b/two_a
    the_discri = sqrt(discriminant)/two_a

    #Step 2: Use the discriminant to deterimine the type of and number of solutions
    #:.2f is a Python string formatting tool that ensures a floating-point number is 
    #rounded to two decimal places when displayed.
    if discriminant > 0:
        # If the discriminant is positive, there are 2 real solutions
        num_solutions = 2
        root1 = real_part + the_discri
        root2 = real_part - the_discri
        
        solution = f"The solutions are: {root1:.2f} and {root2:.2f}" 
    elif discriminant == 0:
       # If the discriminant is zero, there is 1 real solution (a repeated root)
        num_solutions = 1
        root = real_part
        
        solution = f"The solution is: {root:.2f}"
    else:
    # If the discriminant is negative, there are 2 complex solutions
        num_solutions = 2
        root1 = real_part + the_discri
        root2 = real_part - the_discri
       
        solution = f"The complex solutions are: {root1:.2f} and { root2:.2f}\nYou have imaginary solutions!"

    #Step 3: Return the number of solutions and the formatted string
    return num_solutions, solution

# Function to get validated input from the user 
def get_coefficients():
    """
    This function prompts the user to input the coefficients of
    a quadratic equation (a, b, c). It ensures the input is valid
    and that 'a" is not zero.
    Returns:
        -a, b, c: Validated coefficients
    """
    while True:
        try:#try captures possible errors and how to handle them.  
            #Prompt for coefficient 'a' (a != 0)
            a = float(input("Please enter the value of coefficient a (note: a must not equal 0): "))
            if a == 0:
                print("The coefficient 'a' cannot be 0.  Please try again.")
                continue #Restart the loop for valid input
            #Prompt for coefficients 'b' and 'c'
            b = float(input("Enter coefficient b: "))
            c = float(input("Enter coefficient c: "))
            return a, b, c # Valid coefficients
        except ValueError:#helps prevent code from captures and runs in case there is an error and how to handle.
            #Handle invalid (non-numeric input
            print("Invalid input. Please enter numeric values only.")

#Main program to interact with the user
def main():
    """
    The main function handles the flow of the program.
    It repeatedly asks the user to input quadratic coefficients,
    solves the equation, and displays the result.
    """
    print("Welcome to the Quadratic Equation Solver!")

    while True:  #Infinite loop to allow solving multiple equations
        print("\nLet's solve a quadratic equation!")
        a, b, c = get_coefficients() # Get user input for coefficients

        #Solve the quadratic equation using the solve_quadratic function
        num_solutions, solution = solve_quadratic(a, b, c)

        #Display the results
        print(f"\nThere are {num_solutions} solution(s).")
        print(solution)

        #Ask the user if they want to solve another equation
        another = input("\nWould you like to solve another equation? (yes/no): ").strip().lower()
        if another == "no":
            print("Goodbye! Thanks for using the quadratic solver. Have a great day!")
            break #Exit the the loop and end the program

#Ensure the main function runs only when the script is executed directly
if __name__ == "__main__":
    main() #call the main function to start the program