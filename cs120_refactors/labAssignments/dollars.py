import time

class Dollars():
  def number_of_bills(self, dollars):
    ret = 0
    ret += dollars // 100
    dollars %= 100
    