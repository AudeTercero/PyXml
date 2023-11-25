import GestionXML

def alta():
    xmlPath = "vehiculos.xml"
    lista = GestionXML.leer_vehiculos(xmlPath)

    # Comprobaciones pertinentes

    matricula = input("Ingrese la matrícula del vehículo: ")
    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    anioFabricacion = int(input("Ingrese el año de fabricación del vehículo: "))
    tarifaDia = float(input("Ingrese la tarifa por día del vehículo: "))
    estado = input("Ingrese el estado del vehículo: ")

    # Comprobar si ya existe el vehiculo

    # Si no existe, aniadir vehiculo
    GestionXML.aniadir_vehiculo(matricula, marca, modelo, anioFabricacion, tarifaDia, estado, xmlPath)


def baja():
    xmlPath = "vehiculos.xml"
    # Comprobaciones pertinentes
    matricula = input("Ingrese la matrícula del vehículo: ")

    # Comprobar que el vehiculo existe

    # Preguntar si desea borrarlo

    GestionXML.eliminar_vehiculo(matricula, xmlPath)


def modificar():
    xmlPath = "vehiculos.xml"

    # Comprobaciones pertinentes
    matricula = input("Ingrese la matrícula del vehículo: ")

    # Comprobar que el vehiculo existe
    GestionXML.modificar_vehiculo(matricula,xmlPath)


def buscar():
    xmlPath = "vehiculos.xml"

    # Comprobaciones pertinentes
    matricula = input("Ingrese la matrícula del vehículo: ")

    #Mandamos a buscar el vehiculo por matricula con el metodo buscar_vehiculo
    GestionXML.buscar_vehiculo(matricula,xmlPath)

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
