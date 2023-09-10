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
          ret += cents // 25
          cents %= 25
          ret += cents // 10
          cents %= 10
          ret += cents // 5
          cents %= 5
          ret += cents 
          return ret
     
    def dispense_quarter(self, beep: bool):
          print("/--\\")
          print("|25|")
          print("\\--/\n")
          if (beep):
               self.beep()

    def dispense_dime(self, beep: bool):
         print("/--\\")
         print("|10|")
         print("\\-/\n")
         if (beep):
              self.beep()
    
    def dispense_nickel(self, beep: bool):
         print("/--\\")
         print("|5|")
         print("\\-/\n")
         if (beep):
              self.beep()
    
    def dispense_penny(self, beep: bool):
         print("/-\\")
         print("|1|")
         print("\\-/\n")
         if (beep):
              self.beep()


    def beep(self):
          print("\007")
          try:
               time.sleep(1)
          except: 
               print("An exception occured")
               
     


          