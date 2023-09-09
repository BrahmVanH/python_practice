import time

class Coins():
  
     # Takes a number of cents to make change for, and returns the number
     # of coins required to make change for that amount.  This follows the greedy algorithm
     # for making change: taking the greatest number of quarters before dimes, greatest number
     # of dimes before taking nickels, etc.
     #
     # @param cents the number of cents to make change for.
     # @return the number of coins required to make change for the given number of cents.
    def number_of_coins(self, cents):
          ret = 0
          ret += cents / 25
          cents %= 25
          ret += cents / 10
          cents %= 10
          ret += cents / 5
          cents %= 5
          ret += cents 
          return cents
     
    def dispense_quarter(self, beep):
          print("/--\\")
          print("|25|")
          print("\\--/\n")
          if (beep):
               beep()

    def dispense_dime(self, beep):
         print("/--\\")
         print("|10|")
         print("\\-/\n")
         if (beep):
              beep()
    
    def dispense_nickel(self, beep):
         print("/--\\")
         print("|5|")
         print("\\-/\n")
    
    def dispense_penny(self, beep):
         print("/-\\")
         print("|1|")
         print("\\-/\n")


    def beep():
          print("\007")
          try:
               time.sleep(333)
          except: 
               print("An exception occured")
               
     


          