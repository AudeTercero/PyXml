import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree
from pathlib import Path
from datetime import datetime


# ******************** FUNCIONES  VEHICULOS **************************************
# Funcion para ver si existe la matricula
def existe_matricula(fichero, matricula):
    tree = ET.parse(fichero)
    root = tree.getroot()
    for elemento in root.iter('vehiculo'):
        mat_aux = elemento.get('matricula')
        if (matricula == mat_aux):
            return True
    return False


def obtener_vehiculo(xml_path, matricula):
    try:
        tree = ET.parse(xml_path)


# Funcion para mostrar todos los vehiculos guardados
def leer_vehiculos(xml_path):
    if Path(xml_path).exists():
        tree = ET.parse(xml_path)
        root = tree.getroot()

        if not root.findall('vehiculo'):
            print("No hay vehiculos guardados.")
        else:
            print("========== LISTADO VEHICULOS ==========")
            for elemento in root.iter('vehiculo'):
                id_vehiculo = elemento.get('id')
                matricula = elemento.find('matricula').text
                marca = elemento.find('descripcion/marca').text
                modelo = elemento.find('descripcion/modelo').text
                anio_fabricacion = elemento.find('anioFabricacion').text
                tarifa_dia = elemento.find('tarifaDia').text
                estado = elemento.find('estado').text

                print(f'''****VEHICULO****
Id: {id_vehiculo}
Matricula: {matricula}
Marca: {marca}
Modelo: {modelo}
Anio de Fabricacion: {anio_fabricacion}
Tarifa Diaria: {tarifa_dia}
Estado: {estado}        
***********************''')


# Funcion para guardar vehiculos
def aniadir_vehiculo(matricula, marca, modelo, anio_fabricacion, tarifa_dia, estado, xml_path):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
    except FileNotFoundError:
        root = Element('vehiculos')
        tree = ET.ElementTree(root)

    # Creamos el vehiculo y su atributo
    vehiculo = ET.Element('vehiculo')
    vehiculo.set('id', str(obtId(xml_path, "vehiculo")))

    # Creamos sus atributos o subelementos
    ET.SubElement(vehiculo, 'matricula').text = matricula
    descripcion = ET.SubElement(vehiculo, 'descripcion')
    ET.SubElement(descripcion, 'marca').text = marca
    ET.SubElement(descripcion, 'modelo').text = modelo
    ET.SubElement(vehiculo, 'anioFabricacion').text = str(anio_fabricacion)
    ET.SubElement(vehiculo, 'tarifaDia').text = str(tarifa_dia)
    ET.SubElement(vehiculo, 'estado').text = estado

    # Agregamos el nuevo vehiculo
    root.append(vehiculo)

    # Guardamos el archivo XML actualizado
    salida = prettify(root)
    file = open("vehiculos.xml", "w")
    file.write(salida)
    file.close()
    eliminarEspacios("vehiculos.xml")


# Funcion para eliminar vehiculos guardados
def eliminar_vehiculo(matricula, xml_path):
    vehiculo_encontrado = False
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # Buscamos el vehiculo con la matricula indicada por el usuario
        for vehiculo in root.findall('vehiculo'):
            mat_vehi = vehiculo.find('matricula').text
            if (mat_vehi == matricula):
                vehiculo_buscado = vehiculo

        # Si lo encuentra, eliminamos el vehiculo
        if vehiculo_buscado is not None:
            vehiculo_encontrado = True
            salir = False

            # Preguntamos si desea eliminar el vehiculo, de ser asi lo borramos
            while not salir:
                op = input("Seguro que quieres borrar el vehiculo? [S/N]").lower()
                if (op == "s"):
                    root.remove(vehiculo_buscado)
                    tree.write(xml_path)
                    print("El vehiculo ha sido eliminado")
                    salir = True;
                elif (op == "n"):
                    print("Saliendo...")
                else:
                    print("Opcion no valida.")

        # Si no lo encuentra, lo indicamos
        if not vehiculo_encontrado:
            print("No se encontro el vehiculo")

        else:
            print("El vehiculo no se ha podido encontrar")

    except FileNotFoundError:
        print("No hay vehiculos guardados")
    except Exception as e:
        print(f"Error: {e}")


# Funcion para modificar vehiculos guardados
def modificar_vehiculo(matricula, xml_path):
    vehiculo_encontrado = False
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        for vehiculo in root.findall('vehiculo'):
            mat_vehi = vehiculo.find('matricula').text

            if mat_vehi == matricula:
                vehiculo_encontrado = True
                salir = False

                while not salir:
                    opc = input(
                        "\tSelecciona una opcion:\n 1. Modificar ID \n 2. Modificar Matricula\n 3. Modificar Marca\n 4. Modificar Modelo"
                        "\n 5. Modificar Anio de Fabricacion \n 6. Modificar Tarifa Diaria\n 7. Modificar estado "
                        "\n 0. Guardar y salir \n")

                    # Hay que controlar que no se repitan id ni matricula
                    if opc == "1":
                        id_valido = False

                        while not id_valido:
                            nuevo_id = input("Ingresa el nuevo ID del vehiculo")
                            if existe_id(xml_path, nuevo_id, "vehiculo") is not True:
                                id_valido = True
                                modificar_atributo(xml_path, "vehiculo",vehiculo.get("id"), nuevo_id)
                            else:
                                print("El ID introducido ya pertenece a un vehiculo existente.")

                    elif opc == "2":
                        mat_valida = False

                        while not mat_valida:
                            nueva_mat = input("Ingresa la nueva matricula del vehiculo")
                            if existe_matricula(xml_path, nueva_mat) is not True:
                                mat_valida = True
                                modificar_etiqueta(xml_path, "vehiculo", "matricula", vehiculo.find("matricula").text, mat_valida)
                            else:
                                print("La matricula introducida ya pertenece a un vehiculo existente.")

                    elif opc == "3":
                        nuevaMarca = input("Ingrese la nueva marca del vehículo: ")
                        modificar_etiqueta(xml_path, "vehiculo", "descripcion/marca", vehiculo.find("descripcion/marca").text, nuevaMarca)

                    elif opc == "4":
                        nuevoModelo = input("Ingrese el nuevo modelo del vehículo: ")
                        modificar_etiqueta(xml_path, "vehiculo", "descripcion/modelo", vehiculo.find("descripcion/modelo").text, nuevoModelo)

                    elif opc == "5":
                        nuevoAnio = int(input("Ingrese el nuevo año de fabricación del vehículo: "))
                        modificar_etiqueta(xml_path, "vehiculo", "anioFabricacion", vehiculo.find("anioFabricacion").text, nuevoAnio)

                    elif opc == "6":
                        nuevaTarifa = float(input("Ingrese la nueva tarifa por día del vehículo: "))
                        modificar_etiqueta(xml_path, "vehiculo", "tarifaDia", vehiculo.find("tarifaDia").text, nuevaTarifa)

                    elif opc == "7":
                        nuevoEstado = input("Ingrese el nuevo estado del vehículo: ")
                        modificar_etiqueta(xml_path, "vehiculo", "estado", vehiculo.find("estado").text, nuevoEstado)

                    elif opc == "0":
                        salir = True

                    else:
                        print("Esa opcion no existe")

        # Si no lo encuentra, lo indicamos
        if not vehiculo_encontrado:
            print("No se encontro el vehiculo")

    except FileNotFoundError:
        print("No hay vehiculos guardados")
    except Exception as e:
        print(f"Error: {e}")


# Funcion para buscar vehiculos guardados
def buscar_vehiculo(matricula, xml_path):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        for vehiculo in root.findall('vehiculo'):
            mat_vehi = vehiculo.find('matricula').text

            if mat_vehi == matricula:
                id_vehiculo = vehiculo.get('id')
                matricula = vehiculo.find('matricula').text
                marca = vehiculo.find('descripcion/marca').text
                modelo = vehiculo.find('descripcion/modelo').text
                anio_fabricacion = vehiculo.find('anioFabricacion').text
                tarifa_dia = vehiculo.find('tarifaDia').text
                estado = vehiculo.find('estado').text

                print(f'''****VEHICULO****
 Id: {id_vehiculo}
 Matricula: {matricula}
 Marca: {marca}
 Modelo: {modelo}
 Anio de Fabricacion: {anio_fabricacion}
 Tarifa Diaria: {tarifa_dia}
 Estado: {estado}        
 ***********************''')

    except FileNotFoundError:
        print("No hay vehiculos guardados")
    except Exception as e:
        print(f"Error: {e}")


# ******************** FUNCIONES  ALQUILER **************************************
def crearAlquiler(dni, fechaIni, fechaFin, kmIni, idVe):
    try:
        tree = ET.parse('alquileres.xml')
        root = tree.getroot()
    except FileNotFoundError:
        root = Element('alquileres')
        tree = ET.ElementTree(root)

    # Creamos el vehiculo y su atributo
    alquiler = ET.Element('alquiler')
    id = ET.SubElement(alquiler, 'id').text = str(obtId('alquileres.xml', "alquiler"))
    alquiler.set('id', id)

    # Creamos sus atributos o subelementos
    ET.SubElement(alquiler, 'id_vehiculo').text = idVe
    ET.SubElement(alquiler, 'dni').text = dni
    ET.SubElement(alquiler, 'fecha_inicio').text = fechaIni
    ET.SubElement(alquiler, 'fecha_final').text = fechaFin
    ET.SubElement(alquiler, 'kilometros_inicio').text = str(kmIni)
    ET.SubElement(alquiler, 'fecha_devolucion').text = ''
    ET.SubElement(alquiler, 'kilometros_final').text = ''
    ET.SubElement(alquiler, 'precio_final').text = ''
    ET.SubElement(alquiler, 'recargo').text = ''
    ET.SubElement(alquiler, 'estado').text = 'Activo'

    # Agregamos el nuevo vehiculo
    root.append(alquiler)

    # Guardamos el archivo XML actualizado
    salida = prettify(root)
    file = open("alquileres.xml", "w")
    file.write(salida)
    eliminarEspacios("alquileres.xml")
    file.close()
    eliminarEspacios('alquileres.xml')


def obtIdVe(matVe):
    tree = ET.parse('vehiculos.xml')
    root = tree.getroot()
    for elemento in root.iter('vehiculo'):
        idVe = elemento.get('id')
        if (elemento.find('matricula').text == matVe):
            return idVe
    return -1


def finAlquiler(fechaDevo, kmFin, id):
    if (Path('alquileres.xml').exists()):
        tree = ET.parse('alquileres.xml')
        root = tree.getroot()
        for elemento in root.iter('alquiler'):
            if (elemento.get('id') == id):
                fechaIni = elemento.find('fecha_inicio').text
                fechaFin = elemento.find('fecha_final').text
                idVe = elemento.find('id_vehiculo').text
                elemento.find('fecha_devolucion').text = fechaDevo
                elemento.find('kilometros_final').text = kmFin
                auxFin = datetime.strptime(fechaFin, '%Y-%m-%d')
                auxDev = datetime.strptime(fechaDevo, '%Y-%m-%d')
                preciFin = elemento.find('precio_final')
                recargo = elemento.find('recargo')
                diasR = (auxDev - auxFin).days
                if (diasR > 0):
                    recargo.text = str(diasR * 80)
                else:
                    recargo.text = str("No hay recargo")
                preciFin.text = str(precioFin(fechaIni, fechaFin, idVe) + int(recargo.text))
                elemento.find('estado').text = 'Finalizado'

                tree.write('alquileres.xml')


def mostrarTodoAlq():
    if (Path('alquileres.xml').exists()):
        tree = ET.parse('alquileres.xml')
        root = tree.getroot()

        if not root.findall('alquiler'):
            print("No hay alquileres guardados")
        else:
            print("========== LISTADO ALQUILERES ==========")
            for elemento in root.iter('alquiler'):
                idAlquiler = elemento.get('id')
                idVehiculo = elemento.find('id_vehiculo').text
                dni = elemento.find('dni').text
                fechaIni = elemento.find('fecha_inicio').text
                fechaFin = elemento.find('fecha_final').text
                kmIni = elemento.find('kilometros_inicio').text
                kmFin = elemento.find('kilometros_final').text
                precio = elemento.find('precio_final').text
                rec = elemento.find('recargo').text
                est = elemento.find('estado').text

                print(f'''****Alquiler****
Id: {idAlquiler}
Id Vehiculo: {idVehiculo}
DNI Cliente: {dni}
Fecha Inicio: {fechaIni}
Fecha Finalizacion: {fechaFin}
Kilometros Inicio: {kmIni}
Kilometros Finalizacion: {kmFin}
Precio Final: {precio}        
Recargo: {rec}
Estado: {est}
***********************''')
    else:
        print("No hay alquileres aun")


def precioFin(fechaIni, fechaFin, idVe):
    tree = ET.parse('vehiculos.xml')
    root = tree.getroot()
    for elemento in root.iter('vehiculo'):
        if (elemento.get('id') == idVe):
            tarifa = float(elemento.find('tarifaDia').text)
    fecha1 = datetime.strptime(fechaIni, '%Y-%m-%d')
    fecha2 = datetime.strptime(fechaFin, '%Y-%m-%d')
    dias = int((fecha2 - fecha1).days)
    return tarifa * dias


def listado_coches_disponibles():
    tree = ET.parse('vehiculos.xml')
    root = tree.getroot()
    dicVeh = {}
    for elemento in root.iter('vehiculo'):
        idVe = elemento.get('id')
        matVe = elemento.find('matricula').text
        marca = elemento.find('descripcion/marca').text
        modelo = elemento.find('descripcion/modelo').text
        estado = elemento.find('estado').text
        if (estado == 'disponible'):
            dicVeh[idVe] = {'mat': matVe, 'marca': marca, 'modelo': modelo}

    return dicVeh


def diponibles():
    tree = ET.parse('vehiculos.xml')
    root = tree.getroot()

    for elemento in root.iter('vehiculo'):
        estado = elemento.find('estado').text
        if (estado == 'disponible'):
            return True

    return False


def alquiDisp(dniRec):
    if (Path('alquileres.xml').exists()):
        tree = ET.parse('alquileres.xml')
        root = tree.getroot()
        dicAlq = {}
        for elemento in root.iter('alquiler'):
            idAlq = elemento.get('id')
            idVeh = elemento.find('id_vehiculo').text
            dni = elemento.find('dni').text
            fechaIni = elemento.find('fecha_inicio').text
            if (dni == dniRec):
                dicAlq[idAlq] = {'Id_Vehiculo': idVeh, 'Dni': dni, 'Fecha_Inicio': fechaIni}
        return dicAlq
# Este metodo va en GestionXMl y hay que modificar la linea 277 de la funcion obtIdVe(matVe) y ponerle .text
def mostrar_por_elemento(etiqueta, abuscar):
    tree = ET.parse('alquileres.xml')
    root = tree.getroot()
    existencias = False
    for elemento in root.iter('alquiler'):
        idAlquiler = elemento.get('id')
        idVehiculo = elemento.find('id_vehiculo').text
        dni = elemento.find('dni').text
        fechaIni = elemento.find('fecha_inicio').text
        fechaFin = elemento.find('fecha_final').text
        kmIni = elemento.find('kilometros_inicio').text
        kmFin = elemento.find('kilometros_final').text
        precio = elemento.find('precio_final').text
        rec = elemento.find('recargo').text
        est = elemento.find('estado').text
        aux = elemento.find(etiqueta).text
        if (aux == abuscar):
            existencias = True
            print(f'''****Alquiler****
            Id: {idAlquiler}
            Id Vehiculo: {idVehiculo}
            DNI Cliente: {dni}
            Fecha Inicio: {fechaIni}
            Fecha Finalizacion: {fechaFin}
            Kilometros Inicio: {kmIni}
            Kilometros Finalizacion: {kmFin}
            Precio Final: {precio}        
            Recargo: {rec}
            Estado: {est}
            ***********************''')
    if (existencias is False):
        print(f"No hay alquileres con {etiqueta} = {abuscar}")

# ******************** FUNCIONES  COMUNES **************************************

def obtId(fichero, etiqueta):
    aux = 1
    if (Path(fichero).exists()):
        tree = ET.parse(fichero)
        root = tree.getroot()
        for elemento in root.iter(etiqueta):
            id = int(elemento.get("id"))
            if (id >= aux):
                aux = id
    else:
        return aux
    return aux + 1


def eliminarEspacios(fichero):
    if (Path(fichero).exists()):
        with open(fichero, 'r') as file:
            contenido = file.read()
        lineas = [linea for linea in contenido.splitlines() if linea.strip()]
        contenidioSin = '\n'.join(lineas)
        with open(fichero, 'w') as file:
            file.write(contenidioSin)


def prettify(elem):
    from xml.etree import ElementTree
    from xml.dom import minidom

    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


# Funcion para modificar el texto de un elemento(ESTO VA EN GESTIONXML)
def modificar_etiqueta(fichero, iterable, etiqueta, id_elemento, texto_cambio):
    salir = False
    tree = ET.parse(fichero)
    root = tree.getroot()

    for elemento in root.iter(iterable):
        id = elemento.get('id')
        elem = elemento.find(etiqueta)
        if id == id_elemento:
            elem.text = texto_cambio

    while not salir:
        op = input("Quieres guardar los cambios generados?[S/N]").lower()

        if op == "s":
            tree.write(fichero)
            salir = True
            print("Cambios guardados, saliendo...")
        elif op == "n":
            salir = True;
            print("Saliendo sin guardar...")
        else:
            print("Entrada no valida.")


# Funcion para ver si existe la id
def existe_id(fichero, id, etiquieta):
    tree = ET.parse(fichero)
    root = tree.getroot()
    for elemento in root.iter(etiquieta):
        id_aux = elemento.get('id')
        if (id == id_aux):
            return True
    return False


def modificar_atributo(fichero, iterable, id_elemento, textoCambio):
    salir = False
    tree = ET.parse(fichero)
    root = tree.getroot()

    for elemento in root.iter(iterable):
        id = elemento.get('id')
        if (id == id_elemento):
            elemento.set("id", textoCambio)

    while not salir:
        op = input("Quieres guardar los cambios generados?[S/N]").lower()

        if op == "s":
            tree.write(fichero)
            salir = True
            print("Cambios guardados, saliendo...")
        elif op == "n":
            salir = True;
            print("Saliendo sin guardar...")
        else:
            print("Entrada no valida.")
