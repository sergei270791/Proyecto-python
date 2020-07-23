def es_primo(numero):
  cont=0
  resultado = True
  for divisor in range(2, numero):
    if (numero % divisor) == 0:
      resultado = False
      break
  return resultado
n=int(input("Ingresa un numero para saber si es primo: "))
print("la respuesta es ",es_primo(n))