def triangle_area_by_sides(a, b, c):
    """Calculate the area of a triangle given the 
    lengths of its three sides using Heron's formula."""
    #Check if the sides form a valid triangle
    
    if(a + b > c) and (a+c > b) and (b + c > a):
        #Calculate the semi-perimeter
        s = (a + b + c) / 2
        #Calculate the area using Heron's formula
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area
    else:
        return "The entered values do not form a valid triangle."

# Example usage
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

area = triangle_area_by_sides(a, b, c)  # Calls the function and stores the result in `area`
if isinstance(area, float):  # Checks if `area` is a floating-point number (a valid area)
    print(f"The area of the triangle is {area:.2f}")  # Prints the area if true
else:
    print(area)  # Prints the error message if false
