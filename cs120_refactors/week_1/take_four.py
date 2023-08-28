# Game of Take Four

# Tell users playing game
# Explain rules to users

# Declare variables?

# Print number of stones remaining in pot
# Prompt Player 1 to choose number of stones to remove
# Updated stones remaining 
# Prompt Player 2 to choose number of stone to remove
# Update stones remaining
# When Number of stones in pot reaches zero, player to take last stone from pot loses

print("How many stones would you like to begin with?")
stones_remaining = int(input())
print(f"There are {stones_remaining} left in the pot")
while stones_remaining > 0:
  print("Player 1, how many stones would you like to remove from the pot?")
  stones_removed = int(input())

  while stones_removed > 4 or stones_removed < 1:
    print("Please choose a number 1 to 4")
    stones_removed = int(input())

  while stones_removed > stones_remaining:
     print("There aren't that many stones left in the pot, please choose an appropriate number")
     stones_removed = int(input())

  stones_remaining -= stones_removed

  if stones_remaining == 1:
    print(f"There is {stones_remaining} stone left in the pot")
  else:
    print(f"There are {stones_remaining} stones left in the pot")


  if stones_remaining <= 0:
      print("You took the last stone, Player 2 wins")
      break
    
  print("Player 2, how many stones would you like to remove from the pot?")
  stones_removed = int(input())

  while stones_removed > 4 or stones_removed < 1:
      print("Please choose a number 1 to 4")
      stones_removed = int(input())

  while stones_removed > stones_remaining:
     print("There aren't that many stones left in the pot, please choose an appropriate number")
     stones_removed = int(input())

  stones_remaining -= stones_removed

  if stones_remaining == 1:
    print(f"There is {stones_remaining} stone left in the pot")
  else:
    print(f"There are {stones_remaining} stones left in the pot")


  if stones_remaining <= 0:
      print("You took the last stone, Player 1 wins")
      break




