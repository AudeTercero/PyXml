import GestionXML
import VerificationExceptions


def alta():
    """
    Metodo para guardar nuevos vehiculos
    :return:
    """

    xmlPath = "vehiculos.xml"
    salir = False
    salir_sin_guardar = False
    cont = 0

    # Comprobaciones pertinentes
    while not salir and not salir_sin_guardar:
        if not cont == 3:
            matricula = input("Ingrese la matricula del vehículo o pulse 0 para salir: ")
            if (matricula == "0"):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    if GestionXML.existe_matricula(xmlPath, matricula):
                        print("Ya existe un vehiculo con esa matricula.")
                        cont += 1

                    else:
                        VerificationExceptions.hayAlgo(matricula)
                        VerificationExceptions.matFormat(matricula)
                        salir = True

                except VerificationExceptions.MisExceptions as err:
                    cont += 1
                    print(err)
        else:
            print("\nHas llegado al limite de intentos.")
            salir_sin_guardar = True

    salir = False
    cont = 0
    while not salir and not salir_sin_guardar:
        if not cont == 3:
            marca = input("Ingrese la marca del vehiculo o pulse 0 para salir: ")
            if (marca == "0"):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(marca)
                    salir = True

                except VerificationExceptions.MisExceptions as err:
                    cont += 1
                    print(err)
        else:
            print("\nHas llegado al limite de intentos.")
            salir_sin_guardar = True

    salir = False
    cont = 0
    while not salir and not salir_sin_guardar:
        if not cont == 3:
            modelo = input("Ingrese el modelo del vehiculo o pulse 0 para salir: ")
            if (modelo == "0" or cont == 3):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(modelo)
                    salir = True

                except VerificationExceptions.MisExceptions as err:
                    cont += 1
                    print(err)
        else:
            print("\nHas llegado al limite de intentos.")
            salir_sin_guardar = True

    salir = False
    cont = 0
    while not salir and not salir_sin_guardar:
        if not cont == 3:
            anioFabricacion = input("Ingrese el anio de fabricacion del vehiculo o pulse 0 para salir: ")
            if (anioFabricacion == "0" or cont == 3):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(anioFabricacion)
                    VerificationExceptions.formatoFecha(anioFabricacion)
                    salir = True

                except VerificationExceptions.MisExceptions as err:
                    cont += 1
                    print(err)
        else:
            print("\nHas llegado al limite de intentos.")
            salir_sin_guardar = True

    salir = False
    cont = 0
    while not salir and not salir_sin_guardar:
        if not cont == 3:
            tarifaDia = input("Ingrese la tarifa por día del vehiculo o pulse 0 para salir: ")
            if (tarifaDia == "0" or cont == 3):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(tarifaDia)
                    VerificationExceptions.esNum(tarifaDia)
                    salir = True

                except VerificationExceptions.MisExceptions as err:
                    cont += 1
                    print(err)
        else:
            print("\nHas llegado al limite de intentos.")
            salir_sin_guardar = True

    salir = False
    cont = 0
    while not salir and not salir_sin_guardar:
        if not cont == 3:
            estado = input(
                "Ingrese el estado del vehiculo (disponible, alquilado o mantenimiento) o pulse 0 para salir: ")
            if (estado == "0"):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.disp_correcto(estado)
                    salir = True

                except VerificationExceptions.MisExceptions as err:
                    cont += 1
                    print(err)
        else:
            print("\nHas llegado al limite de intentos.")
            salir_sin_guardar = True

    if salir_sin_guardar:
        print("Saliendo...")
    else:
        GestionXML.aniadir_vehiculo(matricula, marca, modelo, anioFabricacion, tarifaDia, estado, xmlPath)


def baja():
    """
    Metodo para eliminar vehiculos guardados
    :return:
    """

    xmlPath = "vehiculos.xml"
    cont = 0
    salir = False
    matricula = ""

    # Comprobaciones pertinentes
    if not GestionXML.hay_vehiculos(xmlPath):
        print("No hay vehiculos guardados, saliendo...")
    else:
        while not salir:
            if not cont == 3:
                matricula = input("Ingrese la matricula del vehiculo o pulse 0 para salir: ")
                if (matricula == "0"):
                    print("Saliendo...")
                    salir = True

                elif matricula == "":
                    print("No has introducido nada.")
                    cont += 1
                else:
                    try:

                        if not GestionXML.existe_matricula(xmlPath, matricula):
                            print("No existe ningun vehiculo con esa matricula.")
                            cont += 1

                        else:
                            VerificationExceptions.hayAlgo(matricula)
                            VerificationExceptions.matFormat(matricula)
                            salir = True

                    except VerificationExceptions.MisExceptions as err:
                        cont += 1
                        print(err)
            else:
                salir = True
                print("Has llegado al limite de intentos, saliendo...")

            if cont < 3 and matricula != "0" and matricula != "":
                salir = False

                if GestionXML.esta_disponible(xmlPath, matricula):
                    while not salir:
                        op = input("Seguro que quieres borrar el vehiculo? [S/N]").lower()
                        if (op == "s"):
                            GestionXML.eliminar_vehiculo(matricula, xmlPath)
                            salir = True
                        elif (op == "n"):
                            print("Saliendo...")
                            salir = True
                        else:
                            print("Opcion no valida.")
                else:
                    print("El vehiculo no esta disponible en estos momentos y no se puede borrar. \nSaliendo...")


def modificar():
    """
    Metodo para modificar los atributos de los vehiculos guardados
    :return:
    """

    xml_path = "vehiculos.xml"
    cont = 0
    salir = False
    salir_sin_guardar = False
    matricula = ""

    # Comprobaciones pertinentes
    if not GestionXML.hay_vehiculos(xml_path):
        print("Saliendo...")
    else:
        while not salir:
            matricula = input("Ingrese la matricula del vehiculo o pulse 0 para salir: ")
            if matricula == "0":
                salir = True
                salir_sin_guardar = True
            else:
                try:
                    if not GestionXML.existe_matricula(xml_path, matricula):
                        print("No existe ningun vehiculo con esa matricula.")
                        cont += 1
                    elif cont == 3:
                        print("Has alcanzado el limite de intentos, saliendo...")
                        salir = True
                    else:
                        VerificationExceptions.hayAlgo(matricula)
                        VerificationExceptions.matFormat(matricula)
                        salir = True

                except VerificationExceptions.MisExceptions as err:
                    cont += 1
                    print(err)

        if cont < 3 and not salir_sin_guardar:
            GestionXML.modificar_vehiculo(matricula, xml_path)



def buscar():
    """
    Metodo que permite mostrar los atributos de un vehiculo solicitado
    :return:
    """

    xml_path = "vehiculos.xml"
    cont = 0
    salir = False

    # Comprobaciones pertinentes
    if not GestionXML.hay_vehiculos(xml_path):
        print("Saliendo...")
    else:
        while not salir:
            matricula = input("Ingrese la matricula del vehiculo o pulse 0 para salir: ")
            if matricula == "0":
                salir = True
            else:
                try:
                    if not GestionXML.existe_matricula(xml_path, matricula):
                        print("No existe ningun vehiculo con esa matricula.")
                        cont += 1
                    elif cont == 3:
                        salir = True
                    else:
                        VerificationExceptions.hayAlgo(matricula)
                        VerificationExceptions.matFormat(matricula)
                        salir = True

                except VerificationExceptions.MisExceptions as err:
                    cont += 1
                    print(err)

        # Mandamos a buscar el vehiculo por matricula con el metodo buscar_vehiculo
        if cont == 3:
            print("Has alcanzado el limite de intentos")
        else:
            GestionXML.buscar_vehiculo(matricula, xml_path)


def mostrar():
    """
    Metodo que muestra los atributos de todos los vehiculos guardados
    :return:
    """

    xml_path = "vehiculos.xml"

    if not GestionXML.hay_vehiculos(xml_path):
        print("Saliendo...")
    else:
        GestionXML.leer_vehiculos(xml_path)


def menu():
    """
    Metodo que sirve de menu para acceder a las distintas funciones de la gestion de vehiculos
    :return:
    """

    salir = True
    while (salir):
        opc = input(
            "\t****GESTION VEHICULOS****\n 1. Alta\n 2. Baja\n 3. Modificar\n 4. Buscar \n 5. Mostrar todos\n 0. Salir\n ")
        if opc == "1":
            alta()
        elif opc == "2":
            baja()
        elif opc == "3":
            modificar()
        elif opc == "4":
            buscar()
        elif opc == "5":
            mostrar()
        elif opc == "0":
            print("Saliendo...")
            salir = False
        else:
            print("Esa opcion no existe")
