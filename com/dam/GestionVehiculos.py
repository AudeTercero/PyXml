import GestionXML
import VerificationExceptions


def alta():
    xmlPath = "vehiculos.xml"
    salir = False
    salir_sin_guardar = False
    cont = 0

    # Comprobaciones pertinentes
    while not salir:
        matricula = input("Ingrese la matricula del vehículo o pulse 0 para salir: ")
        if (matricula == "0"):
            salir_sin_guardar = True
            salir = True
        else:
            try:
                if GestionXML.existe_matricula(xmlPath, matricula):
                    print("Ya existe un vehiculo con esa matricula.")
                    cont += 1
                elif cont == 3:
                    salir_sin_guardar = True
                else:
                    VerificationExceptions.hayAlgo(matricula)
                    VerificationExceptions.matFormat(matricula)
                    salir = True

            except VerificationExceptions.MisExceptions as err:
                cont += 1
                print(err)

    salir = False
    while not salir and not salir_sin_guardar:
        cont = 0
        marca = input("Ingrese la marca del vehiculo o pulse 0 para salir: ")
        if (marca == "0"):
            salir_sin_guardar = True
            salir = True
        else:
            try:
                if cont == 3:
                    salir_sin_guardar = True
                else:
                    VerificationExceptions.hayAlgo(marca)
                    salir = True

            except VerificationExceptions.MisExceptions as err:
                cont += 1
                print(err)

    salir = False
    while not salir and not salir_sin_guardar:
        cont = 0
        modelo = input("Ingrese el modelo del vehiculo o pulse 0 para salir: ")
        if (modelo == "0"):
            salir_sin_guardar = True
            salir = True
        else:
            try:
                if cont == 3:
                    salir_sin_guardar = True
                else:
                    VerificationExceptions.hayAlgo(modelo)
                    salir = True

            except VerificationExceptions.MisExceptions as err:
                cont += 1
                print(err)

    salir = False
    while not salir and not salir_sin_guardar:
        cont = 0
        anioFabricacion = input("Ingrese el anio de fabricacion del vehiculo: ")
        if (anioFabricacion == "0"):
            salir_sin_guardar = True
            salir = True
        else:
            try:
                if cont == 3:
                    salir_sin_guardar = True
                else:
                    VerificationExceptions.hayAlgo(anioFabricacion)
                    VerificationExceptions.formatoFecha(anioFabricacion)
                    salir = True

            except VerificationExceptions.MisExceptions as err:
                cont += 1
                print(err)

    salir = False
    while not salir and not salir_sin_guardar:
        cont = 0
        tarifaDia = input("Ingrese la tarifa por día del vehiculo: ")
        if (tarifaDia == "0"):
            salir_sin_guardar = True
            salir = True
        else:
            try:
                if cont == 3:
                    salir_sin_guardar = True
                else:
                    VerificationExceptions.hayAlgo(tarifaDia)
                    VerificationExceptions.esNum(tarifaDia)
                    salir = True

            except VerificationExceptions.MisExceptions as err:
                cont += 1
                print(err)

    salir = False
    while not salir and not salir_sin_guardar:
        cont = 0
        estado = input("Ingrese el estado del vehiculo: ")
        if (estado == "0"):
            salir_sin_guardar = True
            salir = True
        else:
            try:
                if cont == 3:
                    salir_sin_guardar = True
                else:
                    VerificationExceptions.hayAlgo(estado)

                    salir = True

            except VerificationExceptions.MisExceptions as err:
                cont += 1
                print(err)

    if cont == 3:
        print("Has llegado al limite de intentos, saliendo...")
    elif salir_sin_guardar:
        print("Saliendo...")
    else:
        GestionXML.aniadir_vehiculo(matricula, marca, modelo, anioFabricacion, tarifaDia, estado, xmlPath)


def baja():
    xmlPath = "vehiculos.xml"
    cont = 0
    salir = False
    matricula = ""

    # Comprobaciones pertinentes
    while not salir:
        matricula = input("Ingrese la matricula del vehiculo o pulse 0 para salir: ")
        if (matricula == "0"):
            salir = True
        else:
            try:
                if not GestionXML.existe_matricula(xmlPath, matricula):
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

    if cont < 3:
        salir = False

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


def modificar():
    xml_path = "vehiculos.xml"
    cont = 0
    salir = False
    matricula = ""

    # Comprobaciones pertinentes
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
                    print("Has alcanzado el limite de intentos, saliendo...")
                    salir = True
                else:
                    VerificationExceptions.hayAlgo(matricula)
                    VerificationExceptions.matFormat(matricula)
                    salir = True

            except VerificationExceptions.MisExceptions as err:
                cont += 1
                print(err)

    if cont < 3:
        salir = False

        while not salir:



            GestionXML.modificar_vehiculo(matricula, xml_path)


def buscar():
    xml_path = "vehiculos.xml"
    cont = 0
    salir = False

    # Comprobaciones pertinentes
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
    xmlPath = "vehiculos.xml"
    GestionXML.leer_vehiculos(xmlPath)


def menu():
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
