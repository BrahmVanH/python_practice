import math
import datetime
import platform

# print square root of 5.5
x = 5.5
print(f"Square root of 5.5: {math.sqrt(x)}")

# print absolute value of -8.2
x = -8.2
print(f"Absolute value of -8.2: {abs(x)}")

# print current time in ms
now = datetime.datetime.now()
print(f"current time: {now.time()}")

# print value of current operating system
os_information = platform.platform()
os_name = platform.system()
print(f"Current operating system: {os_information}")