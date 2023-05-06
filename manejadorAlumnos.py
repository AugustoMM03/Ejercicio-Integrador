import numpy as np
import csv
from claseAlumnos import Alumno

class manejadorAlumnos:
    def __init__(self, dimension = 8):
        self.__arregloAlumnos = np.empty((dimension), dtype = Alumno)
        self.__dimension = dimension

    def cargarAlumnos(self):
        archivo = open('alumnos.csv')
        cabecera = True
        reader = csv.reader(archivo, delimiter = ';')
        indice = 0
        for fila in reader:
            if cabecera:
                cabecera = not cabecera
            else:
                dni = int(fila[0])
                nom = str(fila[1])
                ap = str(fila[2])
                car = str(fila[3])
                anio = int(fila[4])
                instancia = Alumno (dni,nom,ap,car,anio)
                self.__arregloAlumnos[indice] = instancia
                indice += 1
        archivo.close
        return self.__arregloAlumnos
    
    def buscarAlumno(self,xdni):
        bandera = False
        i = 0
        while i < self.__dimension:
            if (self.__arregloAlumnos[i].getDni() == xdni):
                bandera = True
            i += 1
        return bandera
    
    def listarEstudiantes(self,materia, listamaterias):
        print("DNI\t\tApellido y nombre\tFecha\tNota\tAño que cursa")
        tamanolista = listamaterias.cantElementos()
        for m in range(tamanolista):
            for i in range(self.__dimension):
                if self.__arregloAlumnos[i].getDni() == listamaterias.unDni(m) and listamaterias.unaNota(m) >= 7 and materia == listamaterias.unaMateria(m):
                    print("{}\t{} {}\t\t{}\t{}\t{}".format(self.__arregloAlumnos[i].getDni(), self.__arregloAlumnos[i].getApellido(), self.__arregloAlumnos[i].getNombre(), listamaterias.unaFecha(m), listamaterias.unaNota(m), self.__arregloAlumnos[i].getAnio()))


    def listaOrdenada(self):
        alumnosOrdenados = sorted(self.__arregloAlumnos)
        return alumnosOrdenados


    def mostrarAlumnos(self, ordenados):
        for i in range (self.__dimension):
            print(ordenados[i])