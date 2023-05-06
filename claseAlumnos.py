class Alumno:
    def __init__(self, dni = 0, apellido = '', nombre = '', carrera = '', anio = 0):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__carrera = carrera
        self.__anio = anio

    def getDni(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getAnio(self):
        return self.__anio
    
    def __lt__(self, otro):
        return (self.__anio, self.__apellido, self.__nombre) < (otro.getAnio(), otro.getApellido(), otro.getNombre())

    def __str__(self):
        cadena = str(self.__anio) +" Año" +", "+ self.__carrera +", "+ self.__nombre +" "+ self.__apellido +", "+ str(self.__dni)
        return cadena