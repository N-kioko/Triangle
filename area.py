def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area

# Input base and height from the user
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area using the function
triangle_area = calculate_triangle_area(base, height)

# Print the result
print(f"The area of the triangle with base {base} and height {height} is {triangle_area}")
