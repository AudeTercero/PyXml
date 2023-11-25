import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree
from pathlib import Path
from datetime import datetime


def leerVehiculos(xmlPath):
    if (Path(xmlPath).exists()):
        tree = ET.parse('vehiculos.xml')
        root = tree.getroot()

        if not root.findall('vehiculo'):
            print("No hay vehiculos guardados.")
        else:
            print("========== LISTADO VEHICULOS ==========")
            for elemento in root.iter('vehiculo'):
                idVehiculo = elemento.get('id')
                matricula = elemento.find('matricula').text
                marca = elemento.find('descripcion/marca').text
                modelo = elemento.find('descripcion/modelo').text
                anioFabricacion = elemento.find('anioFabricacion').text
                tarifaDia = elemento.find('tarifaDia').text
                estado = elemento.find('estado').text

                print(f'''****VEHICULO****
                    Id: {idVehiculo}
                    Matricula: {matricula}
                    Marca: {marca}
                    Modelo: {modelo}
                    Anio de Fabricacion: {anioFabricacion}
                    Tarifa Diaria: {tarifaDia}
                    Estado: {estado}        
                    ***********************''')


def aniadirVehiculo(matricula, marca, modelo, anioFabricacion, tarifaDia, estado, xmlPath):  # Mirar tema ID

    try:
        tree = ET.parse(xmlPath)
        root = tree.getroot()
    except FileNotFoundError:
        root = Element('vehiculos')
        tree = ET.ElementTree(root)

    # Creamos el vehiculo y su atributo
    vehiculo = ET.Element('vehiculo')
    id = ET.SubElement(vehiculo, 'id').text = str(obtId(xmlPath, vehiculo))
    vehiculo.set('id', id)

    # Creamos sus atributos o subelementos
    ET.SubElement(vehiculo, 'matricula').text = matricula
    descripcion = ET.SubElement(vehiculo, 'descripcion')
    ET.SubElement(descripcion, 'marca').text = marca
    ET.SubElement(descripcion, 'modelo').text = modelo
    ET.SubElement(vehiculo, 'anioFabricacion').text = str(anioFabricacion)
    ET.SubElement(vehiculo, 'tarifaDia').text = str(tarifaDia)
    ET.SubElement(vehiculo, 'estado').text = estado

    # Agregamos el nuevo vehiculo
    root.append(vehiculo)

    # Guardamos el archivo XML actualizado
    salida = prettify(root)
    file = open("vehiculos.xml", "w")
    file.write(salida)
    file.close()
    eliminarEspacios("vehiculos.xml")


def eliminarVehiculo(matricula, xmlPath):
    try:
        tree = ET.parse(xmlPath)
        root = tree.getroot()

        # Buscamos el vehiculo
        vehiculoBuscado = None

        for vehiculo in root.findall('vehiculo'):
            matVehi = vehiculo.find('matricula').text
            if (matVehi == matricula):
                vehiculoBuscado = vehiculo

        # Si lo encuentra, eliminamos el vehiculo
        if vehiculo is not None:
            root.remove(vehiculo)
            tree.write(xmlPath)
            print("El vehiculo ha sido eliminado")
        else:
            print("El vehiculo no se ha podido eliminar")

    except FileNotFoundError:
        print("No hay vehiculos guardados")
    except Exception as e:
        print(f"Error: {e}")


def modificar_vehiculo(matricula, xmlPath):
    try:
        tree = ET.parse(xmlPath)
        root = tree.getroot()

        # Buscamos el vehiculo
        vehiculoBuscado = None

        for vehiculo in root.findall('vehiculo'):
            matVehi = vehiculo.find('matricula').text
            if (matVehi == matricula):
                vehiculoBuscado = vehiculo

        # Si lo encuentra, modificamos el vehiculo
        if vehiculo is not None:
            root.remove(vehiculo)
            tree.write(xmlPath)
            print("El vehiculo ha sido eliminado")
        else:
            print("El vehiculo no se ha podido encontrar")

    except FileNotFoundError:
        print("No hay vehiculos guardados")
    except Exception as e:
        print(f"Error: {e}")


def buscar_vehiculo():
    print()


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
    id = ET.SubElement(alquiler, 'id').text = str(obtId('alquileres.xml', alquiler))
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
        if (elemento.find('matricula') == matVe):
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


# ******************** FUNCIONES  COMUNES **************************************

def obtId(fichero, etiqueta):
    aux = 1
    if (Path(fichero).exists()):
        tree = ET.parse(fichero)
        root = tree.getroot()
        for elemento in root.iter(etiqueta):
            id = int(elemento.get("id"))
            if (id > aux):
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
