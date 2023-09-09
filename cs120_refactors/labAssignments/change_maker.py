from coins import Coins
coins = Coins()
# Ask the user for the amount of change to give out (in cents)
print("How much chage do you want to give out?")
cents = int(input())


# Report the number of coins we will give out to make that change.

change_cents = coins.number_of_coins(cents)
print(change_cents)

