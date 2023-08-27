# Math trick to take a number, manipulate it several times and always result in the number 3

print("Check out this cool math trick")
# request a positive integer from the user 
print("Enter a positive integer, any one will do ")

og_number_str = input()
x = int(og_number_str)

# square integer 
y = x * x

# Add result to original
y = y + x
# Divide by og 
y = y / x
# add 17
y = y + 17
# subtract og from result
y = y - x
# divide by six
y = y / 6
# result should be three
print(f"Here is the result, should be 3: {y}" )