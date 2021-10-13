def dividableNumberGenerator(limit, number):
  dividableNumbers = []
  for i in range(0, limit, number):
    dividableNumbers.append(i)
  return dividableNumbers

def sumDividableNumbers(dividableNumbers):
  sum = 0
  for i in range(0, len(dividableNumbers)):
    sum += dividableNumbers[i]
  return sum

print(sumDividableNumbers(dividableNumberGenerator(10000, 7) + dividableNumberGenerator(10000, 9)))