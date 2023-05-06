import csv
from claseMaterias import Materia

class manejadorMaterias:
    
    def __init__(self):
        self.__listaMaterias = []
    
    def cargarMaterias(self):

        archivo = open('materiasAprobadas.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                dni = int(fila[0])
                nom = str(fila[1])
                fec = str(fila[2])
                nota = int(fila[3])
                apro = str(fila[4])
                instancia = Materia(dni, nom, fec, nota, apro)
                self.__listaMaterias.append(instancia)
                #print("se ingreso una materia")
        archivo.close

        return self.__listaMaterias
     
    def promedioSinAplazo(self,xdni):
        #notas mayor o igual a 4
        cont = 0
        acum = 0
        for materia in range (len(self.__listaMaterias)):
            if(xdni == self.__listaMaterias[materia].getDni() and self.__listaMaterias[materia].getNota() >= 4):
                acum += self.__listaMaterias[materia].getNota()
                cont += 1
        
        if cont == 0:
            promedio = 0
        else:
            promedio = acum/cont
        return promedio


    def promedioConAplazo(self, xdni):
        cont = 0
        acum = 0
        for materia in range (len(self.__listaMaterias)):
            if xdni == self.__listaMaterias[materia].getDni():
                acum += self.__listaMaterias[materia].getNota()
                cont += 1
        promedio = acum/cont
        return promedio


    def mostrarLista(self):
        for materia in range(len(self.__listaMaterias)):
            print(str(self.__listaMaterias[materia]))

    def cantElementos(self):
        return len(self.__listaMaterias)
    
    def unaNota(self,indice):
        return self.__listaMaterias[indice].getNota()
    
    def unaFecha(self,indice):
        return self.__listaMaterias[indice].getFecha()
    
    def unDni(self,indice):
        return self.__listaMaterias[indice].getDni()
    
    def unaMateria(self,indice):
        return self.__listaMaterias[indice].getNombre()