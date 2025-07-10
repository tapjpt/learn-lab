# Creates a function named 'greet' that takes one parameter, 'name' 
def greet(name):  
    # Prints a personalized greeting message using f-strings
    print(f"Hello, {name}! Welcome to the Python world!")

# Asks the user to input their name and stores it in the variable 'user_name'
user_name = input("Enter your name: ")  

# Calls the 'greet' function, passing the user's input as the argument
greet(user_name)  