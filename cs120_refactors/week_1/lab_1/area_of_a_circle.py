#Let user know were calculating the area of a circle
print("This program calculates the area of a circle.")

# Prompt user to enter radius of circle
print("Please enter the radius of your circle.")

# User input 
r_str = input()

# typecast to int
r = int(r_str)

# Calculate area of circle
pi = 3.141592653
a = (r * r) * pi

# Print area of circle
print(f"The area of your circle is {a}")