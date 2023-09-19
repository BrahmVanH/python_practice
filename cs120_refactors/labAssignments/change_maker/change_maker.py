from coins import Coins
from dollars import Dollars
coins = Coins()
dollarsClass = Dollars()

# Ask the user for the amount of change to give out (in dollars and cents)
print("How much change in dollars do you want to give back?")
dollars = int(input())
print("How much change in cents do you want to give back?")
cents = int(input())


# Report the number of coins we will give out to make that change.
number_of_dollars = dollarsClass.number_of_bills(dollars)
number_of_coins = coins.number_of_coins(cents)
print(f"You will be returning {number_of_dollars} bills")
print(f"You will be returning {number_of_coins} coins")

change_dollars = 0

while (change_dollars + 100 <= dollars):
  dollarsClass.dispense_hundred_bill(True)
  change_dollars += 100

while (change_dollars + 50 <= dollars):
  dollarsClass.dispense_fifty_bill(True)
  change_dollars += 50

while (change_dollars + 20 <= dollars):
  dollarsClass.dispense_twenty_bill(True)
  change_dollars += 20

while (change_dollars + 10 <= dollars):
  dollarsClass.dispense_ten_bill(True)
  change_dollars +=10

while (change_dollars + 5 <= dollars):
  dollarsClass.dispense_five_bill(True)
  change_dollars += 5

while (change_dollars < dollars):
  dollarsClass.dispense_one_bill(True)
  change_dollars +=1

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

