#Print hamburger palace sign

# ask how much of each condiment user wants

#while loop for each condiment

#print the dang thang

print("******************************")
line = 0

for line in range(0, 5):
  print("*                            *")

print("* Dr. Kow's Hamburger Palace *")

line = 0

for line in range(0, 5):
  print("*                            *")
print("******************************")


print("How many slices of lettuce do you want on your burger?")
lettuce_slice = int(input())
print("How many slices of cheese do you want on your burger?")
cheese_slices = int(input())
print("How many mushrooms do you want on your burger?")
mushroom_slices = int(input())

print("(_________)")

line = 0
for line in range(0, lettuce_slice):
  print(" ~~~~~~~~~")

line = 0
for line in range(0, cheese_slices):
  print(" =========")

print("0" * mushroom_slices)

print(" *********")
print("(_________)")

print("Order up!")