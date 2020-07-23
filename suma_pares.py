def suma_pares(n):
  sum=0
  for num in range(n):
    sum+=(2*num+2)
  return sum

n=int(input("Ingrese el número de pares que desea sumar: "))
print("L suma de los primeros ",n," primeros números es: ",suma_pares(n))