import random

print("Lets roll some dice");

number_of_sides = [1, 2, 3, 4]

roll_one = random.choice(number_of_sides)
roll_two = random.choice(number_of_sides)
rolls = []
rolls.append(roll_one)
rolls.append(roll_two)
highest_num = max(rolls)
print(f"First die rolled a: {roll_one}")
print(f"Second die rolled a {roll_two}")

if (roll_one > roll_two):
  print("First roll was higher!")
elif (roll_one == roll_two): 
  print("Both die rolled the same")
else: 
  print("Second roll was higher")

print(f"The highest number roll was {highest_num}")


