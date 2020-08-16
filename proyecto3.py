# -*- coding: utf-8 -*
import unittest
def suma(lista=list()):
    sum=0
    for i in lista:
      sum+=i
    return sum

class producto(object):
  """Clase que representa un producto"""
  def __init__(self,codigo,precio,descuento):
    self.codigo=codigo
    self.precio=precio
    self.descuento=descuento
  
  def __repr__(self):
    return self.codigo

class lista_productos(object):
  def __init__(self):
    self.lista=list()
  """Clase que representa una lista de precios"""
  def precio_sin_descuento(self, parameter_list):
    """Método para obtener el precio de un producto sin descuento"""
    suma()
  
  def precio_con_descuento(self, parameter_list):
    """Método para obtener el precio de un producto con descuento"""

class compra(object):
  """"Clase que representa la compra"""
  pass

class CajaRegistradora(object):
  """Clase que representa la caja registradora"""
  def __init__(self):
    self.lista=list()
    self.precios=list()
    self.descuentos=list()
  
  def preguntar(self):
    try:
      respuesta=input("¿Quieres añadir productos al carrito? Responde sí o no: ")
      respuesta=respuesta.strip()
      while respuesta=="si" or respuesta=="sí" or respuesta=="Si" or respuesta=="Sí":
          return self.registrar()
      else:
        if(respuesta=="no" or respuesta=="No"):
          return self.mostrar(self.lista,self.precios,self.descuentos)
        else:
          print("La respuesta es incorrecta,vuelve a intentarlo")
          return self.preguntar()
    except:
      self.finalizar_compra()
  
  def mostrar(self,lista,precios,descuentos):
    subtotal,total=self.aplicar_descuentos(precios,descuentos)
    print("Estado de la compra:")
    if len(lista)==0:
      print('No hay ningun producto.Fin de la operacion.')
      return
    for i in range(len(lista)):
      print(i+1,'.','Codigo:',lista[i],'          ','Precio',precios[i],'           ','descuento',descuentos[i])
    print('El subtotal de los productos es ',subtotal,' ,despues de aplicar los descuentos el total es ',total)
    return self.cobrar_y_vuelto(total)
  
  def registrar(self):
    """Método para agregar un producto escaneado(tipeado) a la compra"""
    try:
      codigo=int(input('Ingrese el codigo del producto: '))
      precio=int(input('Ingrese el precio del producto: '))
      descuento=int(input('Ingrese el descuento del producto: '))
      self.lista.append(codigo)
      self.precios.append(precio)
      self.descuentos.append(descuento)
      return self.preguntar()
    except:
      self.finalizar_compra()
  
  def subtotal(self):
    """Método para calcular el subtotal de la compra"""
    subtotal=suma(precios)
    return subtotal
  
  def total(self):
    """Método para calcular el total de la compra"""
    total=suma(precios_descuentados)
    return total
  
  def aplicar_descuentos(self,precios,descuentos):
    subtotal=suma(precios)
    descuento=suma(descuentos)
    total=subtotal-descuento
    return subtotal,total
  
  def finalizar_compra(self):
    """Método para finalizar la compra"""
    print('Fin de la compra,ahora le mostraremos el estado de la compra para que pueda cancelar el cliente')
    return self.mostrar(self.lista,self.precios,self.descuentos)
  
  def cobrar_y_vuelto(self,total):
    """Método para indicar con cuánto paga el cliente e indica cuánto debe devolverle"""
    vuelto=-1
    while vuelto<0:
      pago=int(input("¿Con cuanto paga el cliente?: "))
      vuelto=pago-total
      if vuelto<0:
        print('El pago es insuficiente ,vuelve a intentarlo')
    print('El vuelto del cliente es: ',vuelto)
    print("Eso es todo , hasta luego")
    return 




class CajaRegistradoraTest(unittest.TestCase):
  def setUp(self):
    self.caja=CajaRegistradora()
  def test_aplicar_descuentos(self):
    x=self.caja.aplicar_descuentos([120,150,64],[10,18,8])
    self.assertEqual((334,298),x)


if __name__ == '__main__' :
  unittest.main()

caja=CajaRegistradora()
caja.preguntar()
