# -*- coding: utf-8 -*-
def dibujar_tablero(tablero):
  """Para imprimir el tablero"""
  for i in range(3):
    lista='|'
    for j in range(3):
      lista=lista+tablero[i][j]+'|'
    print(lista)
  return preguntar(tablero)

def preguntar(tablero):
  """Para preguntar la posición si todavia no gana nadie"""
  aux=str(tablero)
  aux=aux.count('_')
  aux=reglas(tablero,aux)
  if aux!=0:
    n=int(input('¿Qué posición quieres jugar?(1-9):'))
    validar(n,tablero)
    modificar(n,aux,tablero)
  else:
    print('Fin del juego')
    return

def validar(n,tablero):
  """Para validar que la posición elegida"""
  if n<=9 and n>=1 :
    return
  else:
    print('La opción es incorrecta,vuelve a intentarlo')
    return preguntar(tablero)

def modificar(n,aux,tablero):
  """Para modificar los valores de la matriz tablero"""
  aux2=(n-1)//3
  aux3=(n-1)%3
  if tablero[aux2][aux3]=='_':
    if aux%2==0:
      tablero[aux2][aux3]='O'
    else:
      tablero[aux2][aux3]='X'
    return dibujar_tablero(tablero)
  else:
    print('La opcion ya tiene un valor,vuelve a intentarlo')
    return preguntar(tablero)

def reglas(tablero,aux):
  """Para saber si alguien ganó y quien ganó"""
  if aux!=0:
    if tablero[0][1]==tablero[0][2]==tablero[0][0]!='_' or tablero[1][0]==tablero[1][1]==tablero[1][2]!='_' or tablero[2][0]==tablero[2][1]==tablero[2][2]!='_' or tablero[0][0]==tablero[1][0]==tablero[2][0]!='_' or tablero[0][1]==tablero[1][1]==tablero[2][1]!='_' or tablero[0][2]==tablero[1][2]==tablero[2][2]!='_' or tablero[0][0]==tablero[1][1]==tablero[2][2]!='_' or tablero[0][2]==tablero[1][1]==tablero[2][0]!='_':
      if aux%2!=0:
        print('El ganador es el jugador O(Segundo jugador)')
      else:
        print('El ganador es el jugador X(Primer jugador)')
      aux=0
      return aux
    else:
      return aux
  else:
    print('El juego quedo en empate')
    return aux


tablero= [['_' for x in range(3)] for y in range(3)]
print("Bienvenido al juego Ta-Te-Ti")
print('El primer jugador es X y El segundo jugador sera O y así sucesivamente')
print('El orden de las posiciones es de izquierda a derecha y de arriba hacia abajo')
print('Empecemos!!!')

try:
  dibujar_tablero(tablero)
except KeyboardInterrupt:
  print('\nFin del programa')

