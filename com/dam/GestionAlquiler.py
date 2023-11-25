from pathlib import Path
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree
import VerificationExceptions
import GestionXML


def iniAlquiler():
    dni = None
    fechaIni = None
    fechaFin = None
    kmIni = None
    idCoche = None
    intentos = 0
    salir = False
    while (intentos < 3 and salir is False):
        try:
            idCoche = cochesDisp()
            if (idCoche != -1):
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
            else:
                intentos = 3
        except VerificationExceptions.MisExceptions as err:
            intentos += 1
            print(err)
    if (intentos < 3):
        GestionXML.crearAlquiler(dni, fechaIni, fechaFin, kmIni, idCoche)
        print("Guardado correctamente")
    else:
        print("Se han superado el maximo de errores.")


def cochesDisp():
    dicCoches = GestionXML.cochesDisp()
    opcCorrect = False
    cont = 0
    while (opcCorrect is False and cont < 3):
        for clave, contenido in dicCoches.items():
            print(f'Id: {clave}')
            print(contenido)
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


# pide un dni para buscarlo en el fichero xml
def alquilerDni():
    dicCoches = {}
    opcCorrect = False
    cont = 0
    dni = None
    while (opcCorrect is False and cont < 3):
        try:
            if (dni is None):
                aux = input('Introduce el dni del cliente o 0 para salir:')
                if(aux != '0'):
                    VerificationExceptions.dniFormat(aux)
                    dni = aux
                    cont = 0
                    dicCoches = GestionXML.alquiDisp(dni)
                    for clave, contenido in dicCoches.items():
                        print(f'Id: {clave}')
                        print(contenido)
                        print('++++++++++++++++++++++++++++++')
                    opc = input("Seleccion la id del vehiculo que quieres alquilar:")
                    for clave in dicCoches.keys():
                        if (clave == opc):
                            opcCorrect = True
                    if (opcCorrect == True):
                        return opc
                    else:
                        print('Esa id no esta en la lista')
                        cont += 1
                else:
                    print('Saliendo...')
                    opcCorrect = True
        except VerificationExceptions as err:
            cont += 1
            print(err)
    return -1


def modificar():
    salir = False

    while (salir is False):
        idAlq = alquilerDni()
        if (idAlq != -1):
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
                modificador_ids('id', idAlq, 'alquileres.xml')
            elif opc == "2":
                modificador_ids('id_vehiculo', idAlq, 'vehiculos.xml')
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
                    GestionXML.modificar_etiqueta('dni', id_alquiler, dni)
                else:
                    print("No puedes fallar mas de 3 veces")
            elif opc == "4":
                modificador_fechas('fecha_inicio', id_alquiler)
            elif opc == "5":
                modificador_fechas('fecha_final', id_alquiler)
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
                    GestionXML.modificar_etiqueta('kilometros_inicio', idAlq, km)
                else:
                    print("No puedes fallar mas de 3 veces")
            elif opc == "0":
                print("Saliendo...")
                salir = True
            else:
                print("Esa opcion no existe")
        else:
            print('No puedes fallar mas de 3 veces')
            salir = True


def modificador_ids(etiqueta, id_alquiler, fichero):
    fallos = 0
    id_nueva = None
    while (fallos < 3 and id_nueva is None):
        try:
            aux = input(f'Escriba la nueva {etiqueta}:')
            VerificationExceptions.esNum(aux)
            if (GestionXML.existe_id(fichero, aux, etiqueta) is False):
                id_nueva = aux
            else:
                fallos += 1

        except VerificationExceptions.MisExceptions as err:
            print(err)
            fallos += 1
    if (fallos < 3):
        GestionXML.modificar_etiqueta('alquileres.xml','alquiler',etiqueta, id_alquiler, id_nueva)
    else:
        print("No puedes fallar mas de 3 veces")


def modificador_fechas(etiqueta, id_alquiler):
    fallos = 0
    fecha = None
    while (fallos < 3 and fecha is None):
        try:
            aux = input(f'Escriba la nueva {etiqueta}:')
            VerificationExceptions.formatoFecha(aux)
            fecha = aux
        except VerificationExceptions.MisExceptions as err:
            print(err)
            fallos += 1
    if (fallos < 3):
        GestionXML.modificar_etiqueta(etiqueta, id_alquiler, fecha)
    else:
        print("No puedes fallar mas de 3 veces")





def buscarMatricula():
    print()


def buscarDni():
    print()


def mostrarTodos():
    GestionXML.mostrarTodoAlq()


def menu():
    if (Path('vehiculos.xml').exists()):
        if (GestionXML.diponibles() is True):
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
