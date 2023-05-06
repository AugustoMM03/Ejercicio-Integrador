class Materia:
    def __init__(self, dni = 0, nombre = '', fecha = '', nota = 0, aprobacion = ''):
        self.__dni = dni
        self.__nombre = nombre
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = aprobacion

    def getDni(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def getFecha(self):
        return self.__fecha

    def getNota(self):
        return self.__nota
    
    def getAprobacion(self):
        return self.__aprobacion
    
    def __str__(self):
        cadena = str(self.__dni) +","+ self.__nombre +","+ self.__fecha +","+ self.__nota +","+ self.__aprobacion
        return cadena
    