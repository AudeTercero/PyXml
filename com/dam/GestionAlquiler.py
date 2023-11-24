import VerificationExceptions
import GestionXML


def iniAlquiler():
    dni = None
    fechaIni = None
    fechaFin = None
    kmIni = None
    intentos = 0
    salir = False
    while (intentos < 3 and salir is False):
        try:
            if (dni is None):
                aux = input('Introduce el dni del cliente:\n')
                VerificationExceptions.dniFormat(aux)
                dni = aux
                intentos = 0
            if (fechaIni is None):
                aux = input('Introduce la fecha de inicio del alquiler(yyyy-mm-dd):\n')
                VerificationExceptions.formatoFecha(aux)
                fechaIni = aux
                intentos = 0
            if (fechaFin is None):
                aux = input('Introduce la fecha final del alquiler(yyyy-mm-dd):\n')
                VerificationExceptions.formatoFecha(aux)
                fechaFin = aux
                intentos = 0
            if (kmIni is None):
                aux = input('Introduce los kilometros iniciales:\n')
                VerificationExceptions.esNum(aux)
                kmIni = aux
                intentos = 0
                salir = True
        except VerificationExceptions.MisExceptions as err:
            intentos += 1
            print(err)
    if (intentos < 3):
        GestionXML.crearAlquiler(dni, fechaIni, fechaFin, kmIni)
        print("Guardado correctamente")
    else:
        print("Se han superado el maximo de errores.")


def finAlquiler():
    fechaDevo = None
    kmFin = None
    intentos = 0
    try:
        if(fechaDevo is None):
            aux = input('Introduce la fecha de la devolucion del vehiculo(yyyy-mm-dd):\n')
            VerificationExceptions.formatoFecha(aux)
            fechaDevo = aux
            intentos = 0
        if(kmFin is None):
            aux = input('Introduce el kilometraje final:\n')
            VerificationExceptions.esNum(aux)
            kmFin = aux
            intentos = 0

    except VerificationExceptions.MisExceptions as err:
        intentos += 1
        print(err)


    # precioFin = (fechaIni - fechaDevo) * tarifaVehiculo
    # recargo = (fechaFin - fechaDevo) * costPenalizacion
    estado = 'Finalizado'


def modificar():
    lista = {}

    # aqui se puede meter opciones de switch para luego hacer cosas segun las opciones que metamos
    # se podria usar una lista para asi tener los vehiculos con un menu independiente al numero de vehiculos mostrados para luego mostrarlos
    switch_dic = {
        'opc1': buscarDni(),
    }
    # hay que probarlo
    resulado = switch_dic.get(lista, 'opc1')
    print()


def buscarMatricula():
    print()


def buscarDni():
    print()


def mostrarTodos():
    GestionXML.mostrarTodoAlq()


def menu():
    salir = True
    while (salir):
        opc = input(
            "\t****GESTION ALQUILER****\n 1. Alquilar Vehiculo\n 2. Finalizar Alquiler\n 3. Modificar\n 4. Buscar por matricula \n 5. Buscar por dni del cliente\n 6. Mostrar alquileres \n  0. Salir\n ")

        if opc == "1":
            iniAlquiler()
        elif opc == "2":
            finAlquiler()
        elif opc == "3":
            modificar()
        elif opc == "4":
            buscarMatricula()
        elif opc == "5":
            buscarDni()
        elif opc == "6":
            mostrarTodos()
        elif opc == "0":
            print("Saliendo...")
            salir = False
        else:
            print("Esa opcion no existe")
