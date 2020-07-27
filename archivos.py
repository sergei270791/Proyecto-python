import math
factorial_10 = str(math.factorial(10))

with open('archivo.txt', 'w') as file:
  file.write(factorial_10)
