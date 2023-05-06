from menu import menuOpciones
from manejadorAlumnos import manejadorAlumnos as MA
from manejadorMaterias import manejadorMaterias as MM


def test():
    arregloAlumnos = MA()
    arregloAlumnos.cargarAlumnos()
    listaMaterias = MM()
    listaMaterias.cargarMaterias()
    menu = menuOpciones()
    menu.opciones(arregloAlumnos, listaMaterias)

if __name__ == "__main__":
    test()