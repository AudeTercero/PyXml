from pathlib import Path
import VerificationExceptions
import GestionXML


def iniAlquiler():
    """
    Funcion para dar de alta un alquiler con los datos para ello
    :return:
    """
    dni = None
    fechaIni = None
    fechaFin = None
    kmIni = None
    intentos = 0
    salir = False
    idCoche = cochesDisp()
    if (idCoche != -1):
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
                    VerificationExceptions.dife_fechas(fechaIni, aux)
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
    else:
        intentos = 3
    if (intentos < 3):
        GestionXML.crearAlquiler(dni, fechaIni, fechaFin, kmIni, idCoche)
        print("Guardado correctamente")
    else:
        print("Se han superado el maximo de errores.")


def cochesDisp():
    """
    Funcion que muestra un listado de vehiculos disponibles para que elijas uno
    :return: Retorna la id del vehiculo seleccionado o -1 en caso de que se falle
    """
    dicCoches = GestionXML.listado_coches_disponibles()
    opcCorrect = False
    cont = 0
    while (opcCorrect is False and cont < 3):
        for clave, contenido in dicCoches.items():
            print(
                f'Id Vehiculo: {clave} [ Matricula: {contenido.get('mat')}, Marca: {contenido.get('marca')}, Modelo: {contenido.get('modelo')}]')
            print('++++++++++++++++++++++++++++++')
        opc = input("Seleccion la id del vehiculo que quieres alquilar:")
        for clave in dicCoches.keys():
            if (clave == opc):
                opcCorrect = True
        if (opcCorrect == True):
            return opc
        else:
            print('Esa id no esta en la lista')
    return -1


def finAlquiler():
    """
    Funcion para finalizar un alquiler introduciendo los datos de finalizacion del alquiler
    :return:
    """
    fechaDevo = None
    kmFin = None
    idAlq = None
    intentos = 0
    opcCorrect = False
    while (intentos < 3 and opcCorrect is False):
        try:
            idAlq = alquilerDni()
            if (idAlq != -1):
                if (fechaDevo is None):
                    aux = input('Introduce la fecha de la devolucion del vehiculo(yyyy-mm-dd):\n')
                    VerificationExceptions.formatoFecha(aux)
                    fecha_ini = GestionXML.obt_elemento("alquileres.xml", idAlq, 'alquiler', 'fecha_inicio')
                    VerificationExceptions.dife_fechas(fecha_ini, aux)
                    fechaDevo = aux
                    intentos = 0
                if (kmFin is None):
                    aux = input('Introduce el kilometraje final:\n')
                    VerificationExceptions.esNum(aux)
                    kmFin = aux
                    intentos = 0
                opcCorrect = True
            else:
                intentos = 3
        except VerificationExceptions.MisExceptions as err:
            intentos += 1
            print(err)
    if (intentos < 3):
        GestionXML.finAlquiler(fechaDevo, kmFin, idAlq)


def alquilerDni():
    """
    Funcion que pide un dni para buscarlo en el fichero xml y muestra todos los que hay para elegir uno
    :return: Retorna la id del alquiler seleccionado o -1 en caso de que se falle
    """
    opcCorrect = False
    cont = 0
    dni = None
    while (opcCorrect is False and cont < 3):
        try:
            if (dni is None):
                aux = input('Introduce el dni del cliente o 0 para salir:')
                if (aux != '0'):
                    VerificationExceptions.dniFormat(aux)
                    dni = aux
                    cont = 0
                    dic_alqui = GestionXML.alquiDisp(dni)
                    if (not dic_alqui):
                        print('No hay alquileres activos para ese dni')
                        dni = None
                        cont += 1
                    else:
                        for clave, contenido in dic_alqui.items():
                            print(
                                f'Id Alquiler: {clave} [Id Vehiculo: {contenido.get('Id_Vehiculo')}, DNI Cliente: {contenido.get('dni')}, Fecha Inicio: {contenido.get('Fecha_Inicio')}]')
                            print('++++++++++++++++++++++++++++++')
                        opc = input("Seleccion la id del alquiler:")
                        for clave in dic_alqui.keys():
                            if (clave == opc):
                                opcCorrect = True
                        if (opcCorrect == True):
                            return opc
                        else:
                            print('Esa id no esta en la lista')
                            dni = None
                            cont += 1
                else:
                    print('Saliendo...')
                    return -2
        except VerificationExceptions.MisExceptions as err:
            cont += 1
            print(err)
    return -1


def modificar():
    """
    Funcion para modificar los textos de los elementos del fichero de alquileres
    :return:
    """
    salir = False
    idAlq = alquilerDni()
    if (idAlq != -1):
        while (salir is False):
            opc = input(''' 
            ******* MODIFICACION ALQUILER *******
            1.Id del Alquiler
            2.Id del Vehiculo
            3.Dni cliente
            4.Fecha Inicio del Alquiler
            5.Fecha Fin del Alquiler
            6.Kilometraje inicial
            0.Salir
            ''')
            if opc == "1":
                fallos = 0
                id_nueva = None
                while (fallos < 3 and id_nueva is None):
                    try:
                        aux = input('Escriba la nueva id:')
                        VerificationExceptions.esNum(aux)
                        if (GestionXML.existe_id('alquileres.xml', aux, 'alquiler') is False):
                            id_nueva = aux
                        else:
                            print("Ya existe un alquiler con esa id")
                            fallos += 1

                    except VerificationExceptions.MisExceptions as err:
                        print(err)
                        fallos += 1
                if (fallos < 3):
                    GestionXML.modificar_atributo('alquileres.xml', 'alquiler', idAlq, id_nueva)
                else:
                    print("No puedes fallar mas de 3 veces")
            elif opc == "2":
                fallos = 0
                id_nueva = None
                while (fallos < 3 and id_nueva is None):
                    try:
                        aux = input(f'Escriba la nueva id_vehiculo:')
                        VerificationExceptions.esNum(aux)
                        if (GestionXML.existe_id('vehiculos.xml', aux, 'vehiculo') is True):
                            id_nueva = aux
                        else:
                            print("Ya existe un vehiculo con esa id")
                            fallos += 1

                    except VerificationExceptions.MisExceptions as err:
                        print(err)
                        fallos += 1
                if (fallos < 3):
                    GestionXML.modificar_etiqueta('alquileres.xml', 'alquiler', 'id_vehiculo', idAlq, id_nueva)
                else:
                    print("No puedes fallar mas de 3 veces")
            elif opc == "3":
                fallos = 0
                dni = None
                while (fallos < 3 and dni is None):
                    try:
                        aux = input(f'Escriba el nuevo dni:')
                        VerificationExceptions.dniFormat(aux)
                        dni = aux
                    except VerificationExceptions.MisExceptions as err:
                        print(err)
                        fallos += 1
                if (fallos < 3):
                    GestionXML.modificar_etiqueta('alquileres.xml', 'alquiler', 'dni', idAlq, dni)
                else:
                    print("No puedes fallar mas de 3 veces")
            elif opc == "4":
                fallos = 0
                fecha = None
                while (fallos < 3 and fecha is None):
                    try:
                        aux = input(f'Escriba la nueva {'fecha_inicio'}:')
                        VerificationExceptions.formatoFecha(aux)
                        fecha = aux
                    except VerificationExceptions.MisExceptions as err:
                        print(err)
                        fallos += 1
                if (fallos < 3):
                    GestionXML.modificar_etiqueta('alquileres.xml', 'alquiler', 'fecha_inicio', idAlq, fecha)
                else:
                    print("No puedes fallar mas de 3 veces")
            elif opc == "5":
                fallos = 0
                fecha = None
                while (fallos < 3 and fecha is None):
                    try:
                        aux = input(f'Escriba la nueva {'fecha_final'}:')
                        fecha_ini = GestionXML.obt_elemento("alquileres.xml", idAlq, 'alquiler', 'fecha_inicio')
                        VerificationExceptions.formatoFecha(aux)
                        VerificationExceptions.dife_fechas(fecha_ini, aux)
                        fecha = aux
                    except VerificationExceptions.MisExceptions as err:
                        print(err)
                        fallos += 1
                if (fallos < 3):
                    GestionXML.modificar_etiqueta('alquileres.xml', 'alquiler', 'fecha_final', idAlq, fecha)
                else:
                    print("No puedes fallar mas de 3 veces")
            elif opc == "6":
                fallos = 0
                km = None
                while (fallos < 3 and km is None):
                    try:
                        aux = input(f'Escriba los nuevos kilometros iniciales:')
                        VerificationExceptions.esNum(aux)
                        km = aux
                    except VerificationExceptions.MisExceptions as err:
                        print(err)
                        fallos += 1
                if (fallos < 3):
                    GestionXML.modificar_etiqueta('alquileres.xml', 'alquiler', 'kilometros_inicio', idAlq, km)
                else:
                    print("No puedes fallar mas de 3 veces")
            elif opc == "0":
                print("Saliendo...")
                salir = True
            else:
                print("Esa opcion no existe")
    elif (idAlq == -1):
        print('No puedes fallar mas de 3 veces')


def buscarMatricula():
    """
    Funcion que muestra los alquileres de un determinado vehiculo que se busca por dni
    :return:
    """
    fallos = 0
    salir = False
    id_veh = None
    matricula = None
    while (fallos < 3 and salir is False):
        matricula = input("Introduzca la matricula del vehiculo o pulse 0 para salir:")
        if (matricula != '0'):
            try:
                VerificationExceptions.matFormat(matricula)
                id_veh = GestionXML.obtIdVe(matricula)
                if (int(id_veh) == -1):
                    fallos += 1
                    print("Esa matricula no existe")
                else:
                    salir = True

            except VerificationExceptions.MisExceptions as err:
                print(err)
                fallos += 1
        else:
            salir = True
    if (fallos < 3 and matricula != '0'):
        GestionXML.mostrar_por_elemento('id_vehiculo', id_veh)
    elif (fallos == 3):
        print("Se han cometido mas de 3 fallos")
    else:
        print("Saliendo...")


def buscarDni():
    """
    Funcion para buscar los alquileres realizados con ese dni
    :return:
    """
    dni = None
    fallos = 0
    salir = False
    while (fallos < 3 and salir is False):
        dni = input("Introduzca el dni del cliente o pulse 0 para salir:")
        if (dni != '0' and salir is False):
            try:
                VerificationExceptions.dniFormat(dni)
                salir = True
            except VerificationExceptions.MisExceptions as err:
                print(err)
                fallos += 1
        else:
            salir = True
    if (fallos < 3 and dni != '0'):
        GestionXML.mostrar_por_elemento('dni', dni)

    elif (fallos == 3):
        print("Se han cometido mas de 3 fallos")
    else:
        print("Saliendo...")


def mostrarTodos():
    """
    Funcion para mostrar todos los alquileres
    :return:
    """
    GestionXML.mostrarTodoAlq()


def menu():
    """
    Funcion para el menu de gestion de alquileres
    :return:
    """
    if (Path('vehiculos.xml').exists()):
        salir = True
        while (salir):
            opc = input(
                "\t****GESTION ALQUILER****\n 1. Alquilar Vehiculo\n 2. Finalizar Alquiler\n 3. Modificar\n 4. Buscar por matricula \n 5. Buscar por dni del cliente\n 6. Mostrar alquileres \n 0. Salir\n ")
            if opc == "1":
                if (GestionXML.diponibles() is True):
                    iniAlquiler()
                else:
                    print("No hay coches disponibles")
            elif opc == "2":
                if (Path('alquileres.xml').exists() and GestionXML.alquileres_activos() is True):
                    finAlquiler()
                else:
                    print("No hay alquileres activos")
            elif opc == "3":
                if (Path('alquileres.xml').exists() and GestionXML.alquileres_activos() is True):
                    modificar()
                else:
                    print("No hay alquileres activos. Solo se pueden modificar los alquileres que estan activos")

            elif opc == "4":
                if (Path('alquileres.xml').exists()):
                    buscarMatricula()
                else:
                    print("No hay alquileres aun guardados")
            elif opc == "5":
                if (Path('alquileres.xml').exists()):
                    buscarDni()
                else:
                    print("No hay alquileres aun guardados")

            elif opc == "6":
                if (Path('alquileres.xml').exists()):
                    mostrarTodos()
                else:
                    print("No hay alquileres aun guardados")

            elif opc == "0":
                print("Saliendo...")
                salir = False
            else:
                print("Esa opcion no existe")
    else:
        print("Aun no hay vehiculos guardados")
