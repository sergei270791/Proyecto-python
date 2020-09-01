# -*- coding: utf-8 -*
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Sequence,ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import Table,Text

engine=create_engine('sqlite:///:memory:')
Base=declarative_base()
profesor_curso=Table('profesor_curso',Base.metadata,
  Column('curso_id',ForeignKey('curso.id'), primary_key=True),
  Column('profesor_id',ForeignKey('profesor.id'), primary_key=True)
)
class Curso(Base):
  __tablename__='curso'
  id=Column(Integer,Sequence('curso_id_seq'),primary_key=True)
  nombre=Column(String)
  alumno=relationship("Alumno",order_by="Alumno.id",back_populates="curso")
  profesor=relationship("Profesor",secondary=profesor_curso,back_populates="curso")
  def __repr__(self):
    return '{}'.format(self.nombre)
class Alumno(Base):
  __tablename__='alumno'
  id=Column(Integer,Sequence('alumno_id_seq'),primary_key=True)
  nombre=Column(String)
  apellido=Column(String)
  curso_id=Column(Integer,ForeignKey('curso.id'))
  curso=relationship("Curso",back_populates="alumno")
  def __repr__(self):
    return '{} {}'.format(self.nombre,self.apellido)
class Profesor(Base):
  __tablename__='profesor'
  id=Column(Integer,Sequence('profesor_id_seq'),primary_key=True)
  nombre=Column(String)
  apellido=Column(String)
  curso=relationship("Curso",secondary=profesor_curso,back_populates="profesor")
  def __repr__(self):
    return '{} {}'.format(self.nombre,self.apellido)

Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()
R_vasquez=Profesor(nombre='Robinson Ausberto',apellido='Vasquez Olano')
A_altamirano=Profesor(nombre='Alejandra Beatriz',apellido='Altamirano Macetas')
J_tello=Profesor(nombre='Jose Luis',apellido='Tello Rojas')
session.add_all([R_vasquez,A_altamirano,J_tello])
optica=Curso(nombre='Optica Clasica')
mecanica_clasica=Curso(nombre='Mecanica Clasica')
metodos=Curso(nombre='Metodos Matematicos para Fisicos 2')
#session.add_all([optica,mecanica_clasica,metodos])
optica.profesor.append(R_vasquez)
optica.profesor.append(A_altamirano)
mecanica_clasica.profesor.append(R_vasquez)
mecanica_clasica.profesor.append(J_tello)
metodos.profesor.append(J_tello)
metodos.profesor.append(A_altamirano)
print('Los profesores son:')
print(session.query(Profesor).all())
print('Los cursos son:')
print(session.query(Curso).all())
print('Los curso de R.Vasquez son:')
print(session.query(Curso).filter(Curso.profesor.any(nombre='Robinson Ausberto')).all())
print('Los curso de J.Tello son:')
print(session.query(Curso).filter(Curso.profesor.any(nombre='Jose Luis')).all())
print('Los curso de A.Altamrinano son:')
print(session.query(Curso).filter(Curso.profesor.any(nombre='Alejandra Beatriz')).all())
print('Los profesores de Optica Clasica son:')
print(session.query(Profesor).filter(Profesor.curso.any(nombre='Optica Clasica')).all())
print('Los profesores de Mecanica Clasica son:')
print(session.query(Profesor).filter(Profesor.curso.any(nombre='Mecanica Clasica')).all())
print('Los profesores de Metodos Matematicos para Fisicos 2 son:')
print(session.query(Profesor).filter(Profesor.curso.any(nombre='Metodos Matematicos para Fisicos 2')).all())
