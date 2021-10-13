def generateLucasRow(limit):
  rowOfLucas = []
  iteration = 0
  numberLucas = 0
  while numberLucas < limit:
    numberLucas = (2 - iteration) / (1 - iteration - iteration ** 2)
    rowOfLucas.append(numberLucas)
    iteration += 1
  return rowOfLucas

def oddLucasNumbers(rowOfLucas):
  for i in range (0, len(rowOfLucas)):
    if rowOfLucas[i] % 2 == 0:
      rowOfLucas.remove(i)
  return rowOfLucas

def sumOddLucasNumbers(rowOfOddLucas):
  sum = 0
  for i in range(0, len(rowOfOddLucas)):
    sum += rowOfOddLucas[i]
  return sum

print(sumOddLucasNumbers(oddLucasNumbers(generateLucasRow(4000000))))