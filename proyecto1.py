from random import choices
def aleatorio():
  """Mostrara los 2 valores aleatorios y imprimira la suma"""
  print("Enseguida te mostraremos los resultados al tirar los 2 dados:")
  list=choices([1,2,3,4,5,6],k=2)
  print(list)
  print(sum(list))
  return consultar()

def consultar():
  """Sirve para comsultar y validar si el usuario quiere seguir jugando"""
  respuesta=input("¿Quieres seguir jugando? Responde sí o no: ")
  respuesta=respuesta.strip()
  while respuesta=="si" or respuesta=="sí" or respuesta=="Si" or respuesta=="Sí":
      return aleatorio()
  else:
    if(respuesta=="no" or respuesta=="No"):
      print("Fin del juego.")
      return
    else:
      print("La respuesta es incorrecta,vuelve a intentarlo")
      return consultar()
print("Bienvenido al juego de dados:")
aleatorio()




