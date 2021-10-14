class BinaryCounter:
  def __init__(self, led3, led2, led1, led0):
    self.__led3 = led3
    self.__led2 = led2
    self.__led1 = led1
    self.__led0 = led0

  def getBinaryValue(self):
    return str(self.__led3) + str(self.__led2) + str(self.__led1) + str(self.__led0)

  def getDecimalValue(self):
    return 8 * self.__led3 + 4 * self.__led2 + 2 * self.__led1 + self.__led0

  def getHexadecimalValue(self, decimalValue):
      if decimalValue < 10:
        return decimalValue
      elif decimalValue == 10:
        return "A"
      elif decimalValue == 11:
        return "B"
      elif decimalValue == 12:
        return "C"
      elif decimalValue == 13:
        return "D"
      elif decimalValue == 14:
        return "E"
      else:
        return "F"
        

  def increment(self):
    if not self.__led0:
      self.__led0 = 1
    elif not self.__led1:
      self.__led1 = 1
    elif not self.__led2:
      self.__led2 = 1
      self.__led1 = 0
      self.__led0 = 0
    elif not self.__led3:
      self.__led3 = 1
      self.__led2 = 0
      self.__led1 = 0
      self.__led0 = 0

  def decrement(self):
    if self.__led0:
      self.__led0 = 0
    elif self.__led1:
      self.__led1 = 0
      self.__led0 = 1
    elif self.__led2:
      self.__led2 = 0
      self.__led1 = 1
    elif self.__led3:
      self.__led3 = 0
      self.__led2 = 1
    
binaryCounter = BinaryCounter(1, 0, 1, 0)

print(binaryCounter.getBinaryValue())
print(binaryCounter.getDecimalValue())
print(binaryCounter.getHexadecimalValue(binaryCounter.getDecimalValue()))

binaryCounter.increment()
print(binaryCounter.getBinaryValue())

binaryCounter.decrement()
print(binaryCounter.getBinaryValue())