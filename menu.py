class menuOpciones:
    
    def __init__(self):
        self.__opcion = None
    
    def opciones(self, arreglo, lista):
        
        while self.__opcion != 4:
            print("Menu de opciones: ")
            print("1)- Informar promedio de un alumno con y sin aplazos")
            print("2)- Informar estudiantes que aprobaron una materia en forma promocional")
            print("3)- Obtener listado de alumnos")
            print("4)- Salir")
            self.__opcion = (int(input("Ingrese una opcion: ")))
            
            if self.__opcion == 1:
                dniAlumno = int(input("Ingrese el dni de un alumno para informar promedio: "))
                bandera = arreglo.buscarAlumno(dniAlumno)
                if bandera == True:
                    print("Se encontro el alumno")
                    promSA = lista.promedioSinAplazo(dniAlumno)
                    promCA = lista.promedioConAplazo(dniAlumno)
                    if promSA == 0:
                        print("Alumno {}, promedio con aplazo {:.2f} y no posee un promedio sin aplazo ya que no tiene ninguna nota mayor a 4".format(dniAlumno,promCA))
                    else:
                        print("Alumno {}, promedio con Aplazo {:.2f}, promedio sin aplazo {:.2f}".format(dniAlumno,promCA,promSA))
                else:
                    print("El alumno ingresado no esta en la lista")
            
            elif self.__opcion == 2:
                nomMateria = str(input("Ingrese el nombre de una materia para mostrar alumnos que la promocionaron: "))
                arreglo.listarEstudiantes(nomMateria, lista)
            
            elif self.__opcion == 3:
                print("|---|--|-| LISTADO DE ALUMNOS |-|--|---|")
                alumnosOrdenados = arreglo.listaOrdenada()
                arreglo.mostrarAlumnos(alumnosOrdenados)
            elif self.__opcion == 4:
                print("Salio del programa")

            else:
                print("Opcion no valida, volver a ingresar")