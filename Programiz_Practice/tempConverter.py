# Introduction message for the user
print("Hi, I'm your temperature converter.")  # Prints a friendly introduction to set the tone of the program.

# Start of a try-except block to handle potential errors
try:
    # Asking the user which temperature system they use
    location = input("So tell me, in your location, do you use Fahrenheit or Celsius? ").strip().lower()
    # Educational note: 
    # 1. `input()` takes input from the user.
    # 2. `.strip()` removes any leading or trailing whitespace.
    # 3. `.lower()` converts the input to lowercase to ensure consistency regardless of capitalization.
    
    # Check if the user uses Fahrenheit
    if location == "fahrenheit":  # Checks if the user's input matches "fahrenheit".
        print("Ah, so you use Fahrenheit.")  # Acknowledges the user's choice.
        print("I'll tell you what it is in Celsius.")  # Explains what the program will do next.
        
        # Asking the user for the temperature in Fahrenheit
        f_temp = float(input("First tell me, what's the temperature? "))  
        # Educational note:
        # 1. `input()` gathers the temperature as a string.
        # 2. `float()` converts the input string to a floating-point number so it can be used in calculations.

        # Converting Fahrenheit to Celsius
        c_temp = (f_temp - 32) * (5 / 9)  # Applies the formula for converting Fahrenheit to Celsius.
        # Educational note: The formula is Celsius = (Fahrenheit - 32) * 5/9.

        # Displaying the temperature in Celsius
        print(f"In Celsius, your temperature is {c_temp:.2f}°C")  
        # Educational note:
        # 1. `{c_temp:.2f}` formats the output to show 2 decimal places for neatness.
        # 2. `°C` is added to indicate the unit.

    # Check if the user uses Celsius
    elif location == "celsius":  # Checks if the user's input matches "celsius".
        print("Ah, so you use Celsius.")  # Acknowledges the user's choice.
        print("I'll tell you what it is in Fahrenheit.")  # Explains what the program will do next.

        # Asking the user for the temperature in Celsius
        c_temp = float(input("First tell me, what's the temperature? "))  
        # Educational note:
        # 1. The temperature input is gathered and converted to a float just like above.

        # Converting Celsius to Fahrenheit
        f_temp = c_temp * (9 / 5) + 32  # Applies the formula for converting Celsius to Fahrenheit.
        # Educational note: The formula is Fahrenheit = (Celsius * 9/5) + 32.

        # Displaying the temperature in Fahrenheit
        print(f"In Fahrenheit, your temperature is {f_temp:.2f}°F")  
        # Educational note: The same formatting and unit indicator as earlier.

    # Handling invalid inputs for location
    else:
        print("Please enter either Fahrenheit or Celsius as your location.")  
        # This block executes if the user's input doesn't match "fahrenheit" or "celsius".

# First except block to handle specific input errors
except ValueError:  
    # Educational note:
    # This catches errors if the user enters something that cannot be converted to a `float()`.
    print("Oops! Please make sure you enter a valid number for the temperature.")  

# Second except block to catch any unexpected errors
except Exception as e:  
    # Educational note:
    # 1. This acts as a catch-all for any errors not handled by the first block (e.g., programmer error or unforeseen issues).
    # 2. `Exception as e` captures the error message in the variable `e`, which can be displayed for debugging.
    print(f"An error occurred: {e}")  