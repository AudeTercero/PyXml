import VerificationExceptions


def iniAlquiler():
    dni = None
    fechaIni = None
    fechaFin = None
    kmIni = None
    intentos = 0
    while (intentos < 3):
        try:
            if (dni is None):
                dni = input('Introduce el dni del cliente:\n')
                VerificationExceptions.dniFormat(dni)
            if (fechaIni is None):
                fechaIni = input('Introduce la fecha de inicio del alquiler(yyyy-mm-dd):\n')
                VerificationExceptions.formatoFecha(fechaIni)
            if (fechaFin is None):
                fechaFin = input('Introduce la fecha final del alquiler(yyyy-mm-dd):\n')
                VerificationExceptions.formatoFecha(fechaFin)
            if (kmIni is None):
                kmIni = input('Introduce los kilometros iniciales:\n')
                VerificationExceptions.esNum(kmIni)
                estado = 'Activo'
        except VerificationExceptions.MisExceptions as err:
            intentos += 1
            print(err)
            if (fechaIni is None and fechaFin is None and kmIni is None):
                dni = None
            elif (dni is not None and fechaIni is not None and fechaFin is None):
                fechaIni = None
            elif (fechaFin is not None and kmIni is None):
                fechaFin = None
            elif (kmIni is not None):
                kmIni = None


def finAlquiler():
    fechaDevo = input('Introduce la fecha de la devolucion del vehiculo(yyyy-mm-dd):\n')
    kmFin = input('Introduce el kilometraje final:\n')
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
    #hay que probarlo
    resulado = switch_dic.get(lista,'opc1')
    print()


def buscarMatricula():
    print()


def buscarDni():
    print()


def mostrarTodos():
    print()


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
