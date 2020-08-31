# -*- coding: utf-8 -*
"""MUY IMPORTANTE: AL DESCOMENTAR LAS LINEAS DE CODIGO DEL PROGRAMA , SE VE COMO SIGUE EL FLUJO DE EJECUCION Y COMENTANDO EL TESTING."""
import unittest
def suma(lista=list()):
    sum=0
    for i in lista:
      sum+=i
    return sum

class Producto(object):
  """Clase que representa un producto"""
  def __init__(self,codigo,precio,descuento):
    self.codigo=codigo
    self.precio=precio
    self.descuento=descuento
  
  def __str__(self):
    return '- Codigo:{}          Precio:{}         Descuento:{}\n'.format(self.codigo,self.precio,self.descuento)
  
  def representacion(self):
    return self.precio,self.descuento

class ListaProductos(object):
  """Clase que representa una lista de precios"""
  def __init__(self,lista):
    self.lista=lista
    self.lista_sin_descuento=list()
    self.lista_con_descuento=list()
  
  def asignar(self):
    lista_provisional=list()
    lista_provisional2=list()
    for producto in self.lista:
      self.precio,self.descuento=producto.representacion()
      lista_provisional.append(self.precio)
      lista_provisional2.append((self.precio-self.descuento))
    self.lista_sin_descuento=lista_provisional
    self.lista_con_descuento=lista_provisional2
  def precio_sin_descuento(self):
    """Método para obtener el precio de un producto sin descuento"""
    self.asignar()
    return self.lista_sin_descuento
  
  def precio_con_descuento(self):
    """Método para obtener el precio de un producto con descuento"""
    self.asignar()
    return self.lista_con_descuento
  
  def __repr__(self):
    return self.lista

class Compra(object):
  """"Clase que representa la compra"""
  def __init__(self,subtotal,total):
    self.subtotal=subtotal
    self.total=total
  
  def mostrar(self):
    print('El subtotal de los productos es ',self.subtotal,' ,despues de aplicar los descuentos el total es ',self.total)
    return True

class CajaRegistradora(object):
  """Clase que representa la caja registradora"""
  def __init__(self):
    self.lista=list()
  def preguntar(self):
    respuesta=input("¿Quieres añadir productos al carrito? Responde sí o no: ")
    respuesta=respuesta.strip()
    if respuesta=="si" or respuesta=="sí" or respuesta=="Si" or respuesta=="Sí":
      return self.registrar()
    else:
      if(respuesta=="no" or respuesta=="No"):
        return self.finalizar_compra()
      else:
        print("La respuesta es incorrecta,vuelve a intentarlo")
        return self.preguntar()
  def registrar(self):
    codigo=int(input('Ingrese el codigo del producto: '))
    precio=int(input('Ingrese el precio del producto: '))
    descuento=int(input('Ingrese el descuento del producto: '))
    self.producto=Producto(codigo,precio,descuento)
    return self.agregar(self.lista,self.producto)
  def estado_compra(self): 
    print("Estado de la compra:")
    for producto in self.lista:
      print(producto)
  def agregar(self,lista,producto):
    """Método para agregar un producto escaneado a la compra"""
    self.producto=producto
    self.lista.append(producto)
    #self.estado_compra()
    #self.preguntar()
    return self.lista
  def subtotal(self):
    """Método para calcular el subtotal de la compra"""
    self.lista_productos=ListaProductos(self.lista)
    subtotal=suma(self.lista_productos.precio_sin_descuento())
    return subtotal
  def total(self):
    """Método para calcular el total de la compra"""
    self.lista_productos=ListaProductos(self.lista)
    total=suma(self.lista_productos.precio_con_descuento())
    return total
  def finalizar_compra(self):
    """Método para finalizar la compra"""
    self.lista_productos=ListaProductos(self.lista)
    print('Fin de la compra,ahora le mostraremos el estado de la compra para que pueda cancelar el cliente')
    self.compra=Compra(self.subtotal(),self.total())
    if self.compra.mostrar():
      return self.cobrar_y_vuelto(self.total())
  def cobrar_y_vuelto(self,total):
    pago=total-1
    while pago<total:
      pago=int(input("¿Con cuanto paga el cliente?: "))
      if pago<total:
        print('El pago es insuficiente ,vuelve a intentarlo')
    return self.vuelto(pago,total)
  def vuelto(self,pago,total):
    """Método para indicar con cuánto paga el cliente e indica cuánto debe devolverle"""
    vuelto=pago-total
    if vuelto<0:
      return False
    """ print('El vuelto del cliente es: ',vuelto)
    print("Eso es todo , hasta luego") """
    return vuelto


#caja=CajaRegistradora()
#caja.preguntar()


class CajaRegistradoraTest(unittest.TestCase):
  def setUp(self):
    self.caja=CajaRegistradora()
    self.producto1=Producto(125000,120,10)
    self.producto2=Producto(125001,180,15)
    self.producto3=Producto(125002,100,8)
  def test_agregar(self):
    """ Casos de prueba sobre el método que agrega un producto a la compra """
    lista=self.caja.agregar(self.caja.lista,self.producto1)
    self.assertEqual([self.producto1],lista)
    lista=self.caja.agregar(self.caja.lista,self.producto2)
    self.assertEqual([self.producto1,self.producto2],lista)
    lista=self.caja.agregar(self.caja.lista,self.producto3)
    self.assertEqual([self.producto1,self.producto2,self.producto3],lista)
    self.caja.lista=lista
    self.caja.lista_productos=ListaProductos(lista)
  def test_subtotal(self):
    """ Casos de prueba sobre el método  que calcula el subtotal de la compra """
    self.test_agregar()
    subtotal=self.caja.subtotal()
    self.assertEqual(400,subtotal)
  def test_total(self):
    """ Casos de prueba sobre el método  que calcula el total de la compra (con los descuentos aplicados) """
    self.test_agregar()
    total=self.caja.total()
    self.assertEqual(367,total)
  def test_finalizar_compra(self):
    """ Casos de prueba sobre el método que finaliza la compra """
    pass
  def test_vuelto(self):
    """ Casos de prueba sobre el método que calcula el vuelto que se le debe dar al cliente """
    vuelto1=self.caja.vuelto(100,50)
    vuelto2=self.caja.vuelto(200,170)
    vuelto3=self.caja.vuelto(50,100)
    vuelto4=self.caja.vuelto(100,92)
    self.assertEqual(50,vuelto1)
    self.assertEqual(30,vuelto2)
    self.assertEqual(8,vuelto4)
    self.assertFalse(vuelto3)

if __name__ == '__main__' :
  unittest.main()
