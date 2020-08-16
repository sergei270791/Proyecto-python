# -*- coding: utf-8 -*

import sqlite3
conexion=sqlite3.connect(':memory:')
cursor=conexion.cursor()
"""con cursor.execute(aca dentro se pone entre comillas el codigo squl para crear tablas, insertar datos, etc)
con conexion.commit() se guardan los cambios, con conexion.rollback() se revierten los cambios 
para consultar las filas se define una nueva variable query con valor = "SELECT * FROM NAME_TABLE" 
se define otra variable para traer esa filas que se iguala a cursor.execute(query).fetchall
y para imprimirlos en pantalla ponemos esa variable dentro de un print y listo
por ultimo cerramos la conexion con conexion.close()
"""
