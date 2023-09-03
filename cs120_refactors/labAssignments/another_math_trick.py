import time

print("I've got another math trick for you!")

# Prompt user to enter their phones area code
print("Enter the first 3 digits of your phone number.")
x = int(input())

# Multiply by 128
x = x * 128
print(f"Your area code multiplied by 128: {x}")
time.sleep(1)

# Add 1
x = x + 1
print(f"... Plus 1: {x}")
time.sleep(1)

# Multiply by 156250
x = x * 156250
print(f"... Multiplied by 156250: {x}")
time.sleep(1)

# Prompt user to enter the last 7 digits of their phone number
print("Now enter the remaining 7 digits of your phone number.")
y = int(input())

# Add last 7 of phone number
x = x + y
print(f"Our working number plus the rest of your phone number: {x}")
time.sleep(1)

# Add last 7 of phone number again
x = x + y
print(f"... The last 7 digits added once more: {x}")
time.sleep(1)

# Subtract 156250
x = x - 156250
print(f"... Minus 156250: {x}")
time.sleep(1)

# Divide number by 2
x = x / 2

# Print result
print(f"... And divided by 2... Does this number look familiar?: {int(x)}")


