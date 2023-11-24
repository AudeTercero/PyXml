import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree
from pathlib import Path
from datetime import datetime


def leerVehiculos(xmlPath):
    try:
        tree = ET.parse(xmlPath)
        root = tree.getroot()
        recorrer(root)
        '''
        vehiculosLista = []

        for atributo in root.findall('vehiculo'):
            vehiculoInfo = []

            # Extraer informacion de cada elemento dentro de vehiculo
            id = atributo.find('id').text
            matricula = atributo.find('matricula').text
            marca = atributo.find('.//descripcion/marca').text
            modelo = atributo.find('.//descripcion/modelo').text
            anoFabricacion = atributo.find('anoFabricacion').text
            tarifaDia = atributo.find('tarifaDia').text
            estado = atributo.find('estado').text

            # Agregar la informacion del vehiculo a la lista
            vehiculoInfo.extend([id, matricula, marca, modelo, anoFabricacion, tarifaDia, estado])

            vehiculosLista.append(vehiculoInfo)

        return vehiculosLista
        '''
    except FileNotFoundError:
        print(f"El archivo {xmlPath} no existe.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo XML: {e}")
        return None


def recorrer(elemento, indent=0):
    print(elemento.tag, end="")
    # Para recorrer los atributos. Los atributos estan en un diccionario
    for attr in elemento.attrib:
        attrName = attr
        attrValue = elemento.attrib[attr]
        print("\t", attrName, ":", attrValue, " ", end="")
    print("\n\t", elemento.text)
    for n in elemento:
        recorrer(n)


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


# ******************** FUNCIONES  ALQUILER **************************************
def crearAlquiler(dni, fechaIni, fechaFin, kmIni, matVe):
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
    ET.SubElement(alquiler, 'id_vehiculo').text = obtIdVe(matVe)
    ET.SubElement(alquiler, 'dni').text = dni
    ET.SubElement(alquiler, 'fecha_inicio').text = fechaIni
    ET.SubElement(alquiler, 'fecha_final').text = fechaFin
    ET.SubElement(alquiler, 'kilometros_inicio').text = str(kmIni)
    ET.SubElement(alquiler, 'fecha_devolucion')
    ET.SubElement(alquiler, 'kilometros_final')
    ET.SubElement(alquiler, 'precio_final')
    ET.SubElement(alquiler, 'recargo')
    ET.SubElement(alquiler, 'estado').text = 'Activo'

    # Agregamos el nuevo vehiculo
    root.append(alquiler)

    # Guardamos el archivo XML actualizado
    salida = prettify(root)
    file = open("alquileres.xml", "w")
    file.write(salida)
    eliminarEspacios("alquileres.xml")
    file.close()

def obtIdVe(matVe):
    tree = ET.parse('vehiculos.xml')
    root = tree.getroot()
    for elemento in root.iter('vehiculo'):
        idVe = elemento.get('id')
        if(elemento.find('matricula') == matVe):
            return idVe
    return -1
def finAlquiler(fechaDevo, kmFin, id):
    if (Path('alquileres.xml').exists()):
        tree = ET.parse('alquileres.xml')
        root = tree.getroot()
        for elemento in root.iter('alquiler'):
            if (elemento.get('id') == id):
                fechaIni = elemento.find('fecha_inicio')
                fechaFin = elemento.fidn('fecha_final')
                idVe = elemento.find('id_vehiculo')
                elemento.find('fecha_devolucion').text = fechaDevo
                elemento.find('kilometros_final').text = kmFin
                elemento.find('precio_final').text = precioFin(fechaIni, fechaFin, idVe)
                auxFin = datetime.strptime(fechaFin, '%Y-%m-%d')
                auxDev = datetime.strptime(fechaDevo, '%Y-%m-%d')
                recargo = elemento.find('recargo')
                diasR = (auxDev - auxFin).days
                if (diasR > 0):
                    recargo.text = diasR * 80
                else:
                    recargo.text = 0
                elemento.find('estado').text = 'Finalizado'

                tree.write('alquileres.xml')


def mostrarTodoAlq():
    if (Path('alquileres.xml').exists()):
        tree = ET.parse('alquileres.xml')
        root = tree.getroot()
        print("========== LISTADO ALQUILERES ==========")
        for elemento in root.iter('alquiler'):
            idAlquiler = elemento.get('id')
            idVehiculo = elemento.find('id_vehiculo')
            dni = elemento.find('dni')
            fechaIni = elemento.find('fecha_inicio')
            fechaFin = elemento.fidn('fecha_final')
            kmIni = elemento.find('kilometros_inicio')
            kmFin = elemento.find('kilomtreso_final')
            precio = elemento.find('precio_final')
            rec = elemento.find('recargo')
            est = elemento.find('estado')

            print(f'''****Alquiler****\n
                    \tId: {idAlquiler}\n
                    \tId Vehiculo: {idVehiculo}\n
                    \tDNI Cliente: {dni}\n
                    \tFecha Inicio: {fechaIni}\n
                    \tFecha Finalizacion: {fechaFin}\n
                    \tKilometros Inicio: {kmIni}\n
                    \tKilometros Finalizacion: {kmFin}\n
                    \tPrecio Final: {precio}\n        
                    \tRecargo: {rec}\n
                    \tEstado: {est}''')
    else:
        print("No hay alquileres aun")


def precioFin(fechaIni, fechaFin, idVe):
    tree = ET.parse('vehiculos.xml')
    root = tree.getroot()
    for elemento in root.iter('vehiculo'):
        if (elemento.get('id') == idVe):
            tarifa = float(elemento.find('tarifaDia'))
    fecha1 = datetime.strptime(fechaIni, '%Y-%m-%d')
    fecha2 = datetime.strptime(fechaFin, '%Y-%m-%d')
    dias = int((fecha2 - fecha1).days)
    return tarifa * dias


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
