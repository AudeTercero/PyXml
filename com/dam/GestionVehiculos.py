import GestionXML

def alta():
    xmlPath = "vehiculos.xml"
    lista = GestionXML.leerVehiculos(xmlPath)

    # Comprobaciones pertinentes

    matricula = input("Ingrese la matrícula del vehículo: ")
    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    anioFabricacion = int(input("Ingrese el año de fabricación del vehículo: "))
    tarifaDia = float(input("Ingrese la tarifa por día del vehículo: "))
    estado = input("Ingrese el estado del vehículo: ")

    # Comprobar si ya existe el vehiculo

    # Si no existe, aniadir vehiculo
    GestionXML.aniadirVehiculo(matricula, marca, modelo, anioFabricacion, tarifaDia, estado, xmlPath)


def baja():
    xmlPath = "vehiculos.xml"
    # Comprobaciones pertinentes
    matricula = input("Ingrese la matrícula del vehículo: ")

    # Comprobar que el vehiculo existe

    # Preguntar si desea borrarlo

    GestionXML.eliminarVehiculo(matricula, xmlPath)


def modificar():
    salir = True
    nuevaMatricula, nuevaMarca, nuevoModelo, nuevoAnio, nuevaTarifa, nuevoEstado = ""
    xmlPath = "vehiculos.xml"

    # Comprobaciones pertinentes
    matricula = input("Ingrese la matrícula del vehículo: ")

    # Comprobar que el vehiculo existe
    lista = GestionXML.leerVehiculos(xmlPath)

    #Si existe recogemos sus atributos

    # Preguntar que se desea modificar
    while (salir):
        opc = input(
            "\tSelecciona una opcion: \n 1. Modificar Matricula\n 2. Modificar Marca\n 3. Modificar Modelo"
            "\n 4. Modificar Anio de Fabricacion \n 5. Modificar Tarifa Diaria\n 6. Modificar estado "
            "\n 0. Salir \n")

        if opc == "1":
            nuevaMatricula = input("Ingrese la nueva matrícula del vehículo: ")
        elif opc == "2":
            nuevaMarca = input("Ingrese la nueva marca del vehículo: ")
        elif opc == "3":
            nuevoModelo = input("Ingrese el nuevo modelo del vehículo: ")
        elif opc == "4":
            nuevoAnio = int(input("Ingrese el nuevo año de fabricación del vehículo: "))
        elif opc == "5":
            nuevaTarifa = float(input("Ingrese la nueva tarifa por día del vehículo: "))
        elif opc == "6":
            nuevoEstado = input("Ingrese el nuevo estado del vehículo: ")
        elif opc == "0":
            print("Saliendo...")
            salir = False
        else:
            print("Esa opcion no existe")

    #Si desea guardar
    GestionXML.eliminarVehiculo(matricula)
    GestionXML.aniadirVehiculo(nuevaMatricula, nuevaMarca, nuevoModelo, nuevoAnio, nuevaTarifa, nuevoEstado)


def buscar():
    xmlPath = "vehiculos.xml"

    # Comprobaciones pertinentes
    matricula = input("Ingrese la matrícula del vehículo: ")

    #Comprobamos que existe el vehiculo
    lista = GestionXML.leerVehiculos(xmlPath)

    #Si existe lo mostramos
    if lista:
        for vehiculoInfo in lista:
            if vehiculoInfo[1] == matricula:
                print("=== VECHICULO ===")
                print("ID:", vehiculoInfo[0])
                print("Matrícula:", vehiculoInfo[1])
                print("Marca y Modelo:", vehiculoInfo[2])
                print("Año de Fabricación:", vehiculoInfo[3])
                print("Tarifa por Día:", vehiculoInfo[4])
                print("Estado:", vehiculoInfo[5])


def mostrar():
    xmlPath = "vehiculos.xml"
    lista = GestionXML.leerVehiculos(xmlPath)

    if lista:
        for vehiculoInfo in lista:
            print("=== VECHICULO ===")
            print("ID:", vehiculoInfo[0])
            print("Matrícula:", vehiculoInfo[1])
            print("Marca y Modelo:", vehiculoInfo[2])
            print("Año de Fabricación:", vehiculoInfo[3])
            print("Tarifa por Día:", vehiculoInfo[4])
            print("Estado:", vehiculoInfo[5])
            print("=" * 17)
    else:
        print("No hay vehiculos guardados")

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
