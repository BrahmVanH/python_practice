import time

class Dollars():
  def number_of_bills(self, dollars):
    ret = 0
    ret += dollars // 100
    dollars %= 100
    ret += dollars // 50
    dollars %= 50
    ret += dollars // 20
    dollars %= 20
    ret += dollars // 10
    dollars %= 10
    ret += dollars // 5
    dollars %= 5
    ret += dollars
    return ret
  
  def dispense_hundred_bill(self, beep: bool): 
      print("|---------|")
      print("|---100---|")
      print("|---------|")

      if (beep):
        self.beep()

  def dispense_fifty_bill(self, beep: bool):
      print("|--------|")
      print("|---50---|")
      print("|--------|")

      if (beep):
          self.beep()

  def dispense_twenty_bill(self, beep: bool):
      print("|--------|")
      print("|---20---|")
      print("|--------|") 

      if (beep):
          self.beep()
  
  def dispense_ten_bill(self, beep: bool):
      print("|--------|")
      print("|---10---|")
      print("|--------|") 

      if (beep):
          self.beep() 
  
  def dispense_five_bill(self, beep: bool):
      print("|---------|")
      print("|----5----|")
      print("|---------|") 

      if (beep):
          self.beep()

  def dispense_one_bill(self, beep: bool):
      print("|---------|")
      print("|----1----|")
      print("|---------|") 

      if (beep):
          self.beep()

  def beep(self):
          print("\007")
          try:
               time.sleep(1)
          except: 
               print("An exception occurred")