# Conversion factor
conv_fac = 0.621371

# Prompt user for preferred metric or imperial system
metric = input("Do you prefer metric or imperial? ").lower()

try:
    if metric == "metric":
        # Taking Kilometers input from the user
        km = float(input("Enter value in kilometers: "))
        # Calculate miles
        miles = km * conv_fac
        # Print result
        print(f"{km:.2f} kilometers is equal to {miles:.2f} miles.")
    elif metric == "imperial":
        # Taking Miles input from the user
        miles = float(input("Enter value in miles: "))
        # Calculate kilometers
        km = miles / conv_fac
        # Print result
        print(f"{miles:.2f} miles is equal to {km:.2f} kilometers.")
    else:
        print("Please enter either 'metric' or 'imperial'.")
except ValueError:
    print("Please enter a valid numeric value.")