# Prompts the user to input their age as a string, converts it to an integer using `int()`, and assigns it to the variable `age`.
age = int(input("Enter your age: "))

# Checks if the `age` variable is less than 18, which is the threshold for being considered a minor.
if age < 18:
    print("You are a minor.")

# Handles the specific case where `age` is exactly 18, indicating the user has just reached adulthood. 
# The `elif` ensures this condition is checked only if the previous condition (`age < 18`) is false.
elif age == 18:
    print("You just became an adult!")

# Covers all other cases where `age` is greater than 18, printing that the user is an adult.
# The `else` acts as the default condition when none of the previous conditions are met.
else:
    print("You are an adult.")

