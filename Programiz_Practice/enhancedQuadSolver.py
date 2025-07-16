import math       # Provides mathematical functions (like sqrt) for real numbers.
import cmath      # Provides mathematical functions that support complex numbers.
import sys        # Gives access to interpreter variables and functions, including command-line arguments (sys.argv).

def format_number(x):
    """
    Formats a number to a string with 2 decimal places.
    
    If the number is a complex number (checked with isinstance), and its imaginary
    part is negligibly small, then it is formatted as if it were a real number. Otherwise,
    the formatting shows both parts.
    
    Parameters:
    - x: The number (real or complex) to format.
    
    Returns:
    - A string representing the number formatted to two decimal places.
    
    Notes:
    - isinstance(x, complex) checks the type of x. This is the Pythonic way to determine
      if x is an instance of the complex type.
    """
    if isinstance(x, complex):  # Check if 'x' is a complex number.
        # If the imaginary part is extremely small, we treat the number as real.
        if abs(x.imag) < 1e-10:  
            return f"{x.real:.2f}"
        else:
            # Determine the sign for proper formatting of the imaginary part.
            sign = '+' if x.imag >= 0 else '-'
            return f"{x.real:.2f} {sign} {abs(x.imag):.2f}i"
    # Otherwise, format x (a real number) normally.
    return f"{x:.2f}"

def solve_quadratic(a, b, c):
    """
    Computes the solutions of the quadratic equation: ax^2 + bx + c = 0.
    
    This function uses the quadratic formula, where the discriminant (D) is given by:
        D = b^2 - 4ac
    The discriminant determines:
      - Two distinct real solutions if D > 0.
      - One real solution (a double root) if D == 0.
      - Two complex solutions if D < 0.
    
    We use:
      - math.sqrt for computing the square root when D is non-negative.
      - cmath.sqrt for computing the square root when D is negative (allowing complex outputs).
    
    Parameters:
    - a, b, c: The coefficients of the quadratic equation (with a ≠ 0).
    
    Returns:
    - num_solutions: An integer representing the number of distinct solutions (1 or 2).
    - solution: A formatted string describing the solutions.
    """
    discriminant = b**2 - 4 * a * c  # Calculate the discriminant.
    
    if discriminant > 0:
        # Two distinct real solutions.
        num_solutions = 2
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        solution = f"The solutions are: {format_number(root1)} and {format_number(root2)}"
    elif discriminant == 0:
        # One real solution (repeated root).
        num_solutions = 1
        root = -b / (2 * a)
        solution = f"The solution is: {format_number(root)}"
    else:
        # Two complex solutions when the discriminant is negative.
        num_solutions = 2
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        solution = f"The solutions are (complex): {format_number(root1)} and {format_number(root2)}"
    
    return num_solutions, solution

def get_coefficients():
    """
    Prompts the user for the coefficients of the quadratic equation.
    
    This function ensures:
      - The input values are numeric (using a try-except block).
      - The coefficient 'a' is not zero (since a quadratic requires a non-zero a).
    
    Returns:
    - a, b, c: Validated numeric coefficients that the user inputs.
    """
    while True:
        try:
            # Prompt the user for coefficient 'a'.
            a = float(input("Please enter the value of coefficient a (note: a must not equal 0): "))
            if a == 0:
                print("Coefficient 'a' cannot be 0. Please try again.")
                continue  # Restart the loop if a is invalid.
            
            # Prompt the user for coefficients 'b' and 'c'.
            b = float(input("Enter coefficient b: "))
            c = float(input("Enter coefficient c: "))
            
            return a, b, c
        
        except ValueError:
            # Handle cases where the user does not input a number.
            print("Invalid input. Please enter numeric values only.")

def main():
    """
    The main interactive function for the quadratic solver.
    
    - Welcomes the user.
    - Continually prompts the user to enter quadratic coefficients,
      then computes and displays the results.
    - Offers the option to solve another equation.
    
    This function is only executed when the script is run directly, not when
    the module is imported elsewhere. This design supports code reuse and modularity.
    """
    print("Welcome to the Quadratic Equation Solver!")
    while True:
        print("\nLet's solve a quadratic equation!")
        # Retrieve validated user input.
        a, b, c = get_coefficients()
        
        # Solve the quadratic equation with the provided coefficients.
        num_solutions, solution = solve_quadratic(a, b, c)
        
        # Display the number of solutions with correct text.
        if num_solutions == 1:
            print(f"\nThere is {num_solutions} solution.")
        else:
            print(f"\nThere are {num_solutions} solutions.")
        print(solution)
        
        # Ask the user whether to solve another equation.
        another = input("\nWould you like to solve another equation? (yes/no): ").strip().lower()
        if another in ("no", "n"):
            print("Goodbye! Thanks for using the quadratic solver. Have a great day!")
            break

# This block allows the code to be either executed interactively
# or imported without running the interactive interface automatically.
if __name__ == "__main__":
    # Here we examine sys.argv which contains command-line arguments.
    # For example, running the script as: python script.py test
    # will place "test" in sys.argv[1], signaling that we should run the unit tests.
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        import unittest  # Import the unit testing framework.
        
        class TestQuadraticSolver(unittest.TestCase):
            def test_two_real_solutions(self):
                # Test equation: x^2 - 3x + 2 = 0 has roots 1 and 2.
                num_sol, sol_str = solve_quadratic(1, -3, 2)
                self.assertEqual(num_sol, 2)
                self.assertTrue("1.00" in sol_str and "2.00" in sol_str)
            
            def test_one_real_solution(self):
                # Test equation: x^2 + 2x + 1 = 0 has a double root at -1.
                num_sol, sol_str = solve_quadratic(1, 2, 1)
                self.assertEqual(num_sol, 1)
                self.assertIn("-1.00", sol_str)
            
            def test_complex_solutions(self):
                # Test equation: x^2 + 2x + 5 = 0 which has complex roots.
                num_sol, sol_str = solve_quadratic(1, 2, 5)
                self.assertEqual(num_sol, 2)
                self.assertIn("i", sol_str)
                
        # The argv parameter passed here tells unittest to ignore any extra command-line arguments.
        unittest.main(argv=[sys.argv[0]])
    else:
        # Run the main interactive function if no special "test" argument is provided.
        try:
            main()
        except KeyboardInterrupt:
            print("\nProgram interrupted. Goodbye!")
