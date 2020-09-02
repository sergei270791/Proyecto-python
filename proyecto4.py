# -*- coding: utf-8 -*
import csv
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,Time,String,Sequence,ForeignKey
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
    horario_curso = relationship('Horario', order_by='Horario.dia_de_semana', back_populates='curso')
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
    horario_profesor = relationship('Horario', order_by='Horario.dia_de_semana', back_populates='profesor') 
    def __repr__(self):
        return '{} {}'.format(self.nombre,self.apellido)
class Horario(Base):
    __tablename__ = 'horario'
    
    id = Column(Integer, Sequence('author_id_seq'), primary_key=True)
    # Weekday saved as ISO format
    # https://docs.python.org/3/library/datetime.html#datetime.date.isoweekday
    dia_de_semana = Column(Integer)
    hora_entrada = Column(Time)
    hora_fin = Column(Time)
    curso_id = Column(Integer, ForeignKey('curso.id'))
    profesor_id = Column(Integer, ForeignKey('profesor.id'))
    curso = relationship('Curso', back_populates='horario_curso')
    profesor = relationship('Profesor', back_populates='horario_profesor')
    def __repr__(self):
        return "{} {}".format(self.nombre)
class CursoReporte(object):
    def __init__(self, archivo):
        self.archivo = archivo
    def export(self, curso):
        alumnado = curso.alumno
        with open(self.archivo, 'w') as a_file:
            writer = csv.writer(a_file)
            for alumno in alumnado:
                writer.writerow([str(alumno)])
class CursoHorarioReporte(object):
    def __init__(self, archivo):
        self.archivo = archivo
    def export(self, curso):
        horarios = curso.horario_curso
        with open(self.archivo, 'w') as a_file:
            writer = csv.writer(a_file)
            for horario in horarios:
                writer.writerow([horario.dia_de_semana, horario.hora_entrada, horario.hora_fin, horario.profesor])
class ProfesorHorarioReporte(object):
    def __init__(self, archivo):
        self.archivo = archivo
    def export(self, profesor):
        horarios = profesor.horario_profesor
        with open(self.archivo, 'w') as a_file:
            writer = csv.writer(a_file)
            for horario in horarios:
                writer.writerow([horario.dia_de_semana, horario.hora_entrada, horario.hora_fin, horario.curso.nombre])

Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()
R_vasquez=Profesor(nombre='Robinson Ausberto',apellido='Vasquez Olano')
A_altamirano=Profesor(nombre='Alejandra Beatriz',apellido='Altamirano Macetas')
J_tello=Profesor(nombre='Jose Luis',apellido='Tello Rojas')
optica=Curso(nombre='Optica Clasica')
mecanica_clasica=Curso(nombre='Mecanica Clasica')
metodos=Curso(nombre='Metodos Matematicos para Fisicos 2')
primer_alumno = Alumno(nombre='Manuel', apellido='Garcia', curso=optica)
segundo_alumno = Alumno(nombre='David', apellido='Neira', curso=mecanica_clasica)
tercer_alumno = Alumno(nombre='Diego', apellido='Saldarriaga', curso=metodos)
cuarto_alumno = Alumno(nombre='Sergei', apellido='Calle', curso=optica)
quinto_alumno = Alumno(nombre='Maria', apellido='Tuñoque', curso=mecanica_clasica)
optica.profesor.append(R_vasquez)
optica.profesor.append(A_altamirano)
mecanica_clasica.profesor.append(R_vasquez)
mecanica_clasica.profesor.append(J_tello)
metodos.profesor.append(J_tello)
metodos.profesor.append(A_altamirano)
hora1 = datetime.time(8, 0, 0)
hora2 = datetime.time(10, 0, 0)
hora3 = datetime.time(12, 0, 0)
hora4 = datetime.time(14, 0, 0)
hora5 = datetime.time(16, 0, 0)
horario1 = Horario(dia_de_semana=1, hora_entrada=hora1, hora_fin=hora2, curso=optica, profesor=R_vasquez)
horario2 = Horario(dia_de_semana=1, hora_entrada=hora2, hora_fin=hora3,curso=metodos, profesor=A_altamirano)
horario3 = Horario(dia_de_semana=1, hora_entrada=hora4, hora_fin=hora5, curso=mecanica_clasica, profesor=J_tello)
horario4 = Horario(dia_de_semana=3, hora_entrada=hora1, hora_fin=hora2, curso=metodos, profesor=J_tello)
horario5 = Horario(dia_de_semana=3, hora_entrada=hora2, hora_fin=hora3, curso=mecanica_clasica, profesor=R_vasquez)
horario6 = Horario(dia_de_semana=3, hora_entrada=hora4, hora_fin=hora5, curso=optica, profesor=A_altamirano)
horario7 = Horario(dia_de_semana=5, hora_entrada=hora1, hora_fin=hora2, curso=mecanica_clasica, profesor=R_vasquez)
horario8 = Horario(dia_de_semana=5, hora_entrada=hora2, hora_fin=hora3, curso=optica, profesor=A_altamirano)
horario9 = Horario(dia_de_semana=5, hora_entrada=hora4, hora_fin=hora5, curso=metodos, profesor=J_tello)
session.add_all([R_vasquez,A_altamirano,J_tello])
session.add_all([optica,mecanica_clasica,metodos])
session.add_all([primer_alumno,segundo_alumno,tercer_alumno,cuarto_alumno,quinto_alumno])
session.add_all([optica,mecanica_clasica,metodos])
session.add_all([horario1,horario2,horario3,horario4,horario5,horario6,horario7,horario8,horario9])
session.commit()
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
CursoReporte('{}.csv'.format(optica.nombre)).export(optica)
CursoReporte('{}.csv'.format(mecanica_clasica.nombre)).export(mecanica_clasica)
CursoReporte('{}.csv'.format(metodos.nombre)).export(metodos)
CursoHorarioReporte('horario_{}.csv'.format(optica.nombre)).export(optica)
CursoHorarioReporte('horario_{}.csv'.format(mecanica_clasica.nombre)).export(mecanica_clasica)
CursoHorarioReporte('horario_{}.csv'.format(metodos.nombre)).export(metodos)
ProfesorHorarioReporte('horario_{}.csv'.format(R_vasquez)).export(R_vasquez)
ProfesorHorarioReporte('horario_{}.csv'.format(A_altamirano)).export(A_altamirano)
ProfesorHorarioReporte('horario_{}.csv'.format(J_tello)).export(J_tello)
