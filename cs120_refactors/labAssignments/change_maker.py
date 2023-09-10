from coins import Coins
coins = Coins()
# Ask the user for the amount of change to give out (in cents)
print("How much chage do you want to give out?")
cents = int(input())


# Report the number of coins we will give out to make that change.

number_of_coins = coins.number_of_coins(cents)
print(f"you will be returning {number_of_coins} coins")

change_cents = 0

while (change_cents + 25 < cents):
  coins.dispense_quarter(True)
  change_cents += 25

while (change_cents + 10 < cents):
  coins.dispense_dime(True)
  change_cents += 10

while (change_cents + 5 < cents):
  coins.dispense_nickel(True)
  change_cents += 5

while (change_cents < cents):
  coins.dispense_penny(True)
  change_cents += 1

